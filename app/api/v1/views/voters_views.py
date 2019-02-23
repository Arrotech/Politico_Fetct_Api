from flask import make_response, jsonify, request, abort, Blueprint
from app.api.v1.models.voters_model import VotersModel, voters
from utils.validations import raise_error, \
    check_voters_keys, on_success, is_valid_date
import json
vote = Blueprint('votes', __name__)


class Vote:
    """A user can vote his/her candidate of choice."""

    @vote.route('/voters', methods=['POST'])
    def post():
        """A user can vote his/her candidate of choice."""

        errors = check_voters_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))
        details = request.get_json()
        createdOn = details['createdOn']
        createdBy = details['createdBy']
        office = details['office']
        candidate = details['candidate']

        if not is_valid_date(createdOn):
            return raise_error(400, "createdOn is in the wrong format")
        if details['office'].isalpha() is False \
                or details['candidate'].isalpha() is False \
                or details['createdBy'].isalpha() is False:
            return raise_error(400, "input is in wrong format")

        voter = VotersModel().save(createdOn, createdBy, office, candidate)
        return on_success(201, "voted successfully")
