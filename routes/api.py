from flask import Blueprint, jsonify, render_template
from models import Event

api = Blueprint('api', __name__)

@api.route('/events')   
def get_events():
    events = Event.query.order_by(Event.date.desc(), Event.time.desc()).all()
    return jsonify([{
        "id": event.id,
        "host": event.host,
        "event_name": event.event_name,
        "event_type": event.event_type,
        "description": event.description,
        "address": event.address,
        "date": event.date.isoformat(),
        "time": event.time.isoformat(),
        "price_range": event.price_range,
        "contact": event.contact
    } for event in events])

