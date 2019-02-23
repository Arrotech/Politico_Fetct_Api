candidates = []


class CandidatesModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = candidates

	def save(self, office, party, candidate):
		"""Save a new party that has been created."""

		new_candidate = {
		"candidate_id" : len(self.entries)+1,
		"office" : office,
		"party" : party,
		"candidate" : candidate,
		}
		self.entries.append(new_candidate)
		return self.entries