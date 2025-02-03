import sys
sys.path.append('/home/BenCarmel123/fatty-popup')
from run import app, db
from models import Event
from datetime import datetime, timedelta

def get_next_thursday():
    today = datetime.now().date()
    days_ahead = (3 - today.weekday()) % 7
    return today + timedelta(days=days_ahead)

def get_next_saturday():
    today = datetime.now().date()
    days_ahead = (5 - today.weekday()) % 7
    return today + timedelta(days=days_ahead)

def set_events():
    with app.app_context():
        next_thursday = get_next_thursday()
        next_saturday = get_next_saturday()
        asaf_chetrit_events = Event.query.filter(Event.host == 'Asaf Chetrit').all()
        flag1 = False
        flag2 = False
        for event in asaf_chetrit_events:
            if event.date == next_thursday:
                flag1 = True
            if event.date == next_saturday:
                flag2 = True
        if not flag1:
            event1 = Event(
                host='Asaf Chetrit',
                event_name='Carmel Market Ramen',
                event_type='ramen',
                description=' .אסף שטרית מכין ראמן צלול מציר עוף וטארה סויה, ותוספת של רולדת פרגית עם אצות. כל חמישי מ12-22 מחוץ לרומיה בר בשוק הכרמל',
                address='Hacarmel 15, Tel Aviv',
                date=get_next_thursday(),
                time=datetime.strptime('12:00', "%H:%M").time(),
                price_range='?? - ??')
            db.session.add(event1)
        if not flag2:
            event2 = Event(
                host='Asaf Chetrit',
                event_name='Ramen at roots',
                event_type='ramen',
                description='אסף שטרית מכין ראמן צלול מציר עוף וטארה סויה, ותוספת של רולדת פרגית עם אצות. כל מוצ"ש מ17 ברוטס בר.',
                address='roots bar, Tel Aviv',
                date=get_next_saturday(),
                time=datetime.strptime('17:00', "%H:%M").time(),
                price_range='?? - ??')
            db.session.add(event2)
        db.session.commit()

if __name__ == '__main__':
    set_events()