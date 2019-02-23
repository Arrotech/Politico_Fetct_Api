from flask import make_response, jsonify, request, Blueprint
from app.api.v2.models.users_model import UsersModel
from utils.validations import check_role_key,\
    role_restrictions, admin_restrictions,\
    raise_error, check_register_keys,\
    is_valid_email, is_valid_url,\
    is_valid_phone, check_candidates_keys2, check_password
import json
from utils.authorization import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token
import re

auth = Blueprint('auth', __name__)


class Register:
    """A user can create a new account."""
    
    @auth.route('/auth/signup', methods=['POST'])
    def create_account():
        """Create new account."""

        errors = check_register_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        firstname = details['firstname']
        lastname = details['lastname']
        email = details['email']
        password = generate_password_hash(details['password'])
        phoneNumber = details['phoneNumber']
        passportUrl = details['passportUrl']
        role = details['role']

        if not is_valid_email(email):
            return raise_error(400, "Email is in the wrong format")
        if not is_valid_phone(phoneNumber):
            return raise_error(400, "phone number is in the wrong format")
        if details['firstname'].isalpha()== False:
            return raise_error(400, "firstname is in wrong format")
        if details['lastname'].isalpha()== False:
            return raise_error(400, "lastname is in wrong format")
        if details['role'].isalpha()== False:
            return raise_error(400, "role is in wrong format")
        if not is_valid_url(passportUrl):
            return raise_error(400, "passportUrl is in the wrong format")
        if details['password'] == "":
            return raise_error(400, "password required")
        if len(details['password']) < 8:
            return raise_error(400, "length of password should be atleast eight characters")
        if UsersModel().get_email(email):
            return raise_error(400, "Email already exists!")
        if UsersModel().get_phoneNumber(phoneNumber):
            return raise_error(400, "phoneNumber already exists!")
        if UsersModel().get_passportUrl(passportUrl):
            return raise_error(400, "passportUrl already in use!")

        user = UsersModel().save(firstname,
                lastname,
                email,
                password,
                phoneNumber,
                passportUrl,
                role)
        return make_response(jsonify({
            "status": "201",
            "message": "Account created successfully",
            "user": user
            }), 201)

    @auth.route('/auth/login', methods=['POST'])
    def user_login():
        """Sign In a user"""

        details = request.get_json()
        email = details['email']
        password = details['password']
        user = UsersModel().get_email(email)
        if user:
            password_db = user['password']
            if check_password_hash(password_db, password):
                token = create_access_token(identity=email)
                return make_response(jsonify({
                    "status": "200",
                    "message": f"successfully logged in {email}",
                    "token": token
                }), 200)
            return raise_error(401, "Invalid email or password")
        return raise_error(401, "Invalid email or password")

    @auth.route('/users', methods=['GET'])
    @jwt_required
    @admin_required
    def get_all_users():
        '''Fetch all the existing users.'''

        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "users": json.loads(UsersModel().get_users())
            }), 200)

    @auth.route('/users/<int:user_id>', methods=['GET'])
    @jwt_required
    @admin_required
    def get_user(user_id):
        """Fetch a specific user."""

        user = UsersModel().get_user_by_id(user_id)
        user = json.loads(user)
        if user:
            return make_response(jsonify({
                "status": "200",
                "message": "success",
                "user": user
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "user not found"
            }), 404)

    @auth.route('/users/<int:user_id>', methods=['PUT'])
    @jwt_required
    @admin_required
    def put(user_id):
        """Promote user to be an admin."""

        errors = check_role_key(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        role = details['role']

        if(admin_restrictions(role) is False):
            return raise_error(400, "please select admin as the role")

        user = UsersModel().edit_role(role, user_id)
        if user:
            return make_response(jsonify({
                "status": "200",
                "message": "user successfully promoted to be an admin",
                "new_role": user
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "user not found"
            }), 404)


