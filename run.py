from flask import Flask
from db import db
from routes.main import main
from routes.api import api
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(base_dir, 'tables')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_dir, "main.db")}'
app.config['SQLALCHEMY_BINDS'] = {
    'event_db': f'sqlite:///{os.path.join(db_dir, "event.db")}'
}

app.config.update(
   ADMIN_USERNAME='affogato_master',
   ADMIN_PASSWORD='scrypt:32768:8:1$fXNTcI8NgZAXrdgV$221bd9826f5e38a63dc2709eefd44ba3ee83a7885c504727e5282b933a6d554fd793c06e3c09d137e4c5f3722082816c6fee335f6caa35242b0c8b023f865694',
   SQLALCHEMY_TRACK_MODIFICATIONS=False,
   SECRET_KEY=os.getenv('SECRET_KEY', 'benji')
)

os.makedirs(os.path.join(base_dir, 'tables'), exist_ok=True)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(main)
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)