from flask import Blueprint, request, jsonify
from models.reserva import Reserva
from config import db

reserva_bp = Blueprint('reserva_bp', __name__)

@reserva_bp.route('/reservas', methods=['POST'])
def hacer_reserva():
    data = request.get_json()
    nueva_reserva = Reserva(usuario_id=data['usuario_id'], servicio=data['servicio'], fecha_reserva=data['fecha_reserva'])
    db.session.add(nueva_reserva)
    db.session.commit()
    return jsonify({"mensaje": "Reserva realizada con éxito"}), 201
