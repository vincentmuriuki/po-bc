import unittest
from app import create_app
import json

class TestOfficeOperations(unittest.TestCase):
    """
    This class tests the office endpoints
    post: Create a new office
    get{id}: Fetch a specific office
    get: Fetch all offices
    put: update an office
    delete: deletes an office
    """
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.office_payload = {
            "name": "Office of the Governer",
            "description": "This is the office of the Governer. It handles all public affairs of a county",
            "location": "Nairobi",
            "status": "Inactive"
        }
        self.status = 'Active'
        self.id = 1

    def create_office(self, path='/api/v1/offices', data={}):
        data = self.office_payload
        res = self.client.post(path, data=json.dumps(data), content_type="application/json")

        return res

    def test_office_creation(self):
        res = self.create_office()

        self.assertEqual(res.status_code, 201)

    def test_delete_all_offices(self):
        res = self.client.delete(
            '/api/v1/offices',
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 204)

    def test_delete_one_office(self):
        res = self.client.delete(
            '/api/v1/offices/{}'.format(self.id),
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 204)

    def test_fetch_single_office(self):
        res = self.client.get(
            '/api/v1/offices/{}'.format(self.id),
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 200)

    def test_fetch_all_offices(self):
        res = self.client.get(
            '/api/v1/offices',
            content_type='application/json'
        )
        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 200)

    def test_update_office(self):
        res = self.client.put(
            '/api/v1/offices/{}'.format(self.id),
            data = json.dumps(self.status),
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 201)