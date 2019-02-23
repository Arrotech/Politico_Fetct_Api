import unittest
import json
from app.api.v2.views.party_views import Party
from app.api.v2.models.parties_model import PartiesModel
from utils.dummy import edit_party, party_logoUrl_value, party_hqAddress_exists, party_logoUrl_exists,  party_hqAddress_value, get_party2, party_name_exists, create_party3, create_party2, create_account, user_login, party_name_keys, party_name_value
from .base_test import BaseTest


class TestOffice(BaseTest):
	"""Test office endpoint."""

	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(create_account),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header

	def test_create_party(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'party created successfully!')
		assert response.status_code == 201

	def test_party_logoUrl_value(self):
		"""Test party json keys"""

		response1 = self.client.post(
			'/api/v2/parties', data=json.dumps(party_logoUrl_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'logoUrl is in the wrong format!')
		assert response1.status_code == 400

	def test_party_name_exists(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response = self.client.post(
			'/api/v2/parties', data=json.dumps(party_name_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Party with that name already exists!')
		assert response.status_code == 400

	def test_party_hqAddress_exists(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response = self.client.post(
			'/api/v2/parties', data=json.dumps(party_hqAddress_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Party with that hqAddress already exists!')
		assert response.status_code == 400

	def test_party_logoUrl_exists(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response = self.client.post(
			'/api/v2/parties', data=json.dumps(party_logoUrl_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Party with that logoUrl already exists!')
		assert response.status_code == 400

	def test_unexisting_officeUrl(self):
		"""Test when unexisting url is provided."""

		response = self.client.get(
			'/api/v2/party')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_get_parties(self):
		"""Test fetching all offices that have been created."""
    
		response = self.client.get(
			'/api/v2/parties', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_party(self):
		"""Test getting a specific party by id."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response1 = self.client.get(
			'/api/v2/parties/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response1.status_code == 200


	def test_delete_party(self):
		"""Test getting a specific party by id."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response1 = self.client.delete(
			'/api/v2/parties/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'party deleted')
		assert response1.status_code == 200

	def test_get_unexisting_party(self):
		"""Test getting a specific party by id."""

		response1 = self.client.get(
			'/api/v2/parties/100', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'party not found')
		assert response1.status_code == 404

	def test_party_keys(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(party_name_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid name key')
		assert response.status_code == 400

	def test_edit_party_name_value(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parties/1', data=json.dumps(party_name_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'name of the party should only contain letters!')
		assert response1.status_code == 400

	def test_edit_party_hqAddress_value(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parties/1', data=json.dumps(party_hqAddress_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'hqAddress of the party should only contain letters!')
		assert response1.status_code == 400

	def test_edit_party_logoUrl_value(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parties/1', data=json.dumps(party_logoUrl_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'logoUrl is in the wrong format!')
		assert response1.status_code == 400

	def test_edit_party(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(create_party2), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/parties/1', data=json.dumps(edit_party), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'party updated successfully')
		assert response1.status_code == 200

	def test_edit_party_keys(self):
		"""Test party json keys"""

		response = self.client.put(
			'/api/v2/parties/1', data=json.dumps(party_name_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid name key')
		assert response.status_code == 400

	def test_party_nameValue(self):
		"""Test name json values."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(party_name_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'name should only contain letters!')
		assert response.status_code == 400

	def test_party_hqAddressValue(self):
		"""Test name json values."""

		response = self.client.post(
			'/api/v2/parties', data=json.dumps(party_hqAddress_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'hqAddress should only contain letters!')
		assert response.status_code == 400


