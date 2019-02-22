from flask import Flask, jsonify, make_response, request
from flask_restful import Resource, reqparse
from ..models.offices import OfficeModels
import datetime as dt


office_models = OfficeModels()
offices = office_models.fetchall()

class AllOffices(Resource):
	def get(self):
		offices = office_models.fetchall()
		if offices:
			return make_response(jsonify({
					'Message': 'A list of all Government offics',
					'offices': offices
				}), 200)
		return {
			'Message': 'There are no offices to view'
		}, 404

	def post(self):
		id = len(offices) + 1
		created_at = str(dt.datetime.now())
		status = "Inactive"
		parser = reqparse.RequestParser()
		parser.add_argument(
			'name', type=str, required=True, help="This field is required"
			)
		parser.add_argument('description', type=str, required=True, help="This field is required")
		parser.add_argument('location', type=str, required=True, help="This field is required")

		args = parser.parse_args()

		new_office = office_models.create_office(id, args['name'], args['description'], args['location'], created_at, status)

		return new_office, 201

	def delete(self):
		offices = office_models.fetchall()
		if len(offices) == 0:
			return (
				{
					'Message': 'There are no offices to delete'
				}
			), 204

		offices = []
		return (
			{
				'Message': 'All offices deleted!'
			}
		), 204
			
class IndividualOffices(Resource):
	def get(self, id):
		office = office_models.fetchone(id)
		if office is None:
			return ({
					'Message': 'Office not found'
				}), 404

		return (
			{
				'Mesage': 'Success',
				'Office Details': office
			}, 200)

	def put(self, id):
		office = office_models.fetchone(id)
		if not office:
			return (
				{
					'Message': 'Selected office was not found'
				}
			), 404
		office[0]['status'] = "Active"

		return (
			{
				'Message': 'The office is now active'
			}
		), 201

	def delete(self, id):
		office = office_models.fetchone(id)
		if not office:
			return (
				{
					'Message': 'Selected office was not found'
				}
			), 404
		else:
			offices.remove(office[0])
			return (
				{
					'Message': 'Success! Office deleted'
				}
			), 204

class Home(Resource):
	def get(self):
		return redirect("https://github.com/zalando/connexion")