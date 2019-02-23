import json
parties = []


class PartiesModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = parties

	def save(self, name, hqAddress, logoUrl):
		"""Save a new party that has been created."""

		new_party = {
		"party_id" : len(self.entries)+1,
		"name" : name,
		"hqAddress" : hqAddress,
		"logoUrl" : logoUrl,
		}
		self.entries.append(new_party)
		return self.entries

	def get_name(self, name):
		"""Get a party with a specific name."""

		for party in self.entries:
			if party['name'] == name:
				return json.dumps(party, default=str)

	def get_hqAddress(self, hqAddress):
		"""Get party by hqAddress."""

		for party in self.entries:
			if party['hqAddress'] == hqAddress:
				return party

	def get_logoUrl(self, logoUrl):
		"""Get party by logoUrl."""

		for party in self.entries:
			if party['logoUrl'] == logoUrl:
				return party

	def get_all_parties(self):
		"""Fetch all the existing parties."""

		return self.entries

	def get_a_party(self, party_id):
		"""Fetch a specific political party."""

		if self.entries:
			for party in self.entries:
				if party.get('party_id') == party_id:
					return party

	def update_party(self, party_id, details):
		"""Updates an existing party."""

		for party in self.entries:
			if party['party_id'] == party_id:
				name = details.get('name')
				hqAddress = details.get('hqAddress')
				logoUrl = details.get('logoUrl')
				if name:
					party['name']  = name
				if hqAddress:
					party['hqAddress'] = hqAddress
				if logoUrl:
					party['logoUrl'] = logoUrl
				return party
