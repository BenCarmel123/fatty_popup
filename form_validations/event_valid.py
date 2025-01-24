from flask import Flask, render_template, request
from datetime import datetime, timedelta

def valid_instagram(instagram):
    errors = []
    if instagram[0] != "@":
        errors.append("Instagram must start with '@'")
    if len(instagram) < 2 or len(instagram) > 30:
        errors.append("Instagram must be between 2 and 30 characters")
    return errors

def valid_phone(phone):
    errors = []
    if phone[:2]!="05":
        errors.append("Phone number must start with 05")
    l = len(phone)
    if l!=10:
        if l == 13 and phone[3:5] != " - " or l == 11 and phone[3] != "-":
            errors.append("Phone number must have 10 digits")
        elif l>13 or l<10:
            errors.append("Phone number must have 10 digits")
    return errors

def valid_email(email):
    errors = []
    if "@" not in email or "." not in email:
        errors.append("Email must contain '@' and '.'")
    if email.count("@") > 1 or email.count(".") > 1:
        errors.append("Email must contain only one '@' and '.'")
    return errors

def valid_contact(contact):
    if contact[0] == "@":
        if valid_instagram(contact):
            return True
    elif "@" in contact:
        if valid_email(contact):
            return True
    else:
        if valid_phone(contact):
            return True
    return False

def valid_word(word):
    errors = []
    if word[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        errors.append("Capital letter")
    for char in word[1:]:
        if char not in "abcdefghijklmnopqrstuvwxyz":
            errors.append("only letters")
    return errors

def validate_event(host, event_name, event_type, description, address, date, time, price_range, contact):
    res = ""
    if event_type == "select":
        res += "Event type" + "\n"
    if not description or len(description) > 100:
        res += "Description"+ "\n"
    if not address or len(address) > 100:
        res += "Address" + "\n"
    if not date or not (datetime.today().date() <= date <= (datetime.today().date() + timedelta(days=30))):
        res += "Date" + "\n"
    if not time:
        res += "Time" + "\n"
    if not price_range:
        res += "Price range" + "\n"
    if not contact or not valid_contact(contact):
        res += "Contact Details" + "\n"
    
    return res