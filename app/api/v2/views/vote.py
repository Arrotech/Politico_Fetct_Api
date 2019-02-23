from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.voters_model import VotersModel
from app.api.v2.models.users_model import UsersModel
from app.api.v2.models.offices_model import OfficesModel
from utils.validations import raise_error, \
    check_voters_keys2, on_success, is_valid_date, convert_to_int
import json
from flask_jwt_extended import jwt_required, get_jwt_identity
vote_v2= Blueprint('votes_v2', __name__)


class Vote:
    """A user can vote his/her candidate of choice."""

    @vote_v2.route('/vote', methods=['POST'])
    @jwt_required
    def post():
        """A user can vote his/her candidate of choice."""

        errors = check_voters_keys2(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        createdBy = details['createdBy']
        office = details['office']
        candidate = details['candidate']

        value = convert_to_int(createdBy)
        value2 = convert_to_int(office)
        value3 = convert_to_int(candidate)
        if type(value) is not int:
            return raise_error(400, "only positive integer is accepted")
        if type(value2) is not int:
            return raise_error(400, "only positive integer is accepted")
        if type(value3) is not int:
            return raise_error(400, "only positive integer is accepted")
        if UsersModel().get_user_by_id(createdBy):
            if OfficesModel().get_office_by_id(office):
                vote = VotersModel().save(createdBy, office, candidate)
                if "error" in vote:
                    return raise_error(400, "Please check your input and try again!")
                return make_response(jsonify({
                    "status": "201",
                    "message": "voted successfully",
                    "vote": vote
                    }))
            return raise_error(400, "office does not exist")
        return raise_error(400, "user does not exist")

    @vote_v2.route('/vote/results', methods=['GET'])
    @jwt_required
    def get_results():
        """Fetch results."""
        
        results = VotersModel().get_candidate()
        results = json.loads(results)
        if results:
            return make_response(jsonify({
                "status": "200",
                "message": "success",
                "office": results
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "no results found"
            }), 404)
