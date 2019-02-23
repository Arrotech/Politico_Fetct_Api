from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.candidates_model import CandidatesModel, candidates
from utils.validations import raise_error, check_candidates_keys, on_success
import json
candidate = Blueprint('candidates', __name__)


class Candidates:
    """Candidates enpoint to show interest in running for an office."""

    @candidate.route('/candidates', methods=['POST'])
    def post():
        """A candidate can show interest to run for a seat."""

        errors = check_candidates_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        office = details['office']
        party = details['party']
        candidate = details['candidate']

        if details['office'].isalpha() is False \
                or details['party'].isalpha() is False \
                or details['candidate'].isalpha() is False:
            return raise_error(400, "input is in wrong format")
        candidate = CandidatesModel().save(office, party, candidate)
        return on_success(201, "interest created successfully")
