from app.config.config import db

# Colección donde se guardan las métricas
metricas_collection = db["metricas"]

def guardar_metrica(data):
    """Inserta una nueva métrica en la base de datos"""
    resultado = metricas_collection.insert_one(data)
    return str(resultado.inserted_id)

def obtener_metricas():
    """Obtiene todas las métricas guardadas"""
    metricas = list(metricas_collection.find({}, {"_id": 0}))
    return metricas

def obtener_resumen_financiero():
    """Suma los ingresos agrupados por categoria"""
    pipeline = [
        {"$match": {"tipo": "ingreso"}},
        {"$group": {
            "_id": "$categoria",
            "total": {"$sum": "$valor"}
        }}
    ]
    resultado = list(metricas_collection.aggregate(pipeline))
    return [{"categoria": r["_id"], "total": r["total"]} for r in resultado]

def obtener_concurrencia():
    """Cuenta cuantas veces aparece cada servicio (RF-AN-02)"""
    pipeline = [
        {"$group": {
            "_id": "$servicio",
            "cantidad": {"$sum": 1}
        }},
        {"$sort": {"cantidad": -1}}
    ]
    resultado = list(metricas_collection.aggregate(pipeline))
    return [{"servicio": r["_id"], "cantidad": r["cantidad"]} for r in resultado]