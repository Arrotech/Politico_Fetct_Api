users = []


class UsersModel():         

	def __init__(self):
		"""Initialization."""
		
		self.entries = users

	def save(self, firstname, lastname, othername, email, phoneNumber, passportUrl, role):
		"""Save a new party that has been created."""

		new_user = {
		"user_id" : len(self.entries)+1,
		"firstname" : firstname,
		"lastname" : lastname,
		"othername" : othername,
		"email" : email,
		"phoneNumber" : phoneNumber,
		"passportUrl" : passportUrl,
		"role" : role,
		}
		self.entries.append(new_user)
		return self.entries