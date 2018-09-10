# (c) 2018 QubiQ
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def recompute_promotions(self):
        for sel in self:
            promotions = sel.env['sale.promotion'].search([
                ('partners', 'in', sel.partner_id.id),
                ('date_from', '<=', sel.date_order),
                '|',
                ('date_to', '>=', sel.date_order),
                ('date_to', '=', False),
            ])

            if len(promotions) > 0:
                prod_dic = {}
                prod_promo_dic = {}
                for line in sel.order_line:
                    if line.is_free:
                        line.unlink()
                    else:
                        # Create the following dict for each line
                        # {'product_id': [product_qty]}
                        if line.product_id.id not in prod_dic:
                            prod_dic[line.product_id.id] = \
                                [line.product_uom_qty]
                        else:
                            prod_dic[line.product_id.id][0] += \
                                line.product_uom_qty

                        # Add price unit and taxes to the value dict list
                        if len(prod_dic[line.product_id.id]) < 3:
                            prod_dic[line.product_id.id].append(
                                line.price_unit)
                            prod_dic[line.product_id.id].append(
                                line.tax_id.id)

                for promo in promotions:
                    for k, v in prod_dic.items():
                        if k in promo.products.ids:
                            # Get the free quantity
                            free_prod_times = v[0] // promo.product_qty
                            if free_prod_times > 0:
                                free_prod_qty = promo.product_free_qty * \
                                    free_prod_times

                                if promo.is_free_product:
                                    # Create the following dict:
                                    '''
                                        {'promo_product_id': [
                                            'free_product_id', 'qty', 'diff'
                                        ]}
                                    '''
                                    if k not in prod_promo_dic.keys():
                                        prod_promo_dic[k] = [[
                                            promo.product_free.id,
                                            free_prod_qty, 'diff']]
                                    else:
                                        prod_promo_dic[k] += [[
                                            promo.product_free.id,
                                            free_prod_qty, 'diff']]
                                else:
                                    # Create the following dict:
                                    '''
                                        {'promo_product_id': [
                                            'free_product_id', 'free qty',
                                        ]}
                                    '''
                                    if k not in prod_promo_dic.keys():
                                        prod_promo_dic[k] = \
                                            [[k, free_prod_qty]]
                                    else:
                                        prod_promo_dic[k] += \
                                            [[k, free_prod_qty]]

                for i in prod_promo_dic:
                    no_value = False
                    higher = 0
                    for free_prod in prod_promo_dic[i]:
                        prod_obj = sel.env['product.product'].browse(
                                    free_prod[0])
                        if isinstance(free_prod, (list,)):
                            # Get the promo with the most value
                            if len(free_prod) == 3:
                                if prod_obj.list_price > higher:
                                    higher = prod_obj.list_price
                                    prod_obj_def = prod_obj
                                    no_value = True
                            else:
                                if prod_dic[i][1] > higher:
                                    higher = prod_dic[i][1]
                                    prod_obj_def = prod_obj
                                    no_value = False
                    if no_value:
                        higher = 0
                        prod_line_obj = prod_obj_def
                    else:
                        prod_line_obj = sel.env.ref(
                            'sale_promotion.free_product')
                        higher = -higher

                    # Create line with the most valuable promo
                    sel.write({
                        'order_line': [(0, 0, {
                            'product_id': prod_line_obj.id,
                            'name': prod_obj_def.name,
                            'product_uom_qty': prod_promo_dic[i][0][1],
                            'price_unit': higher,
                            'is_free': True,
                        })]
                    })
            else:
                # Unlink all promos if no one is found when recalculating
                for line in sel.order_line:
                    if line.is_free:
                        line.unlink()
