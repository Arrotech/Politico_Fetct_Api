voters = []


class VotersModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = voters

	def save(self, createdOn, createdBy, office, candidate):
		"""Save a vote."""

		new_vote = {
		"vote_id" : len(self.entries)+1,
		"createdOn" : createdOn,
		"createdBy" : createdBy,
		"office" : office,
		"candidate" : candidate,
		}
		self.entries.append(new_vote)
		return self.entries