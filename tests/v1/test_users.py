import unittest
import json
from app.api.v1.views.user_views import Register
from app.api.v1.views.candidates_views import Candidates
from app.api.v1.models.candidates_model import CandidatesModel
from utils.dummy import create_account, account_keys, email_value, passport_value, phone_value, firstname_value, lastname_value, othername_value, role_value
from .base_test import BaseTest

class TestUsersAccount(BaseTest):
	"""Testing the users account endpoint."""

	def test_create_account(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(create_account), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Account created successfully')
		assert response.status_code == 201

	def test_account_keys(self):
		"""Test account json keys."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(account_keys), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid firstname key')
		assert response.status_code == 400

	def test_account_emailValue(self):
		"""Test the account email format."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(email_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Email is in the wrong format')
		assert response.status_code == 400

	def test_firstname_value(self):
		"""Test the account firstname format."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(firstname_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_lastname_value(self):
		"""Test the account lastname format."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(lastname_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_othername_value(self):
		"""Test the account othername format."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(othername_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_role_value(self):
		"""Test the account role format."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(role_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'input is in wrong format')
		assert response.status_code == 400

	def test_account_phoneValue(self):
		"""Test the account phone number format."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(phone_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'phone number is in the wrong format')
		assert response.status_code == 400

	def test_account_passportValue(self):
		"""Test the account passport url format."""

		response = self.client.post(
			'/api/v1/users', data=json.dumps(passport_value), content_type='application/json')
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'passportUrl is in the wrong format')
		assert response.status_code == 400