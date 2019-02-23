import unittest
import json
from app.api.v2.views.auth_views import Register
from app.api.v2.models.users_model import UsersModel
from utils.dummy import role_value2, wrong_role_value, edit_account, password_length, empty_password, create_account, user_login2, account_keys, email_value, passport_value, new_account, phone_value, firstname_value, lastname_value, othername_value, role_value, user_login, unregistered_user,  email_exists, phone_exists, passport_exists
from .base_test import BaseTest

class TestUsersAccount(BaseTest):
	"""Testing the users account endpoint."""

	def get_token(self):

		self.client.post('/api/v2/auth/signup', data=json.dumps(create_account),
		content_type='application/json')
		resp = self.client.post('/api/v2/auth/login', data=json.dumps(user_login),
			content_type='application/json')
		access_token = json.loads(resp.get_data(as_text=True))['token']
		auth_header = {'Authorization': 'Bearer {}'.format(access_token)}
		return auth_header

	def test_create_account(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_account), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Account created successfully')
		assert response.status_code == 201

	def test_get_users(self):
		"""Test fetching all offices that have been created."""
    
		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_account), content_type='application/json', headers=self.get_token())
		response1 = self.client.get(
			'/api/v2/users', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			"success")
		assert response1.status_code == 200

	def test_get_user(self):
		"""Test getting a specific party by id."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_account), content_type='application/json', headers=self.get_token())
		response1 = self.client.get(
			'/api/v2/users/1', content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'],
			'success')
		assert response1.status_code == 200

	def test_empty_password(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(empty_password), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'password required')
		assert response.status_code == 400

	def test_password_length(self):
		"""Test the vote json keys."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(password_length), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'length of password should be atleast eight characters')
		assert response.status_code == 400

	def test_email_exists(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(email_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Email already exists!')
		assert response.status_code == 400

	def test_phoneNumber_exists(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(phone_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'phoneNumber already exists!')
		assert response.status_code == 400

	def test_login_wrong_password(self):
		"""Tesr that the password in the db is the same as the password the user enters/"""

		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(user_login2), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid email or password', msg='not allowed')
		assert response.status_code == 401

	def test_passportUrl_exists(self):
		"""Test create a new account."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(passport_exists), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'passportUrl already in use!')
		assert response.status_code == 400

	def test_signin_account(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'successfully logged in email@gmail.co.ke', msg='not allowed')
		assert response.status_code == 200

	def test_unexisting_url(self):
		response = self.client.post(
			'/api/v2/auth/lo8563gin', data=json.dumps(user_login), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['status'], 'not found', msg='not allowed')
		assert response.status_code == 404

	def test_unexisting_user(self):
		response = self.client.post(
			'/api/v2/auth/login', data=json.dumps(unregistered_user), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid email or password', msg='not allowed')
		assert response.status_code == 401

	def test_account_keys(self):
		"""Test account json keys."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(account_keys), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Invalid firstname key')
		assert response.status_code == 400

	def test_account_emailValue(self):
		"""Test the account email format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(email_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'Email is in the wrong format')
		assert response.status_code == 400

	def test_firstname_value(self):
		"""Test the account firstname format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(firstname_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'firstname is in wrong format')
		assert response.status_code == 400

	def test_lastname_value(self):
		"""Test the account lastname format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(lastname_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'lastname is in wrong format')
		assert response.status_code == 400

	def test_role_value(self):
		"""Test the account role format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(role_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'role is in wrong format')
		assert response.status_code == 400

	def test_account_phoneValue(self):
		"""Test the account phone number format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(phone_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'phone number is in the wrong format')
		assert response.status_code == 400

	def test_account_passportValue(self):
		"""Test the account passport url format."""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(passport_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response.data.decode())
		self.assertEqual(result['message'], 'passportUrl is in the wrong format')
		assert response.status_code == 400

	# def test_edit_office_name(self):
	# 	"""Test name json values."""

	# 	response1 = self.client.post(
	# 		'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
	# 	response = self.client.put(
	# 		'/api/v2/offices/1', data=json.dumps(office_name), content_type='application/json', headers=self.get_token())
	# 	result = json.loads(response.data.decode())
	# 	self.assertEqual(result['message'], 'The name of the office is in wrong format!')
	# 	assert response.status_code == 400

	# def test_edit_office_category(self):
	# 	"""Test name json values."""

	# 	response1 = self.client.post(
	# 		'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
	# 	response = self.client.put(
	# 		'/api/v2/offices/1', data=json.dumps(category_name), content_type='application/json', headers=self.get_token())
	# 	result = json.loads(response.data.decode())
	# 	self.assertEqual(result['message'], 'The category of the office is in wrong format!')
	# 	assert response.status_code == 400

	# def test_delete_office(self):
	# 	"""Test getting a specific party by id."""

	# 	response = self.client.post(
	# 		'/api/v2/offices', data=json.dumps(create_office2), content_type='application/json', headers=self.get_token())
	# 	response1 = self.client.delete(
	# 		'/api/v2/offices/1', content_type='application/json', headers=self.get_token())
	# 	result = json.loads(response1.data.decode())
	# 	self.assertEqual(result['message'],
	# 		'office deleted')
	# 	assert response1.status_code == 200

	# def test_edit_office_keys(self):
	# 	"""Test party json keys"""

	# 	response = self.client.put(
	# 		'/api/v2/offices/1', data=json.dumps(office_name_keys), content_type='application/json', headers=self.get_token())
	# 	result = json.loads(response.data.decode())
	# 	self.assertEqual(result['message'], 'Invalid name key')
	# 	assert response.status_code == 400

	def test_edit_account(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_account), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/users/1', data=json.dumps(edit_account), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'user successfully promoted to be an admin')
		assert response1.status_code == 200

	def test_edit_role_key(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_account), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/users/1', data=json.dumps(wrong_role_value), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'Invalid role key')
		assert response1.status_code == 400

	def test_edit_role(self):
		"""Test party json keys"""

		response = self.client.post(
			'/api/v2/auth/signup', data=json.dumps(new_account), content_type='application/json', headers=self.get_token())
		response1 = self.client.put(
			'/api/v2/users/1', data=json.dumps(role_value2), content_type='application/json', headers=self.get_token())
		result = json.loads(response1.data.decode())
		self.assertEqual(result['message'], 'please select admin as the role')
		assert response1.status_code == 400

