import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.parties_model import PartiesModel
from utils.authorization import admin_required
from utils.validations import raise_error, \
    check_party_keys, is_valid_url, on_success, edit_party_name_keys, edit_party_hqAddress_keys, edit_party_logoUrl_keys
from flask_jwt_extended import jwt_required, get_jwt_identity
party_v2 = Blueprint('parties_v2', __name__)


class Party:
    """Creates a new political party."""

    @party_v2.route('/parties', methods=['POST'])
    @jwt_required
    @admin_required
    def post():
        """Create a new political party."""

        errors = check_party_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        name = details['name']
        hqAddress = details['hqAddress']
        logoUrl = details['logoUrl']

        if PartiesModel().get_name(name):
            return raise_error(400, "Party with that name already exists!")
        if PartiesModel().get_hqAddress(hqAddress):
            return raise_error(400, "Party with that hqAddress already exists!")
        if PartiesModel().get_logoUrl(logoUrl):
            return raise_error(400, "Party with that logoUrl already exists!")
        if not is_valid_url(logoUrl):
            return raise_error(400, "logoUrl is in the wrong format!")
        if details['name'].isalpha() is False:
            return raise_error(400, "name should only contain letters!")
        if details['hqAddress'].isalpha() is False:
            return raise_error(400, "hqAddress should only contain letters!")

        res = PartiesModel().save(name, hqAddress, logoUrl)
        return jsonify({
            "status": "201",
            "message": "party created successfully!",
            "party": res
        }), 201

    @party_v2.route('/parties', methods=['GET'])
    @jwt_required
    def get_parties():
        """Fetch all the existing parties."""

        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "parties": json.loads(PartiesModel().get_parties())
            }), 200)

    @party_v2.route('/parties/<int:party_id>', methods=['GET'])
    @jwt_required
    def get_party(party_id):
        """Fetch a specific political party."""

        party = PartiesModel().get_party(party_id)
        party = json.loads(party)
        if party:
            return make_response(jsonify({
                "status": "200",
                "message": "success",
                "party": party
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "party not found"
            }), 404)

    @party_v2.route('/parties/<int:party_id>', methods=['DELETE'])
    @jwt_required
    @admin_required
    def delete(party_id):
        """Delete a specific party."""

        party = PartiesModel().get_party(party_id)
        if party:
            PartiesModel().delete(party_id)
            return make_response(jsonify({
                "status": "200",
                "message": "party deleted"
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "party not found"
            }), 404)

    @party_v2.route('/parties/<int:party_id>', methods=['PUT'])
    @jwt_required
    @admin_required
    def put(party_id):
        """Edit party name"""

        errors = check_party_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        name = details['name']
        hqAddress = details['hqAddress']
        logoUrl = details['logoUrl']

        if details['name'].isalpha() is False:
            return raise_error(400, "name of the party should only contain letters!")
        if details['hqAddress'].isalpha() is False:
            return raise_error(400, "hqAddress of the party should only contain letters!")
        if not is_valid_url(logoUrl):
            return raise_error(400, "logoUrl is in the wrong format!")
        party = PartiesModel().edit_party(name, hqAddress, logoUrl, party_id)
        if party:
            return make_response(jsonify({
                "status": "200",
                "message": "party updated successfully",
                "new_party": party
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "party not found"
            }), 404)