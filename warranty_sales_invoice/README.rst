.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

======================
Warranty Sales Invoice
======================

This module allows you to generate sales order guarantee invoices.


Installation
============

To install this module, don't need anything special.


Configuration
=============

To configure this module, you need to:

#. Go to Configuration -> Companies, select the company that will work with guarantees.
#. Go to the "Warranty" page and set up the "Income Warranty Account" field.


Usage
=====

To use this module, you need to:

#. Go to Sales -> Orders -> Quotations/Orders, create one with products and validate it.
#. Click in **Create Invoice**, there are several options:

     - **Invoiceable lines (deduct down payments):** can indicate a guarantee, this
      will be calculated with the amount without fees that are missing for
      invoicing. Ex:

      If the order have 300€ in total untaxed and the total untaxed
      of the invoices sum 100€, the missing total untaxed are 200€, with this 200€
      if indicated a 10.0% in the field "Warranty Percentage" the system will
      genered 2 invoices 1 normal with 180€ and other (with warranty) with 20€.

    - **Down payment (percentage):** You can indicate a guarantee, this will be
      calculated with the total amount of the sales order applying the percentage of
      the down payment field. Ex:

      If the amount in the sale order are 200€ and the down payment are 10%, the
      amount of the invoice are 20€, but if the warranty percentage are 10%, we will
      have 2 invoices, 1 with one applied percentage of 9% (down payment) and the
      other with 1% (warranty) (the total of the invoices are 20€). The system
      calculate the percentages with this formulas:

          - **down payment percentage** -> down payment percentage - (down payment
            percentage * warranty percentage)
          - **warranty percentage** -> down payment percentage * warranty percentage

    - **Down payment (fixed amount):** You can indicate a guarantee, this will be
      calculated on the amount indicated in the "Initial payment amount" field. Ex:

      If the "amount" are 20€ and the "warranty percentage" are 10%, the system will
      generate 2 invoices, one normal of 18€ and the other with warranty of 2€.

If the system have to create one warranty invoice will check if exist one invoice with warranty in state draft, if exist, the system add the new warranty in this invoice, else will create one.


ROADMAP
=======

[ Enumerate known caveats and future potential improvements.
  It is mostly intended for end-users, and can also help
  potential new contributors discovering new features to implement. ]

* ...


Bug Tracker
===========
Bugs and errors are managed in `issues of GitHub <https://github.com/QubiQ/qu-sale-workflow/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/QubiQ/qu-sale-workflow/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* QubiQ, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Valentin Vinagre <valentin.vinagre@qubiq.es>
* Harald Panten <harald.panten@qubiq.es>

Maintainer
~~~~~~~~~~

This module is maintained by QubiQ.

.. image:: https://pbs.twimg.com/profile_images/702799639855157248/ujffk9GL_200x200.png
   :alt: QubiQ
   :target: https://www.qubiq.es

This module is part of the `QubiQ/qu-sale-workflow <https://github.com/QubiQ/qu-sale-workflow>`_.

To contribute to this module, please visit https://github.com/QubiQ.
