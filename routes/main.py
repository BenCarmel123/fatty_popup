from flask import Blueprint, render_template, request, flash, redirect, current_app, session
from datetime import datetime , timedelta
from db import db
from models import Event
from form_validations.event_valid import validate_event

main = Blueprint('main', __name__)

def get_sorted_events(like=None):
    query = Event.query
    if like:
        query = query.filter(Event.event_type.ilike(like))
    return query.order_by(Event.date).all()

def event_counter(gap):
    date_a = datetime.now().date()
    date_b = (datetime.now() + timedelta(days=gap)).date()
    return Event.query.filter(Event.date >= date_a, Event.date <= date_b).count()


@main.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@main.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('login.html', input_username = '')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == current_app.config['ADMIN_USERNAME'] and password == current_app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            return redirect('/admin')
        else:
            flash("Incorrect Username and/or Password, please try again")
            return render_template('login.html', input_username=username)

@main.route('/admin', methods=['GET', 'POST'])
def admin_page():
    if not session.get('logged_in'):
        return redirect('/')
    if request.method == 'GET':
     return render_template('admin.html', first_name='Ben', events = get_sorted_events(None))


@main.route('/admin/<int:id>', methods=['POST'])
def delete_event_by_id(id):
    event = Event.query.get(id)
    if not event:
        flash("Event not found")
        return render_template('admin.html', events = get_sorted_events(None), first_name='Ben')
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted successfully")
    return render_template('admin.html', events = get_sorted_events(None), first_name='Ben')

@main.route('/pop')
def pop_list():
    return render_template('pop.html', event_count=event_counter(30))

@main.route('/ramen')
def ramen_list():
    ramen_list = get_sorted_events('ramen')
    return render_template('ramen.html', ramen_list=ramen_list)

@main.route('/other')
def other_list():
    event_list = get_sorted_events(None)
    ramen_list = get_sorted_events('ramen')
    other_list = [event for event in event_list if event not in ramen_list]
    return render_template('other.html', other_list=other_list)

@main.route('/event', methods=['GET', 'POST'])
def event_form():
    # If the form is submitted
    if request.method == 'POST':
        host = request.form['host']
        event_name = request.form['event_name']
        event_type = request.form['event_type']
        description = request.form['description']
        address = request.form['address']
        date = datetime.strptime(request.form['date'], "%Y-%m-%d").date()
        time = datetime.strptime(request.form['time'], "%H:%M").time()
        price_range = request.form['price_range']
        contact = request.form['contact']
        exists = Event.query.filter(
            Event.address.ilike(address.strip()),
            Event.date == date,
            Event.time == time
        ).first()
        # Check if event already exists
        if exists: 
            flash("Event already registered")
            return render_template('admin.html', first_name='Ben', events = get_sorted_events(None))
        
        # Validate event
        message = validate_event(host,event_name,event_type, description, address, date, time, price_range, contact)
        if message == "":
            new_event = Event(
                host=host,
                event_name=event_name,
                event_type=event_type,
                description=description,
                address=address,
                date=date,
                time=time,
                price_range=price_range,
                contact=contact
            )
            db.session.add(new_event)
            db.session.commit()
            return render_template('admin.html', my_events = get_sorted_events(None), first_name='Ben')
        else:
            flash(message)
            return render_template('event.html', form_data=request.form)
    return render_template('event.html')



