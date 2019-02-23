from app.api.v2.models.db_conn import Database
from werkzeug.security import generate_password_hash
import json
from flask import jsonify


class PartiesModel(Database):
	"""Initialization."""

	def __init__(self,name=None,
		hqAddress=None,
		logoUrl=None):

		super().__init__()
		self.name = name
		self.hqAddress = hqAddress
		self.logoUrl = logoUrl

	def save(self, name, hqAddress, logoUrl):
		"""Save information of the new party"""

		self.curr.execute(
            ''' INSERT INTO parties(name, hqAddress, logoUrl)\
             VALUES('{}','{}','{}')\
             RETURNING name, hqAddress, logoUrl'''\
            .format(name, hqAddress, logoUrl))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party

	def get_parties(self):
		"""Fetch all parties."""

		query = "SELECT * from parties"
		parties = Database().fetch(query)
		return json.dumps(parties, default=str)

	def get_party(self, party_id):
		"""Fetch a single party"""

		self.curr.execute(""" SELECT * FROM parties WHERE party_id={}""".format(party_id ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return json.dumps(party, default=str)

	def get_name(self, name):
		"""Get party with specific name."""

		self.curr.execute(''' SELECT * FROM parties WHERE name=%s''',(name, ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party

	def get_hqAddress(self, hqAddress):
		"""Get party with specific hqAddress."""

		self.curr.execute(''' SELECT * FROM parties WHERE hqAddress=%s''',(hqAddress, ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party

	def get_logoUrl(self, logoUrl):
		"""Get party with specific logoUrl."""

		self.curr.execute(''' SELECT * FROM parties WHERE logoUrl=%s''',(logoUrl, ))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party

	def delete(self, party_id):
		''' Delete order '''
		
		self.curr.execute(''' DELETE FROM parties WHERE party_id=%s''',(party_id, ))
		self.conn.commit()
		self.curr.close()

	def edit_party(self, party_id, name, hqAddress, logoUrl):
		"""User can Change name of the party."""

		self.curr.execute("""UPDATE parties\
			SET name='{}', hqAddress='{}', logoUrl='{}'\
			WHERE party_id={} RETURNING name, hqAddress, logoUrl"""\
			.format(party_id,name,hqAddress,logoUrl))
		party = self.curr.fetchone()
		self.conn.commit()
		self.curr.close()
		return party