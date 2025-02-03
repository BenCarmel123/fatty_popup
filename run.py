
from flask import Flask
from db import db
from routes.main import main, scheduler
from routes.api import api
import os

app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))
db_dir = os.path.join(base_dir, 'tables')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(base_dir, 'tables', 'main.db')
app.config['SQLALCHEMY_BINDS'] = {
    'event_db': 'sqlite:////' + os.path.join(base_dir, 'tables', 'event.db')
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

scheduler.init_app(app)
scheduler.start()

app.register_blueprint(main)
app.register_blueprint(api, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)