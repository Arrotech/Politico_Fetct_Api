from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.users_model import UsersModel, users
from utils.validations import raise_error, \
    check_register_keys, is_valid_email, \
    is_valid_url, on_success, is_valid_phone
import json
user = Blueprint('users', __name__)


class Register:
    """A user can create a new account."""

    @user.route('/users', methods=['POST'])
    def post():
        """Create new account."""

        errors = check_register_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        firstname = details['firstname']
        lastname = details['lastname']
        othername = details['othername']
        email = details['email']
        phoneNumber = details['phoneNumber']
        passportUrl = details['passportUrl']
        role = details['role']

        if not is_valid_email(email):
            return raise_error(400, "Email is in the wrong format")
        if not is_valid_phone(phoneNumber):
            return raise_error(400, "phone number is in the wrong format")
        if details['firstname'].isalpha() is False \
                or details['lastname'].isalpha() is False \
                or details['othername'].isalpha() is False \
                or details['role'].isalpha() is False:
            return raise_error(400, "input is in wrong format")
        if not is_valid_url(passportUrl):
            return raise_error(400, "passportUrl is in the wrong format")

        user = UsersModel().save(
            firstname,
            lastname,
            othername,
            email,
            phoneNumber,
            passportUrl,
            role)
        return on_success(201, "Account created successfully")
