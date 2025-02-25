from flask import Blueprint, request, jsonify
from models.user import Usuario
from config import db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nuevo_usuario = Usuario(nombre=data['nombre'], email=data['email'], password_hash=data['password'])
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
