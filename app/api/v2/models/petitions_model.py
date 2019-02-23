from app.api.v2.models.db_conn import Database
import json


class PetitionsModel(Database):
	"""Initialization."""

	def __init__(self,createdBy=None,
		office=None,
		body=None):

		super().__init__()
		self.createdBy = createdBy
		self.office = office
		self.body = body

	def save(self, createdBy, office, body):
		"""Save information of a new petition"""

		self.curr.execute(
            ''' INSERT INTO petitions(createdBy, office, body)\
             VALUES('{}','{}','{}')\
             RETURNING createdBy, office, body'''\
            .format(createdBy, office, body))
		petition = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return petition