from models import Event
from run import db, app 
from datetime import datetime

def cleanup_old_events():
    with app.app_context():
        old_events = Event.query.filter(Event.date < datetime.now().date()).all()
        for event in old_events:
            db.session.delete(event)
        db.session.commit()

if __name__ == '__main__':
    cleanup_old_events()