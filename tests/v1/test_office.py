import unittest
import json
from app.api.v1.views.office_views import Office
from app.api.v1.models.offices_model import OfficesModel
from utils.dummy import create_office, office_keys, get_office, office_category, office_name, offices, delete_office, category_restrictions
from .base_test import BaseTest


class TestOffice(BaseTest):
	"""Test office endpoint."""

	def test_create_office(self):
		"""Test create a new office."""

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(create_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'office created successfully!')
		assert response.status_code == 201

	def test_name_exists(self):
		"""Test create a new office."""

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(create_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'office with that name already exists!')
		assert response.status_code == 400

	def test_update_office(self):
		"""Test updating an already existing office."""

		response1 = self.client.post(
			'/api/v1/offices', data=json.dumps(create_office), content_type='application/json')
		response = self.client.patch(
			'/api/v1/offices/1/edit', data=json.dumps(create_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'office updated successfully')
		assert response.status_code == 200

	def test_update_unexisting_office(self):
		"""Test updating an already existing office."""

		response = self.client.patch(
			'/api/v1/offices/100/edit', data=json.dumps(create_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['status'], 'not found')
		assert response.status_code == 404

	def test_unexisting_officeUrl(self):
		"""Test when unexisting url is provided."""

		response = self.client.get(
			'/api/v1/office')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_keys(self):
		"""Test office json keys"""

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(office_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid category key')
		assert response.status_code == 400

	def test_get_offices(self):
		"""Test fetching all offices that have been created."""

		
		response1 = self.client.post(
			'/api/v1/offices', data=json.dumps(create_office), content_type='application/json')
		response = self.client.get(
			'/api/v1/offices', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_unexisting_offices(self):
		"""Test fetching all offices that have been created."""

		response = self.client.get(
			'/api/v1/offices', content_type='application/json')
		result = json.loads(response.data.decode('utf-8'))
		self.assertEqual(result['message'],
			"success")
		assert response.status_code == 200

	def test_get_office(self):
		"""Test getting a specific office by id."""

		response1 = self.client.post(
			'/api/v1/offices', data=json.dumps(create_office), content_type='application/json')
		response = self.client.get(
			'/api/v1/offices/1', data=json.dumps(get_office), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response.status_code == 200

	def test_unexisting_office(self):
		"""Test fetching unexisting office."""

		response = self.client.get(
			'/api/v1/offices/5')
		result = json.loads(response.data.decode())
		assert response.status_code == 404
		assert result['status'] == "not found"

	def test_office_categoryValue(self):
		"""Test category name json values."""

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(office_category), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_delete_office(self):
		"""Test delete office."""

		response1 = self.client.post(
			'/api/v1/offices', data=json.dumps(create_office), content_type='application/json')
		result1 = json.loads(response1.data.decode())
		response = self.client.delete(
			'/api/v1/offices/1/delete',
			headers={"content_type":'application/json'}
			)
		result2 = json.loads(response.data.decode('utf-8'))
		self.assertEqual(result2['message'],'office deleted')
		self.assertEqual(response.status_code, 200)


	def test_delete_unexisting_office(self):
		"""Test delete office."""

		response = self.client.delete(
			'/api/v1/offices/100/delete',
			headers={"content_type":'application/json'}
			)
		result = json.loads(response.data.decode('utf-8'))
		self.assertEqual(result['status'],'not found')
		self.assertEqual(response.status_code, 404)

	def test_office_nameValue(self):
		"""Test name json values."""

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(office_name), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_office_category_input(self):
		"""Test name json values."""

		response = self.client.post(
			'/api/v1/offices', data=json.dumps(category_restrictions), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'select from state, local, federal or legislative')
		assert response.status_code == 400



