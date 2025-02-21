import sys
sys.path.append('/home/BenCarmel123/fatty-popup')

from run import app, db
from models import Event
from datetime import datetime, timedelta

def get_next_weekday(target_day):
    today = datetime.now().date()
    days_ahead = (target_day - today.weekday()) % 7
    return today + timedelta(days=days_ahead)

def set_events():
    with app.app_context():
        next_thursday = get_next_weekday(3)
        asaf_events = {event.s_date for event in Event.query.filter(Event.chef1_name == 'Asaf Chetrit').all()}
        new_events = []
        if next_thursday not in asaf_events:
            new_events.append(Event(
                host_name='',
                host_insta='',
                chef1_name='Asaf Chetrit',
                chef1_insta='@asafchetrit',
                chef2_name='',
                chef2_insta='',
                event_name='Carmel Market Ramen',
                type='ramen',
                description='אסף שטרית מכין ראמן צלול מציר עוף וטארה סויה, ותוספת של רולדת פרגית עם אצות. כל חמישי מ12-22 מחוץ לרומיה בר בשוק הכרמל',
                location='Hacarmel 15, Tel Aviv',
                s_date=next_thursday, 
                e_date=next_thursday
            ))

        if new_events:
            db.session.add_all(new_events)
            db.session.commit()

if __name__ == '__main__':
    set_events()
