import sys
sys.path.append('/home/BenCarmel123/fatty-popup')
from run import app, db
from models import Event
from datetime import datetime

def cleanup_old_events():
    with app.app_context():
        old_events = Event.query.filter(Event.e_date < datetime.now().date()).all()
        for event in old_events:
            db.session.delete(event)
        db.session.commit()

if __name__ == '__main__':
    cleanup_old_events()