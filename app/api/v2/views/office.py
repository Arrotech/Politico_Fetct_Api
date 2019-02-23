from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.offices_model import OfficesModel
from utils.validations import raise_error, check_office_keys, on_success, office_restrictions
from utils.authorization import admin_required
import json
from flask_jwt_extended import jwt_required, get_jwt_identity

office_v2 = Blueprint('office_v2', __name__)


class Office:
    """Creates a new government office."""

    @office_v2.route('/offices', methods=['POST'])
    @jwt_required
    @admin_required
    def post():
        """Create a new government office."""

        errors = check_office_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        category = details['category']
        name = details['name']

        if details['name'].isalpha() is False:
            return raise_error(400, "The name of the office is in wrong format!")
        if(office_restrictions(category) is False):
            return raise_error(400, "select from state, local, federal or legislative")
        if OfficesModel().get_name(name):
            return raise_error(400, "office with that name already exists!")

        res = OfficesModel().save(category, name)
        return jsonify({
            "status": "201",
            "message": "office created successfully!",
            "office": res
            }), 201

    @office_v2.route('/offices', methods=['GET'])
    @jwt_required
    def get_offices():
        '''Fetch all the existing offices.'''

        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "offices": json.loads(OfficesModel().get_offices())
            }), 200)

    @office_v2.route('/offices/<int:office_id>', methods=['GET'])
    @jwt_required
    def get_office(office_id):
        """Fetch a specific political office."""

        office = OfficesModel().get_office_by_id(office_id)
        office = json.loads(office)
        if office:
            return make_response(jsonify({
                "status": "200",
                "message": "success",
                "office": office
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "office not found"
            }), 404)

    @office_v2.route('/offices/<int:office_id>', methods=['DELETE'])
    @jwt_required
    @admin_required
    def delete(office_id):
        """Delete a specific office."""

        office = OfficesModel().get_office_by_id(office_id)
        if office:
            OfficesModel().delete(office_id)
            return make_response(jsonify({
                "status": "200",
                "message": "office deleted"
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "office not found"
            }), 404)

    @office_v2.route('/offices/<int:office_id>', methods=['PUT'])
    @jwt_required
    @admin_required
    def put(office_id):
        """Edit office details"""

        errors = check_office_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        category = details['category']
        name = details['name']

        if details['category'].isalpha() is False:
            return raise_error(400, "The category of the office is in wrong format!")
        if details['name'].isalpha() is False:
            return raise_error(400, "The name of the office is in wrong format!")

        office = OfficesModel().edit_office(category, name, office_id)
        if office:
            return make_response(jsonify({
                "status": "200",
                "message": "office updated successfully",
                "new_office": office
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "office not found"
            }), 404)
