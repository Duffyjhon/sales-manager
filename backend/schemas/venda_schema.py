from marshmallow import Schema, fields

class VendaSchema(Schema):
    id = fields.Int(dump_only=True)
    cliente = fields.Str(required=True)
    produto = fields.Str(required=True)
    valor = fields.Float(required=True)
