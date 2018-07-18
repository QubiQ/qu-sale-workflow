.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================
Pricelist Triple Discount
=========================

Este módulo extiende la funcionalidad del módulo sale_triple_discount permitiendo asignar 3 descuentos en las listas de precios.

Estos 3 descuentos se aplicarán consecutivamente en las sale order que trabajen con esa pricelist,
es decir, se aplica el descuento 1 sobre el precio base y al nuevo precio resultante le aplicamos el descuento 2, etc.


Installation
============

No se requiere de ninguna instalación especial.

Configuration
=============

Activar "Discounts" y "Multiple Sales Prices per Product" en la configuración de ventas.
Seleccionar "Prices computed from formulas" debajo de "Multiple Sales Prices per Product".


Usage
=====

Si la pricelist tiene como politica **incluir el descuento en el precio**, en la líneas de venta los 3 campos
de descuento aparecerán vacíos pero el precio del producto aparecerá con los descuentos aplicados. Esos 3 campos de
descuento se pueden utilizar para aplicar aún más descuentos sobre el precio final.

Si la pricelist tiene como política de descuentos **enseñar el descuento al consumidor**, el precio base del producto se mantendrá en las líneas y se traspasarán los descuentos incluidos en la pricelist.


Gestión de errores
==================

Los errores/fallos se gestionan en `las incidencias de GitHub <https://github.com/QubiQ/qu-sale-workflow/issues>`_.
En caso de problemas, compruebe por favor si su incidencia ha sido ya
reportada. Si fue el primero en descubrirla, ayúdenos a solucionarla indicando
una detallada descripción `aquí <https://github.com/QubiQ/qu-sale-workflow/issues/new>`_.

Créditos
========

Contribudores
-------------

* Oscar Navarro <oscar.navarro@qubiq.es>

Maintainer
----------

This module is maintained by the Qubiq.
