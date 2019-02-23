from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v2.models.candidates_model import CandidatesModel
from app.api.v2.models.users_model import UsersModel
from app.api.v2.models.offices_model import OfficesModel
from utils.validations import raise_error, check_candidates_keys, on_success, convert_to_int
from utils.authorization import admin_required
import json
from flask_jwt_extended import jwt_required, get_jwt_identity

candidate_v2 = Blueprint('candidates_v2', __name__)


class Candidates:
    """Candidates enpoint to show interest in running for an office."""

    @candidate_v2.route('/candidates/register', methods=['POST'])
    @jwt_required
    @admin_required
    def post():
        """A candidate can show interest to run for a seat."""

        errors = check_candidates_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        office = details['office']
        candidate = details['candidate']
        party = details['party']

        value = convert_to_int(office)
        value2 = convert_to_int(candidate)
        value3 = convert_to_int(party)
        if type(value) is not int:
            return raise_error(400, "only positive integer is accepted")
        if type(value2) is not int:
            return raise_error(400, "only positive integer is accepted")
        if type(value3) is not int:
            return raise_error(400, "only positive integer is accepted")
        if OfficesModel().get_office_by_id(office): 
            if UsersModel().get_user_by_id(candidate):
                candidate = CandidatesModel().save(office, candidate, party)
                if "error" in candidate:
                    return raise_error(400, "Please check your input and try again!")
                return make_response(jsonify({
                    "status": "201",
                    "message": "user promoted successfully",
                    "candidate": candidate
                    }))
            return raise_error(400, "user does not exist")
        return raise_error(400, "office does not exist")

    @candidate_v2.route('/candidates', methods=['GET'])
    @jwt_required
    def get_all_candidates():
        '''Fetch all the existing candidates.'''

        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "users": json.loads(CandidatesModel().get_candidates())
            }), 200)

    @candidate_v2.route('/candidates/<int:candidate_id>', methods=['GET'])
    @jwt_required
    def get_candidate(candidate_id):
        """Fetch a specific candidate."""

        candidate = CandidatesModel().get_candidate_by_id(candidate_id)
        candidate = json.loads(candidate)
        if candidate:
            return make_response(jsonify({
                "status": "200",
                "message": "success",
                "candidate": candidate
                }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "candidate not found"
            }), 404)
