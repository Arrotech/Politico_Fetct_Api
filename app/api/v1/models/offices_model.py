import json
offices = []


class OfficesModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = offices

	def save(self, category, name):
		"""Save a new party that has been created."""

		new_office = {
		"office_id" : len(self.entries)+1,
		"category" : category,
		"name" : name,
		}
		self.entries.append(new_office)
		return self.entries

	def get_all_offices(self):
		"""Fetch all the existing offices."""

		return self.entries

	def get_an_office(self, office_id):
		"""Fetch a specific political office."""

		if self.entries:
			for office in self.entries:
				if office.get('office_id') == office_id:
					return office

	def get_name(self, name):
		"""Get party by hqAddress."""

		for office in self.entries:
			if office['name'] == name:
				return json.dumps(office, default=str)

	def update_office(self, office_id, details):
		"""Update an existing office."""

		for office in self.entries:
			if office['office_id'] == office_id:
				category = details.get('category')
				name = details.get('name')
				if category:
					office['category']  = category
				if name:
					office['name'] = name
				return office
