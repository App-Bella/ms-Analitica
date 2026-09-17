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