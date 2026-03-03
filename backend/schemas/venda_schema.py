from marshmallow import Schema, fields, EXCLUDE

class VendaSchema(Schema):
    class Meta:
        unknown = EXCLUDE  # ignora campos que não estiverem no schema (evita 400 por campo extra)

    id = fields.Int(dump_only=True)
    cliente = fields.Str(required=True)
    produto = fields.Str(required=True)
    valor = fields.Float(required=True)

    # Aceita o valor vindo do <input type="date"> => "YYYY-MM-DD"
    data_venda = fields.Date(required=False, allow_none=True)