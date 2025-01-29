from flask import Blueprint, render_template, request, flash, redirect, current_app 
from datetime import datetime , timedelta
from db import db
from models import Event
from form_validations.event_valid import validate_event

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('home.html')

@main.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('admin_login.html', input_username = '')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == current_app.config['ADMIN_USERNAME'] and password == current_app.config['ADMIN_PASSWORD']:
            return redirect('/admin_page')
        else:
            flash("Incorrect Username and/or Password, please try again")
            return render_template('admin_login.html', input_username=username)

@main.route('/admin_page', methods=['GET', 'POST'])
def admin_page():
    if request.method == 'GET':
     return render_template('admin_page.html', first_name='Ben', events=Event.query.all())


@main.route('/admin_page/<int:id>', methods=['POST'])
def delete_event_by_id(id):
    event = Event.query.get(id)
    if not event:
        flash("Event not found")
        return render_template('admin_page.html', events=Event.query.all(), first_name='Ben')
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted successfully")
    return render_template('admin_page.html', events=Event.query.all(), first_name='Ben')

@main.route('/pop_list')
def pop_list():
    date_a = datetime.now().date()
    date_b = (datetime.now() + timedelta(days=7)).date()
    event_count = Event.query.filter(Event.date >= date_a, Event.date <= date_b).count()
    return render_template('pop_list.html', event_count=event_count)

@main.route('/ramen_list')
def ramen_list():
    ramen_list = sorted(Event.query.filter(Event.event_type.ilike('ramen')).all(), key=lambda x: x.date)
    return render_template('ramen.html', ramen_list=ramen_list)

@main.route('/other_list')
def other_list():
    other_list = Event.query.filter(
        ~Event.event_type.ilike('ramen')
    ).order_by(Event.date).all()
    return render_template('other.html', other_list=other_list)


@main.route('/new_event', methods=['GET', 'POST'])
def event_form():
    host = db.Column(db.String(40), nullable=False)
    event_name = db.Column(db.String(40), nullable=False)
    event_type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    price_range = db.Column(db.String(30), nullable=False)
    contact = db.Column(db.String(25), nullable=False)
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
        if exists:
            flash("Event already registered")
            return redirect('/admin_page')
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
            return render_template('admin_page.html', my_events=Event.query.all(), first_name='Ben')
        else:
            flash(message)
            return render_template('new_event.html', form_data=request.form)
    return render_template('new_event.html')


@main.route('/delete_my_event_by_id/<int:id>', methods=['POST'])
def delete_my_event_by_id(id):
    event = Event.query.get(id)
    if not event:
        flash("Event not found")
        return render_template('admin_page.html', my_events=Event.query.all(), first_name='Ben')
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted successfully")
    return render_template('admin_page.html', my_events=Event.query.all(), first_name='Ben')
