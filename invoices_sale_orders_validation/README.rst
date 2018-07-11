.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================
Invoices Sale Orders Validation
===============================

Se realiza una comprobación de crédito y método de pago al crear/editar pedidos de venta y facturas de cliente según la compañía asociada.

Installation
============

No es necesario nada en especial

Configuration
=============

Se debe de ir a la compañía que se requiera realizar el control:

* Activar el check 'Invoices and Sale Orders Validation'
* Indicar el total máximo en el campo 'Amount Untaxed'
* Si se requiere que esta validación sea para todos los modos de pago el campo 'Payment mode' se debe de dejar vacio, en caso contrario la validación será utilizada en el metodo de pago indicado.

Usage
=====

Cuando se crea/graba una factura de venta o un presupuesto/pedido de venta se comprueba que cumpla las restricciones.


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

* Valentin Vinagre <valentin.vinagre@qubiq.es>
* Xavier Piernas <xavier.piernas@qubiq.es>

Maintainer
----------

This module is maintained by the Qubiq.
