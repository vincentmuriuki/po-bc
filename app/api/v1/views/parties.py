from flask_restful import Resource, reqparse
from ..models.parties import PartyOperations
from flask import jsonify, make_response
import datetime as dt

party_operations = PartyOperations()
parties = party_operations.fetchall()

class MultipleViews(Resource):
	"""
	This class takes care of get, post, and delete endpoints for all offices
	"""
	def get(self):
		parties = party_operations.fetchall()
		if parties:
			return make_response(jsonify(
					{
						'Message': 'A list of all offices',
						'Offices': parties
					}
				))
		else:
			return ({
				'Mesage': 'There are no parties to view'
				})

	def post(self):
		id = len(parties) + 1
		created_at = str(dt.datetime.now())
		status = "Inactive"
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, required=True, help="This field is required")
		parser.add_argument('description', type=str, required=True, help="This field is required")

		args = parser.parse_args()

		new_party = party_operations.create_party(id, args['name'], args['description'], status, created_at)


		# return new_party, 201
		return make_response(
			jsonify(
				{
			'Party Data': new_party
				}
					), 201)

	def delete(self):
		parties = party_operations.fetchall()
		if len(parties) == 0:
			return (
					{
						'Message': 'There are no parties to delete'
					}
				), 204

		parties = []

		return({
				'Message': 'All parties deleted'
			}), 204

class SingleParty(Resource):
	"""
	This class takes care of get, delete, and put endpoints for single  orders
	"""
	def get(self, id):
		party = party_operations.fetchone(id)

		if party:
			return make_response(
				jsonify(
					{
						'Party Data': party
					}
				), 200
			)
		else:
			return (
				{
					'Message': 'The selected office does not exist'
				}
			), 404

	def delete(self, id):
		party = party_operations.fetchone(id)
		if not party:
			return (
				{
					'Message': 'Selected party not found'
				}
			), 404
		
		parties.remove(party[0])

		return (
			{
				'Message': 'Success! Party deleted'
			}
		), 204

	def put(self, id):
		party = party_operations.fetchone(id)
		if party:
			party[0]['status'] = "Active"
			return (
				{
					'Message': 'The party is now active'
				}
			), 201

		return (
			{
				'Message': 'The selected party does not exist'
			}
		), 404