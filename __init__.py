# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import configuration
from . import sale

def register():
    Pool.register(
        configuration.Configuration,
        configuration.ConfigurationCompany,
        sale.StockMove,
        sale.Sale,
        sale.SaleLine,
        sale.Move,
        sale.MoveLine,
        module='sale_stock_account_move', type_='model')
