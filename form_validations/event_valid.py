from flask import Flask, render_template, request
from datetime import datetime, timedelta
import validators

def is_valid_url(url):
    return validators.url(url)

def valid_instagram(instagram):
   errors = []
   if instagram[0] != "@":
       errors.append("Instagram must start with '@'")
   if len(instagram) < 2 or len(instagram) > 30:
       errors.append("Instagram must be between 2 and 30 characters")
   return errors

def valid_word(word):
   errors = []
   if word[0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
       errors.append("Capital letter")
   for char in word[1:]:
       if char not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ":
           errors.append("only letters")
   return errors

def validate_event(event_name, host_name, host_insta, chef1_name, chef1_insta, chef2_name, chef2_insta, type, description, location, s_date, e_date, res_link):
   res = ""
   if not event_name or len(event_name) > 40:
       res += "Event name" + "\n"
   if host_name and len(host_name) > 40:
       res += "Host name" + "\n"
   if host_insta and len(host_insta) > 30:
       res += "Host Instagram" + "\n"
   if not chef1_name or (len(chef1_name) > 20 or len(valid_word(chef1_name))>0):
       res += "Chef 1 name" + "\n"
   if not chef1_insta or (len(chef1_insta) > 30 or len(valid_instagram(chef1_insta))>0):
       res += "Chef 1 Instagram" + "\n"
   if chef2_name and len(chef2_name) > 40:
       res += "Chef 2 name" + "\n"
   if chef2_insta and (len(chef2_insta) > 30 or len(valid_instagram(chef2_insta))>0):
       res += "Chef 2 Instagram" + "\n"
   if type == "select":
       res += "Event type" + "\n"
   if not description or len(description) > 500:
       res += "Description"+ "\n"
   if not location or len(location) > 100:
       res += "Location" + "\n"
   if not s_date or not (datetime.today().date() <= s_date <= (datetime.today().date() + timedelta(days=30))):
       res += "Date" + "\n"
   if e_date and e_date < s_date:
       res += "End date" + "\n"
   if res_link and not is_valid_url(res_link):
       res += "Link" + "\n"
   return res