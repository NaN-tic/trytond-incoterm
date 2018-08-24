# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond import backend
from trytond.pool import PoolMeta, Pool
from trytond.model import fields, ModelSQL, ValueMixin
from trytond.tools.multivalue import migrate_property

__all__ = ['Party', 'PartyIncoterm']

incoterm = fields.Many2One('incoterm', 'Incoterm')
incoterm_place = fields.Char('Incoterm Name Place')


class Party(metaclass=PoolMeta):
    __name__ = 'party.party'
    incoterm = fields.MultiValue(incoterm)
    incoterm_place = fields.MultiValue(incoterm_place)

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field in {'incoterm', 'incoterm_place'}:
            return pool.get('party.party.incoterm')
        return super(Party, cls).multivalue_model(field)


class PartyIncoterm(ModelSQL, ValueMixin):
    "Party Payment Term"
    __name__ = 'party.party.incoterm'
    party = fields.Many2One(
        'party.party', "Party", ondelete='CASCADE', select=True)
    incoterm = incoterm
    incoterm_place = incoterm_place

    @classmethod
    def __register__(cls, module_name):
        TableHandler = backend.get('TableHandler')
        exist = TableHandler.table_exist(cls._table)

        super(PartyIncoterm, cls).__register__(module_name)

        if not exist:
            cls._migrate_property([], [], [])

    @classmethod
    def _migrate_property(cls, field_names, value_names, fields):
        field_names.extend(['incoterm', 'incoterm_place'])
        value_names.extend(['incoterm', 'incoterm_place'])
        migrate_property(
            'party.party', field_names, cls, value_names,
            parent='party', fields=fields)
