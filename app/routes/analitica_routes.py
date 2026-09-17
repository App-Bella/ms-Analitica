from flask import Blueprint, request, jsonify
from app.models.metrica_model import (
    guardar_metrica,
    obtener_metricas,
    obtener_resumen_financiero,
    obtener_concurrencia
)

analitica_bp = Blueprint('analitica', __name__)

@analitica_bp.route('/metricas', methods=['POST'])
def crear_metrica():
    data = request.get_json()
    id_metrica = guardar_metrica(data)
    return jsonify({"mensaje": "Metrica guardada", "id": id_metrica}), 201

@analitica_bp.route('/metricas', methods=['GET'])
def listar_metricas():
    metricas = obtener_metricas()
    return jsonify(metricas), 200

@analitica_bp.route('/financiero', methods=['GET'])
def resumen_financiero():
    resumen = obtener_resumen_financiero()
    return jsonify(resumen), 200

@analitica_bp.route('/concurrencia', methods=['GET'])
def reporte_concurrencia():
    concurrencia = obtener_concurrencia()
    return jsonify(concurrencia), 200