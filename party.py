# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Party']


class Party:
    __metaclass__ = PoolMeta
    __name__ = 'party.party'
    incoterm = fields.Property(fields.Many2One('incoterm', 'Incoterm'))
    incoterm_place = fields.Property(fields.Char('Incoterm Name Place'))
