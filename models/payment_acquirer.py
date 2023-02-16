# coding: utf-8
import logging

from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class AcquirerBac(models.Model):
    _inherit = 'payment.acquirer'
    
    provider = fields.Selection(selection_add=[('bac', 'BAC')], ondelete={'bac': 'set default'})
    bac_key_id = fields.Char('Key ID', required_if_provider='bac', groups='base.group_user')
    bac_key_text = fields.Char('Key Text', required_if_provider='bac', groups='base.group_user')

    def _bac_get_api_url(self):
        self.ensure_one()
        if self.state == 'enabled':
            return "https://credomatic.compassmerchantsolutions.com/cart/cart.php"
        else:
            return "https://credomatic.compassmerchantsolutions.com/cart/cart.php"
            
    def _get_default_payment_method_id(self):
        self.ensure_one()
        if self.provider != 'bac':
            return super()._get_default_payment_method_id()
        return self.env.ref('payment_bac.payment_method_bac').id