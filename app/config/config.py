import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/pontebella_analitica_db")
    PORT = int(os.getenv("PORT", 5001))

# Conexión a MongoDB
client = MongoClient(Config.MONGO_URI)
db = client.get_database()