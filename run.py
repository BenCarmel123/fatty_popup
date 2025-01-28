from flask import Flask, send_from_directory
from db import db
from routes.main import main
from routes.api import api
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(base_dir, 'tables')


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'tables', 'main.db')
app.config['SQLALCHEMY_BINDS'] = {
    'event_db': 'sqlite:///' + os.path.join(base_dir, 'tables', 'event.db')
}


app.config.update(
    ADMIN_USERNAME='affogato_master',
    ADMIN_PASSWORD='BenjiBear1',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SECRET_KEY=os.getenv('SECRET_KEY', 'benji')
)


os.makedirs(os.path.join(base_dir, 'tables'), exist_ok=True)


db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/.well-known/pki-validation/66B796875537BB3FC99ADC2E818CE5D4.txt')
def serve_validation_file():
    return send_from_directory('.well-known/pki-validation', '66B796875537BB3FC99ADC2E818CE5D4.txt')


app.register_blueprint(main)
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
