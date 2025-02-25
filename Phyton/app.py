from flask import Flask
from config import init_app
from routes.auth_routes import auth_bp
from routes.reserva_routes import reserva_bp

app = Flask(__name__)
init_app(app)

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(reserva_bp, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True)
