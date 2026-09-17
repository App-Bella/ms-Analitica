from flask import Flask
from app.config.config import Config

app = Flask(__name__)

@app.route('/')
def inicio():
    return {"mensaje": "MS-Analitica corriendo correctamente"}

if __name__ == '__main__':
    app.run(port=Config.PORT, debug=True)