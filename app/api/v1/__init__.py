from flask_restful import Api
from flask import Blueprint
from .views.offices import AllOffices, IndividualOffices, Home
from .views.parties import MultipleViews, SingleParty
# import views

version1 = Blueprint('api1', __name__, url_prefix='/api/v1')

api = Api(version1)

api.add_resource(Home, '/')
api.add_resource(AllOffices, '/offices')
api.add_resource(IndividualOffices, '/offices/<int:id>')
api.add_resource(MultipleViews, '/parties')
api.add_resource(SingleParty, '/parties/<int:id>')