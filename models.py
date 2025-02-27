from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Time, Boolean
from db import db
class Event(db.Model):
    __bind_key__ = 'event_db'
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(40), nullable=False)
    host_name = db.Column(db.String(40), nullable=True)
    host_insta = db.Column(db.String(30), nullable=True)
    chef1_name = db.Column(db.String(40), nullable=False)
    chef2_name = db.Column(db.String(40), nullable=True)
    chef1_insta = db.Column(db.String(30), nullable=False)
    chef2_insta = db.Column(db.String(30), nullable=True)
    type = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    s_date = db.Column(db.Date, nullable=False)
    e_date = db.Column(db.Date, nullable=False)
    res_link = db.Column(db.String(100), nullable=True)
    def __repr__(self):
        return ""
