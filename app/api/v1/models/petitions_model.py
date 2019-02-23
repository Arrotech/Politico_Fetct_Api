petitions = []


class PetitionsModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = petitions

	def save(self, createdOn, createdBy, office, body):
		"""Save petition."""

		new_petition = {
		"petition_id" : len(self.entries)+1,
		"createdOn" : createdOn,
		"createdBy" : createdBy,
		"office" : office,
		"body" : body,
		}
		self.entries.append(new_petition)
		return self.entries