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
        next_tuesday = get_next_weekday(1)
        next_wednesday = get_next_weekday(2)
        next_thursday = get_next_weekday(3)
        next_saturday = get_next_weekday(5)

        fifi_events = {event.s_date for event in Event.query.filter(Event.chef1_name == 'Fifi').all()}
        asaf_events = {event.s_date for event in Event.query.filter(Event.chef1_name == 'Asaf Chetrit').all()}

        new_events = []

        if next_tuesday not in fifi_events:
            new_events.append(Event(
                host_name='Yaya Levinsky',
                host_insta='@yaya_levinsky',
                chef1_name='Fifi',
                chef1_insta='@fifisasianfood',
                event_name="Fifi's at Yaya",
                event_type='ramen',
                description='יפעת תבואה, הידועה בתור פיפיז ראמן, מגיעה עד הודעה חדשה ליאיא לוינסקי כל שלישי ורביעי מ19:00-23:00 להציע תפריט פיוזן של ראמן,כיסונים ועוד ביסים טובים',
                location='Yaya Levinsky, Tel Aviv',
                s_date=next_tuesday,
                e_date=next_tuesday
            ))

        if next_wednesday not in fifi_events:
            new_events.append(Event(
                host_name='Yaya Levinsky',
                host_insta='@yaya_levinsky',
                chef1_name='Fifi',
                chef1_insta='@fifisasianfood',
                event_name="Fifi's at Yaya",
                event_type='ramen',
                description='יפעת תבואה, הידועה בתור פיפיז ראמן, מגיעה עד הודעה חדשה ליאיא לוינסקי כל שלישי ורביעי מ19:00-23:00 להציע תפריט פיוזן של ראמן,כיסונים ועוד ביסים טובים',
                location='Yaya Levinsky, Tel Aviv',
                s_date=next_wednesday,
                e_date=next_wednesday
            ))

        if next_thursday not in asaf_events:
            new_events.append(Event(
                chef1_name='Asaf Chetrit',
                chef1_insta='@asafchetrit',
                event_name='Carmel Market Ramen',
                event_type='ramen',
                description='אסף שטרית מכין ראמן צלול מציר עוף וטארה סויה, ותוספת של רולדת פרגית עם אצות. כל חמישי מ12-22 מחוץ לרומיה בר בשוק הכרמל',
                location='Hacarmel 15, Tel Aviv',
                s_date=next_thursday, 
                e_date=next_thursday
            ))

        if next_saturday not in asaf_events:
            new_events.append(Event(
                host_name='roots Bar',
                host_insta='@rootstlv',
                chef1_name='Asaf Chetrit',
                chef1_insta='@asafchetrit',
                event_name='Ramen at Roots',
                event_type='ramen',
                description='אסף שטרית מכין ראמן צלול מציר עוף וטארה סויה, ותוספת של רולדת פרגית עם אצות. כל מוצ"ש מ17 ברוטס בר.',
                location='Roots Bar, Tel Aviv',
                s_date=next_saturday,
                e_date=next_saturday
            ))

        if new_events:
            db.session.add_all(new_events)
            db.session.commit()

if __name__ == '__main__':
    set_events()
