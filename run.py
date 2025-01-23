from flask import Flask
from db import db
from routes.main import main
from routes.api import api
import os

app = Flask(__name__)

base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(base_dir, 'tables')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tables', 'main.db')
app.config['SQLALCHEMY_BINDS'] = {
    'event_db': 'sqlite:////' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tables', 'event.db')
}

app.config.update(
    ADMIN_USERNAME=os.getenv('ADMIN_USERNAME', 'default_user'),
    ADMIN_PASSWORD=os.getenv('ADMIN_PASSWORD', 'default_pass'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SECRET_KEY=os.getenv('SECRET_KEY', 'default_secret')
)

os.makedirs('/home/BenCarmel123/fatty-popup/tables', exist_ok=True)

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(main)
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)