from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.petitions_model import PetitionsModel
from utils.validations import raise_error, \
    check_petitions_keys2, on_success, is_valid_date
import json
from flask_jwt_extended import jwt_required, get_jwt_identity

petition_v2 = Blueprint('petitions_v2', __name__)


class Petition:
    """A user can file petition."""

    @petition_v2.route('/petitions', methods=['POST'])
    @jwt_required
    def post():
        """A user can file a petition."""

        errors = check_petitions_keys2(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        createdBy = details['createdBy']
        office = details['office']
        body = details['body']

        if details['office'].isalpha() is False \
                or details['createdBy'].isalpha() is False:
            return raise_error(400, "input is in wrong format")
        petition = PetitionsModel().save(createdBy, office, body)
        return make_response(jsonify({
            "status": "201",
            "message": "petition filed successfully",
            "petition": petition
            }), 201)
