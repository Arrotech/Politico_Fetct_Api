import unittest
import json
from app.api.v1.views.party_views import Party
from app.api.v1.models.parties_model import PartiesModel
from utils.dummy import create_party, get_party, party, party_keys, party_name, party_hqAddress, party_logoUrl, update_party
from .base_test import BaseTest


class TestParty(BaseTest):
	"""Test party endpoints."""

	def test_create_party(self):
		"""Test when a user creates a new party."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'party created successfully!')
		assert response.status_code == 201

	def test_get_parties(self):
		"""Test when a user gets all parties."""

		response1 = self.client.post(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		response = self.client.get(
			'/api/v1/parties', data=json.dumps(party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_unexisting_parties(self):
		"""Test when a user gets all parties."""

		response = self.client.get(
			'/api/v1/parties', content_type='application/json')
		result = json.loads(response.data.decode('utf-8'))
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_delete_party(self):
		"""Test delete party."""

		response1 = self.client.post(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		result1 = json.loads(response1.data.decode())
		response = self.client.delete(
			'/api/v1/parties/1/delete',
			headers={"content_type":'application/json'}
			)
		result2 = json.loads(response.data.decode('utf-8'))
		self.assertEqual(result2['message'],'party deleted')
		self.assertEqual(response.status_code, 200)


	def test_delete_unexisting_party(self):
		"""Test delete party."""

		response = self.client.delete(
			'/api/v1/parties/100/delete',
			headers={"content_type":'application/json'}
			)
		result = json.loads(response.data.decode('utf-8'))
		self.assertEqual(result['status'],'not found')
		self.assertEqual(response.status_code, 404)

	def test_unexisting_partyUrl(self):
		"""Test when a user provides unexisting url."""

		response = self.client.get(
			'/api/v1/party')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_get_party(self):
		"""Test when a user wants to fetch a specific party."""

		response1 = self.client.post(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		response = self.client.get(
			'/api/v1/parties/1', data=json.dumps(get_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result["message"],
			"success")
		assert response.status_code == 200

	def test_unexisting_party(self):
		"""Test when a user wants to fetch unexisting party."""

		response = self.client.get(
			'/api/v1/parties/5')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_party_keys(self):
		"""Test party json keys."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid name key')
		assert response.status_code == 400

	def test_party_nameValue(self):
		"""Test name input json value."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_name), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_party_hqAddressValue(self):
		"""Test party hqAddress input json values."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_hqAddress), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_party_logoUrlValue(self):
		"""Test party logoUrl input json values."""

		response = self.client.post(
			'/api/v1/parties', data=json.dumps(party_logoUrl), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'logoUrl is in the wrong format')
		assert response.status_code == 400

	def test_update_party(self):
		"""Test updating an already existing party."""

		response1 = self.client.post(
			'/api/v1/parties', data=json.dumps(create_party), content_type='application/json')
		response = self.client.patch(
			'/api/v1/parties/1/edit', data=json.dumps(create_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'party updated successfully')
		assert response.status_code == 200

	def test_update_unexisting_office(self):
		"""Test updating an already existing party."""

		response = self.client.patch(
			'/api/v1/parties/100/edit', data=json.dumps(create_party), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['status'], 'not found')
		assert response.status_code == 404