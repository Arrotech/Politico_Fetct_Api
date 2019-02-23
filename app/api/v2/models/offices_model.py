from app.api.v2.models.db_conn import Database
import json
from flask_jwt_extended import jwt_required

Database().create_table()

class OfficesModel(Database):
	"""Initiallization."""

	def __init__(self, category=None, name=None):
		super().__init__()
		self.category = category
		self.name = name
		
	def save(self, category, name):
		"""Create a new offices."""

		print(category, name)
		self.curr.execute(
			''' INSERT INTO offices(category, name)\
			VALUES('{}','{}')\
			 RETURNING category, name'''\
			.format(category, name))
		office = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return office
		
	def get_offices(self):
		"""Fetch all offices"""

		query = "SELECT * FROM offices"
		offices = Database().fetch(query)
		return json.dumps(offices, default=str)

	def get_office_by_id(self, office_id):
		"""Fetch a single office"""

		self.curr.execute(""" SELECT * FROM offices WHERE office_id={}""".format(office_id ))
		office = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(office, default=str)

	def get_name(self, name):
		"""Get user with specific email."""

		self.curr.execute(''' SELECT * FROM offices WHERE name=%s''',(name, ))
		user = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return user

	def delete(self, office_id):
		''' Delete order '''
		
		self.curr.execute(''' DELETE FROM offices WHERE office_id=%s''',(office_id, ))
		self.conn.commit()
		self.curr.close()

	def edit_office(self, office_id, category, name):
		"""User can Change information of the office."""

		self.curr.execute("""UPDATE offices\
			SET category='{}', name='{}'\
			WHERE office_id={} RETURNING category, name"""\
			.format(office_id,category,name))
		office = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return office