from config import db

class Reserva(db.Model):
    __tablename__ = 'reservas'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    servicio = db.Column(db.String(100), nullable=False)
    fecha_reserva = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.Enum('pendiente', 'confirmada', 'cancelada'), default='pendiente')

    usuario = db.relationship('Usuario', backref=db.backref('reservas', lazy=True))

    def __init__(self, usuario_id, servicio, fecha_reserva, estado='pendiente'):
        self.usuario_id = usuario_id
        self.servicio = servicio
        self.fecha_reserva = fecha_reserva
        self.estado = estado
