from flask_jwt_extended import get_jwt_identity
from functools import wraps
import json
from flask import jsonify

from app.api.v2.models.offices_model import OfficesModel
from app.api.v2.models.users_model import UsersModel


def admin_required(func):
    """ Admin Rights."""
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        users = UsersModel().get_users()
        users = json.loads(users)
        try:
            cur_user = [
                user for user in users if user['email'] == get_jwt_identity()]
            user_role = cur_user[0]['role']
            if user_role != 'admin':
                return jsonify({
                    'message': 'This activity can be completed by Admin only'}), 403 # Forbidden
            return func(*args, **kwargs)
        except Exception as e:
            return jsonify({"message": str(e)}),500
    return wrapper_function