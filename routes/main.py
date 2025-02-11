from flask import Blueprint, render_template, request, flash, redirect, current_app, session
from datetime import datetime , timedelta
from db import db
from models import Event
from form_validations.event_valid import validate_event
from werkzeug.security import check_password_hash

main = Blueprint('main', __name__)

def display_date(date1, date2):
    format_date1 = date1.strftime('%d.%m') 
    format_date2 = date2.strftime('%d.%m') 
    display_date = ''
    if format_date1==format_date2:
        return format_date1
    if format_date1[-2:] == format_date2[-2:]:
        display_date = format_date1[:2] + ' - ' + format_date2
    else:
        display_date = format_date1 + ' - ' + format_date2
    return display_date
                    
def display_location(host_name, location):
    return host_name if not location else location

@main.context_processor
def utility_processor():
    return {'display_date': display_date, 'display_location': display_location , 'first_name': 'Ben'}

def get_sorted_events(like=None):
    query = Event.query
    if like:
        query = query.filter(Event.type.ilike(like))
    return query.order_by(Event.s_date).all()

def event_counter(gap):
    date_a = datetime.now().date()
    date_b = (datetime.now() + timedelta(days=gap)).date()
    return Event.query.filter(Event.s_date >= date_a, Event.s_date <= date_b).count()

def constructor(id, event_name, host_name, host_insta, chef1_name, chef1_insta, 
                chef2_name, chef2_insta, type, description, location, s_date, e_date):
    if not id:
        new_event = Event(
                event_name=event_name,
                host_name=host_name,
                host_insta=host_insta,
                chef1_name=chef1_name,
                chef1_insta=chef1_insta,
                chef2_name=chef2_name,
                chef2_insta=chef2_insta,
                type=type,
                description=description,
                location=location,
                s_date=s_date,
                e_date=e_date,
            )
        return new_event
    else:
        event = Event.query.get(id)
        event.event_name=event_name
        event.host_name=host_name
        event.host_insta=host_insta
        event.chef1_name=chef1_name
        event.chef1_insta=chef1_insta
        event.chef2_name=chef2_name
        event.chef2_insta=chef2_insta
        event.type=type
        event.description=description
        event.location=location
        event.s_date=s_date
        event.e_date=e_date
        return event

@main.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@main.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'GET':
        return render_template('login.html', input_username='')
    else:
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        if (username == current_app.config['ADMIN_USERNAME'] and 
            check_password_hash(current_app.config['ADMIN_PASSWORD'], password)):
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
     return render_template('admin.html', events = get_sorted_events(None))

@main.route('/admin/delete/<int:id>', methods=['POST'])
def delete_event_by_id(id):
    event = Event.query.get(id)
    if not event:
        flash("Event not found")
        return render_template('admin.html', events = get_sorted_events(None))
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted successfully")
    return render_template('admin.html', events = get_sorted_events(None))

@main.route('/admin/edit/<int:id>', methods =['POST'])
def edit_event_by_id(id):
    event = Event.query.get(id)
    if not event:
        flash("Event not found")
        return render_template('admin.html', events = get_sorted_events(None))
    else:
        return render_template('event.html', form_data = event)

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
    if request.method == 'POST':
        editing_id = request.form.get('editing_id') 
        event_name = request.form.get('event_name', '')
        host_name = request.form.get('host_name', '') 
        host_insta = request.form.get('host_insta', '') 
        chef1_name = request.form.get('chef1_name', '')
        chef1_insta = request.form.get('chef1_insta', '')
        chef2_name = request.form.get('chef2_name', '') 
        chef2_insta = request.form.get('chef2_insta', '') 
        type = request.form.get('type', '')
        description = request.form.get('description', '')
        location = request.form.get('location', '')
        s_date = datetime.strptime(request.form.get('s_date', ''), "%Y-%m-%d").date()
        e_date = datetime.strptime(request.form.get('e_date',''), "%Y-%m-%d").date()
        if editing_id:
            event=constructor(editing_id, event_name, host_name, host_insta, chef1_name, chef1_insta, chef2_name, chef2_insta, type, description, location, s_date, e_date )
            db.session.commit()
            flash("Event updated successfully")
            return render_template('admin.html', events = get_sorted_events(None))
        else:
            exists = Event.query.filter(
                Event.event_name.ilike(event_name.strip()),
                Event.s_date == s_date,
                Event.chef1_name.ilike(chef1_name.strip()),
            ).first()
            if exists: 
                flash("Event already registered")
                return render_template('admin.html', events = get_sorted_events(None))
            message = validate_event(event_name, host_name, host_insta, chef1_name, chef1_insta, chef2_name, chef2_insta, type, description, location, s_date, e_date)
            if message == "":
                new_event = constructor(None,event_name, host_name, host_insta, chef1_name, chef1_insta, chef2_name, chef2_insta, type, description, location, s_date, e_date)
                db.session.add(new_event)
                db.session.commit()
                return render_template('admin.html', events = get_sorted_events(None))
            else:
                flash(message)
                return render_template('event.html', form_data=request.form)
    return render_template('event.html')



