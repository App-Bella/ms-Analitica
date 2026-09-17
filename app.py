from flask import Flask
from app.config.config import Config
from app.routes.analitica_routes import analitica_bp

app = Flask(__name__)
app.register_blueprint(analitica_bp, url_prefix='/analitica')

@app.route('/')
def inicio():
    return {"mensaje": "MS-Analitica corriendo correctamente"}

if __name__ == '__main__':
    app.run(port=Config.PORT, debug=True)