from app.api.v2.models.db_conn import Database
from werkzeug.security import generate_password_hash
import json
from flask import jsonify


class UsersModel(Database):
	"""Initialization."""

	def __init__(self,firstname=None,
		lastname=None,
		email=None,
		password=None,
		phoneNumber=None,
		passportUrl=None,
		role=None):

		super().__init__()
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		if password:
			self.password = generate_password_hash(password)
		self.phoneNumber = phoneNumber
		self.passportUrl = passportUrl
		self.role = role

	def save(self,firstname,lastname,email,password,phoneNumber,passportUrl,role):
		"""Save information of the new user"""

		self.curr.execute(
            ''' INSERT INTO users(firstname,lastname,email,password,phoneNumber,passportUrl,role)\
             VALUES('{}','{}','{}','{}','{}','{}','{}')\
             RETURNING firstname,lastname,email,password,phoneNumber,passportUrl,role'''\
            .format(firstname,lastname,email,password,phoneNumber,passportUrl,role))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user

	def get_user_by_id(self, user_id):
		"""Get user with specific email."""

		self.curr.execute(''' SELECT * FROM users WHERE user_id=%s''',(user_id, ))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(user, default=str)


	def get_users(self):
		"""Fetch all users"""

		query = "SELECT * from users"
		users = Database().fetch(query)
		return json.dumps(users, default=str)

	def get_email(self, email):
		"""Get user with specific email."""

		self.curr.execute(''' SELECT * FROM users WHERE email=%s''',(email, ))
		user = self.curr.fetchone()
		self.conn.commit()
		# self.curr.close()
		return user

	def get_phoneNumber(self, phoneNumber):
		"""Get user with specific email."""

		self.curr.execute(''' SELECT * FROM users WHERE phoneNumber=%s''',(phoneNumber, ))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user

	def get_passportUrl(self, passportUrl):
		"""Get user with specific email."""

		self.curr.execute(''' SELECT * FROM users WHERE passportUrl=%s''',(passportUrl, ))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user

	def edit_role(self, user_id, role):
		"""Admin can promote a user to be an admin."""

		self.curr.execute("""UPDATE users\
			SET role='{}'\
			WHERE user_id={} RETURNING role"""\
			.format(user_id,role))
		role = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return role