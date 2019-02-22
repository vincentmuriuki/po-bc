
class PartyOperations():
	"""
	This class takes care of Party Models
	"""
	def __init__(self):
		self.parties = []

	def create_party(self, id, name, description, status, created_at):
		self.id = id
		self.name = name
		self.description = description
		self.created_at = created_at
		self.status = status

		self.party_payload = {
			"id": self.id,
			"name": self.name,
			"description": self.description,
			"created_at": self.created_at,
			"status": self.status
		}

		self.parties.append(self.party_payload)

		return self.party_payload


	def fetchall(self):
		return self.parties

	def fetchone(self, party_id):
		party = [party for party in self.parties if party['id'] == party_id]
		if party:
			return party
		else:
			return None