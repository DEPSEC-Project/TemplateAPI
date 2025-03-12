from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import db
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import re

auth_bp = Blueprint("auth", __name__)
limiter = Limiter(get_remote_address, default_limits=["5 per minute"])

@auth_bp.route('/toto', methods=['POST'])
def toto():
    data = request.json
    return jsonify({"msg":""}), 201

@auth_bp.route('/tutu', methods=['POST'])
@limiter.limit("5 per minute") 
def tutu():
    data = request.json

    return jsonify({"msg": ""}), 401




