import json
from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.parties_model import PartiesModel, parties
from utils.validations import raise_error, \
    check_party_keys, is_valid_url, on_success
party = Blueprint('parties', __name__)


class Party:
    """Creates a new political party."""

    @party.route('/parties', methods=['POST'])
    def post():
        """Create a new political party."""

        errors = check_party_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        name = details['name']
        hqAddress = details['hqAddress']
        logoUrl = details['logoUrl']

        if PartiesModel().get_name(name) \
                or PartiesModel().get_hqAddress(hqAddress) \
                or PartiesModel().get_logoUrl(logoUrl):
            return raise_error(400, "Party already exists")
        if not is_valid_url(logoUrl):
            return raise_error(400, "logoUrl is in the wrong format")
        if details['name'].isalpha() is False \
                or details['hqAddress'].isalpha() is False:
            return raise_error(400, "input is in wrong format")
        res = PartiesModel().save(name, hqAddress, logoUrl)
        return jsonify({
            "message": "party created successfully!",
            "party_id": len(parties)
            }), 201

    @party.route('/parties', methods=['GET'])
    def get_parties():
        """Fetch all the existing parties."""

        return make_response(jsonify({
            "message": "success",
            "parties": PartiesModel().get_all_parties()
            }), 200)

    @party.route('/parties/<int:party_id>', methods=['GET'])
    def get_party(party_id):
        """Fetch a specific political party."""

        party = PartiesModel().get_a_party(party_id)
        if party:
            return make_response(jsonify({
                "message": "success",
                "party": party
                }), 200)
        return make_response(jsonify({
            "status": "not found"
            }), 404)

    @party.route('/parties/<int:party_id>/delete', methods=['DELETE'])
    def delete_party(party_id):
        """Delete a specific party."""

        party = PartiesModel().get_a_party(party_id)
        if party:
            parties.remove(party)
            return on_success(200, "party deleted")
        return make_response(jsonify({
            "status": "not found"
            }), 404)

    @party.route('/parties/<int:party_id>/edit', methods=['PATCH'])
    def edit_party(party_id):
        """Edit a specific party."""

        details = request.get_json()
        party = PartiesModel().update_party(party_id, details)
        if party:
            return on_success(200, "party updated successfully")
        return make_response(jsonify({
            "status": "not found"
            }), 404)
