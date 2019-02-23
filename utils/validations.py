import re
from flask import jsonify, make_response
from flask_jwt_extended import get_jwt_identity
from functools import wraps
import json
from app.api.v2.models.offices_model import OfficesModel
from app.api.v2.models.petitions_model import PetitionsModel
from app.api.v2.models.users_model import UsersModel
from app.api.v2.models.voters_model import VotersModel


def admin_required(func):
    """ Admin Rights."""
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        users = UsersModel().get_users()
        try:
            cur_user = [
                user for user in users if user['email'] == get_jwt_identity()]
            user_role = cur_user[0]['role']
            if user_role != 'admin':
                return {
                    'message': 'This activity can be completed by Admin only'}, 403 # Forbidden
            return func(*args, **kwargs)
        except Exception as e:
            return {"message": e}
    return wrapper_function

def convert_to_int(id):

    try:
        value = int(id)
        if value > 0:
            return value
        return raise_error(400, "cannot be a negative number")
    except Exception as e:
        return {"message": e}

def check_party_keys(request):
    """Check if the key values are correct."""

    res_keys = ['name', 'hqAddress', 'logoUrl']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def edit_party_name_keys(request):
    """Check if the key values are correct."""

    res_keys = ['name']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def edit_party_hqAddress_keys(request):
    """Check if the key values are correct."""

    res_keys = ['hqAddress']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def edit_party_logoUrl_keys(request):
    """Check if the key values are correct."""

    res_keys = ['logoUrl']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_role_key(request):
    """Check if the key value is correct."""

    res_keys = ['role']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors


def check_petitions_keys(request):
    """Check if the key values are correct."""

    res_keys = ['createdOn', 'createdBy', 'office', 'body']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_petitions_keys2(request):
    """Check if the key values are correct."""
    
    res_keys = ['createdBy', 'office', 'body']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_voters_keys(request):
    """Check if the key values are correct."""

    res_keys = ['createdOn', 'createdBy', 'office', 'candidate']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_voters_keys2(request):
    """Check if the key values are correct."""

    res_keys = ['createdBy', 'office', 'candidate']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_candidates_keys(request):
    """Check if the key values are correct."""

    res_keys = ['office', 'party', 'candidate']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_candidates_keys2(request):
    """Check if the key values are correct."""

    res_keys = ['office', 'user']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_register_keys(request):
    """Check if the key values are correct."""

    res_keys = ['firstname', 'lastname', 'email', 'password', 'phoneNumber', 'passportUrl', 'role']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_office_keys(request):
    """Check if the key values are correct."""

    res_keys = ['category', 'name']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def raise_error(status, msg):
    """Handles error messages."""
  
    return make_response(jsonify({
            "status": "400",
            "message": msg
        }), status)

def on_success(status, msg):
    """Handles error messages."""
  
    return make_response(jsonify({
            "message": msg
        }), status)

def is_valid_email(variable):
   """Check if email is a valid mail."""

   if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",
               variable):
       return True
   return False

def is_valid_url(variable):
   """Check if email is a valid mail."""

   if re.match(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)",
               variable):
       return True
   return False

def is_valid_date(variable):
   """Check if email is a valid mail."""
   
   if re.match(r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$",
               variable):
       return True
   return False

def is_valid_phone(variable):
   """Check if email is a valid mail."""
   
   if re.match(r"^(?:254|\+254|0)?(7(?:(?:[12][0-9])|(?:0[0-8])|(9[0-2]))[0-9]{6})$",
               variable):
       return True
   return False

def office_restrictions(data):
  """Restrict user inputs in a list."""

  office = ["state", "local", "federal", "legislative"]
  if data not in office:
    return False
  return True

def role_restrictions(data):
  """Restrict user inputs in a list."""

  user_role = ["user"]
  if data not in user_role:
    return False
  return True
  
def admin_restrictions(data):
  """Restrict user inputs in a list."""

  admin_role = ["admin"]
  if data not in admin_role:
    return False
  return True

def check_password(password):
  """Check passwrod."""

  
