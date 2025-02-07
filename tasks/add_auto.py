import sys
sys.path.append('/home/BenCarmel123/fatty-popup')
from run import app, db
from models import Event
from datetime import datetime, timedelta


def get_next_tuesday():
    today = datetime.now().date()
    days_ahead = (1 - today.weekday()) % 7
    return today + timedelta(days=days_ahead)

def get_next_wednesday():
    today = datetime.now().date()
    days_ahead = (2 - today.weekday()) % 7
    return today + timedelta(days=days_ahead)

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
        next_tuesday = get_next_tuesday()
        next_wednesday = get_next_wednesday()
        next_thursday = get_next_thursday()
        next_saturday = get_next_saturday()
        fifi_events = Event.query.filter(Event.host == 'Fifi').all()
        asaf_chetrit_events = Event.query.filter(Event.host == 'Asaf Chetrit').all()
        a_flag1 = False
        a_flag2 = False
        f_flag1 = False
        f_flag2 = False
        for event in fifi_events:
            if event.date == next_tuesday:
                f_flag1 = True
            if event.date == next_wednesday:
                f_flag2 = True
        if not f_flag1:
            event1 = Event(
                host='Fifi',
                event_name='Fifi\'s at Yaya',
                event_type='ramen',
                description='יפעת תבואה, הידועה בתור פיפיז ראמן, מגיעה עד הודעה חדשה ליאיא לוינסקי כל שלישי ורביעי מ19:00-23:00 להציע תפריט פיוזן של ראמן,כיסונים ועוד ביסים טובים',
                address='Yaya Levinsky, Tel Aviv',
                date=get_next_tuesday(),
                time=datetime.strptime('19:00', "%H:%M").time(),
                price_range='?? - ??', contact='@fifisasianfood')
            db.session.add(event1)
        if not f_flag2:
            event2 = Event(
                host='Fifi',
                event_name='Fifi\'s at Yaya',
                event_type='ramen',
                description='יפעת תבואה, הידועה בתור פיפיז ראמן, מגיעה עד הודעה חדשה ליאיא לוינסקי כל שלישי ורביעי מ19:00-23:00 להציע תפריט פיוזן של ראמן,כיסונים ועוד ביסים טובים',
                address='Yaya Levinsky, Tel Aviv',
                date=get_next_wednesday(),
                time=datetime.strptime('19:00', "%H:%M").time(),
                price_range='?? - ??', contact='@fifisasianfood')
            db.session.add(event1)
            db.session.add(event2)
        for event in asaf_chetrit_events:
            if event.date == next_thursday:
                a_flag1 = True
            if event.date == next_saturday:
                a_flag2 = True
        if not a_flag1:
            event1 = Event(
                host='Asaf Chetrit',
                event_name='Carmel Market Ramen',
                event_type='ramen',
                description=' .אסף שטרית מכין ראמן צלול מציר עוף וטארה סויה, ותוספת של רולדת פרגית עם אצות. כל חמישי מ12-22 מחוץ לרומיה בר בשוק הכרמל',
                address='Hacarmel 15, Tel Aviv',
                date=get_next_thursday(),
                time=datetime.strptime('12:00', "%H:%M").time(),
                price_range='?? - ??', contact='@asafchetrit')
            db.session.add(event1)
        if not a_flag2:
            event2 = Event(
                host='Asaf Chetrit',
                event_name='Ramen at roots',
                event_type='ramen',
                description='אסף שטרית מכין ראמן צלול מציר עוף וטארה סויה, ותוספת של רולדת פרגית עם אצות. כל מוצ"ש מ17 ברוטס בר.',
                address='roots bar, Tel Aviv',
                date=get_next_saturday(),
                time=datetime.strptime('17:00', "%H:%M").time(),
                price_range='?? - ??', contact='@asafchetrit')
            db.session.add(event2)
        db.session.commit()

if __name__ == '__main__':
    set_events()
