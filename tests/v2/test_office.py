import unittest
import json
from app.api.v2.views.office import Office
from app.api.v2.models.offices_model import OfficesModel
from utils.dummy import edit_office, category_name, office_name_keys, create_office2, office_keys, get_office, office_category, office_name, offices, delete_office, name_exists, category_restriction, create_account, user_login
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

	def test_create_office(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'office created successfully!')
		assert response.status_code == 201

	def test_name_exists(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		response1 = self.client.post(
			'/api/v2/offices', data=json.dumps(name_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'office with that name already exists!')
		assert response1.status_code == 400

	def test_wrong_category_value(self):
		"""Test create a new office."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(category_restriction), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'select from state, local, federal or legislative')
		assert response.status_code == 400

	def test_unexisting_officeUrl(self):
		"""Test when unexisting url is provided."""

		response = self.client.get(
			'/api/v2/office')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_keys(self):
		"""Test office json keys"""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid category key')
		assert response.status_code == 400

	def test_get_offices(self):
		"""Test fetching all offices that have been created."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		response1 = self.client.get(
			'/api/v2/offices', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response1.status_code == 200

	def test_unexisting_offices(self):
		"""Test fetching all offices that have been created."""

		response = self.client.get(
			'/api/v2/offices', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode('utf-8'))
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_office(self):
		"""Test getting a specific office by id."""

		response1 = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		response = self.client.get(
			'/api/v2/offices/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response.status_code == 200

	def test_unexisting_office(self):
		"""Test fetching unexisting office."""

		response = self.client.get(
			'/api/v2/offices/500', content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['message'] == "office not found"

	def test_office_nameValue(self):
		"""Test name json values."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(office_name), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'The name of the office is in wrong format!')
		assert response.status_code == 400

	def test_edit_office_name(self):
		"""Test name json values."""

		response1 = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		response = self.client.put(
			'/api/v2/offices/1', data=json.dumps(office_name), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'The name of the office is in wrong format!')
		assert response.status_code == 400

	def test_edit_office_category(self):
		"""Test name json values."""

		response1 = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		response = self.client.put(
			'/api/v2/offices/1', data=json.dumps(category_name), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'The category of the office is in wrong format!')
		assert response.status_code == 400

	def test_delete_office(self):
		"""Test getting a specific party by id."""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		response1 = self.client.delete(
			'/api/v2/offices/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'office deleted')
		assert response1.status_code == 200

	def test_edit_office_keys(self):
		"""Test party json keys"""

		response = self.client.put(
			'/api/v2/offices/1', data=json.dumps(office_name_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid name key')
		assert response.status_code == 400

	def test_edit_party(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/offices/1', data=json.dumps(edit_office), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'office updated successfully')
		assert response1.status_code == 200


