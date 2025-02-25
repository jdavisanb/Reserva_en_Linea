from config import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    rol = db.Column(db.Enum('cliente', 'admin'), default='cliente')

    def __init__(self, nombre, email, password_hash, rol='cliente'):
        self.nombre = nombre
        self.email = email
        self.password_hash = password_hash
        self.rol = rol
