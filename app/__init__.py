from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .routes import employees_bp
    app.register_blueprint(employees_bp, url_prefix="/api")

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    return app
