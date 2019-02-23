from app.api.v2.models.db_conn import Database
import json
import psycopg2



class VotersModel(Database):
	"""Initialization."""

	def __init__(self,createdBy=None,
		office=None,
		candidate=None):

		super().__init__()
		self.createdBy = createdBy
		self.office = office
		self.candidate = candidate

	def save(self, createdBy, office, candidate):
		"""Save information of the new voter"""

		try:
			self.curr.execute(
	            ''' INSERT INTO voters(createdBy, office, candidate)\
	             VALUES('{}','{}','{}')\
	             RETURNING createdBy, office, candidate'''\
	            .format(createdBy, office, candidate))
			vote = self.curr.fetchone()
			self.conn.commit()
			self.curr.close()
			return vote

			query = """
					SELECT offices.name, candidates.candidate_id, users.email FROM voters\
					INNER JOIN offices ON voters.office=offices.office_id\
					INNER JOIN users ON voters.createdBy=users.user_id\
					INNER JOIN candidates ON voters.candidate=candidates.candidate_id;

					"""
			vote = self.curr.fetchall()

			self.curr.execute(query)
			self.conn.commit()
			self.curr.close()

			return json.dumps(vote, default=str)
		except psycopg2.IntegrityError:
			return "error"

	def get_candidate(self):
		"""Get user with specific email."""

		self.curr.execute(''' SELECT candidate, COUNT(*) from voters GROUP BY candidate''')
		candidate = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(candidate, default=str)