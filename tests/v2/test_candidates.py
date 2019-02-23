import unittest
import json
from app.api.v2.views.auth_views import Register
from app.api.v2.views.candidates_views import Candidates
from app.api.v2.models.candidates_model import CandidatesModel
from utils.dummy import account_keys, new_candidate2, new_candidate3, candidate_keys, candidate_office_value2, candidate_party_value2, candidate_candidate_value2, create_account, user_login
from .base_test import BaseTest


class TestCandidates(BaseTest):
	"""Test candidates endpoint."""

	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(create_account),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header

	def test_create_wrong_candidate(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/candidates/register', data=json.dumps(new_candidate2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Please check your input and try again!')
		assert response.status_code == 400

	def test_get_candidates(self):
		"""Test fetching all offices that have been created."""

		response = self.client.post(
			'/api/v2/candidates/register', data=json.dumps(new_candidate3), content_type='application/json', headers=self.get_token())
		response1 = self.client.get(
			'/api/v2/candidates', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response1.status_code == 200

	def test_get_candidate(self):
		"""Test getting a specific office by id."""

		response1 = self.client.post(
			'/api/v2/candidates/register', data=json.dumps(new_candidate3), content_type='application/json', headers=self.get_token())
		response = self.client.get(
			'/api/v2/candidates/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			'candidate not found')
		assert response.status_code == 404

	def test_office_value(self):
		"""Test the format of the office's name json value."""

		response = self.client.post(
			'/api/v2/candidates/register', data=json.dumps(candidate_office_value2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'only positive integer is accepted')
		assert response.status_code == 400

	def test_party_value(self):
		"""Test the format of the party's name json value."""

		response = self.client.post(
			'/api/v2/candidates/register', data=json.dumps(candidate_party_value2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'only positive integer is accepted')
		assert response.status_code == 400

	def test_candidate_value(self):
		"""Test the format of the candidate's name json value."""

		response = self.client.post(
			'/api/v2/candidates/register', data=json.dumps(candidate_candidate_value2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'only positive integer is accepted')
		assert response.status_code == 400

	def test_candidates_keys(self):
		"""Test candidates json keys."""

		response = self.client.post(
			'/api/v2/candidates/register', data=json.dumps(candidate_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid party key')
		assert response.status_code == 400