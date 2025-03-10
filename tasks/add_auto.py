import sys
sys.path.append('/home/BenCarmel123/fatty-popup')
from run import app, db
from models import Event
from datetime import datetime, timedelta

def get_next_weekdays(target_day, num_weeks=3):
    today = datetime.now().date()
    days_ahead = (target_day - today.weekday()) % 7
    next_day = today + timedelta(days=days_ahead)

    dates = []
    for week in range(num_weeks):
        dates.append(next_day + timedelta(weeks=week))

    return dates

def set_events():
    with app.app_context():
        next_thursdays = get_next_weekdays(3, 3)
        asaf_events = {event.s_date for event in Event.query.filter(Event.chef1_name == 'Asaf Chetrit').all()}

        new_events = []
        for thursday in next_thursdays:
            if thursday not in asaf_events:
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
                    location='HaCarmel 15',
                    s_date=thursday,
                    e_date=thursday,
                    res_link='https://www.instagram.com/asafchetrit/'
                ))

        if new_events:
            db.session.add_all(new_events)
            db.session.commit()

if __name__ == '__main__':
    set_events()