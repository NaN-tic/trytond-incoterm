# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, DeactivableMixin, fields

__all__ = ['Incoterm']


class Incoterm(DeactivableMixin, ModelSQL, ModelView):
    'Incoterm'
    __name__ = 'incoterm'
    name = fields.Char("Name", required=True, translate=True)
    code = fields.Char("Code", required=True)
    description = fields.Char("Description")
    place_required = fields.Boolean("Place required",
        help="Make place required for this incoterm")

    def get_rec_name(self, name):
        return '%s - %s' % (self.code, self.name)

    @classmethod
    def search_rec_name(cls, name, clause):
        return ['OR',
            ('code',) + tuple(clause[1:]),
            ('name',) + tuple(clause[1:]),
            ]
