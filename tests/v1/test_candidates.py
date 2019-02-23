import unittest
import json
from app.api.v1.views.user_views import Register
from app.api.v1.views.candidates_views import Candidates
from app.api.v1.models.candidates_model import CandidatesModel
from utils.dummy import account_keys, new_candidate, candidate_keys, candidate_office_value, candidate_party_value, candidate_name_value
from .base_test import BaseTest


class TestCandidates(BaseTest):
	"""Test candidates endpoint."""

	def test_show_interest(self):
		"""Test when a candidate shows interest in running for office."""

		response = self.client.post(
			'/api/v1/candidates', data=json.dumps(new_candidate), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'interest created successfully')
		assert response.status_code == 201

	def test_office_value(self):
		"""Test the format of the office's name json value."""

		response = self.client.post(
			'/api/v1/candidates', data=json.dumps(candidate_office_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_party_value(self):
		"""Test the format of the party's name json value."""

		response = self.client.post(
			'/api/v1/candidates', data=json.dumps(candidate_party_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_candidate_value(self):
		"""Test the format of the candidate's name json value."""

		response = self.client.post(
			'/api/v1/candidates', data=json.dumps(candidate_name_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_candidates_keys(self):
		"""Test candidates json keys."""

		response = self.client.post(
			'/api/v1/candidates', data=json.dumps(candidate_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid party key')
		assert response.status_code == 400