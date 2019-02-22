
class OfficeModels():
	"""
	This class takes care of Office Models
	"""
	def __init__(self):
		self.offices = []

	def create_office(self, id, name, description, location, status, created_at):
		self.name = name
		self.id = id
		self.description = description
		self.location = location
		self.created_at = created_at
		self.status = status

		self.office_payload = {
			"id": self.id,
			"name": self.name,
			"description": self.description,
			"location": self.location,
			"created_at": self.created_at,
			"status": self.status
		}
		self.offices.append(self.office_payload)

		return self.office_payload

	def fetchone(self, office_id):
		office = [office for office in self.offices if office['id'] == office_id]

		if office:
			return office
		else:
			return None
			
	def fetchall(self):
		return self.offices