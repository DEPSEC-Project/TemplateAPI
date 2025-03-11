from flask import Flask,jsonify
from app.config import Config
from app.extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @jwt.unauthorized_loader   # gérer le cas ou le client n'est pas authentifié
    def unauthorized_callback(callback):
        return jsonify({"msg": "Token invalide ou manquant. veuillez vous authentifier."}), 401

    from app.routes.routes1 import auth_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(routes_bp, url_prefix='/blabla')

    return app
