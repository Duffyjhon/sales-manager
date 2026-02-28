from flask import Blueprint, request, jsonify
from backend.services.venda_service import VendaService
from backend.schemas.venda_schema import VendaSchema

vendas_bp = Blueprint("vendas", __name__, url_prefix="/vendas")
venda_schema = VendaSchema()
vendas_schema = VendaSchema(many=True)


@vendas_bp.post("/")
def criar_venda():
    dados = request.json
    erros = venda_schema.validate(dados)

    if erros:
        return jsonify(erros), 400

    venda = VendaService.criar_venda(
        cliente=dados["cliente"],
        produto=dados["produto"],
        valor=dados["valor"]
    )

    return venda_schema.dump(venda), 201

@vendas_bp.delete("/<int:venda_id>")
def deletar_venda(venda_id):
    sucesso = VendaService.deletar_venda(venda_id)

    if not sucesso:
        return jsonify({"error": "Venda não encontrada"}), 404

    return jsonify({"message": "Venda excluída com sucesso"}), 200


@vendas_bp.get("/")
def listar_vendas():
    vendas = VendaService.listar_vendas()
    return vendas_schema.dump(vendas), 200

@vendas_bp.get("")
def listar_vendas_sem_barra():
    return listar_vendas()
