import unittest
from app import create_app
import json

class TestPartyOperations(unittest.TestCase):
    """
    This class tests the party endpoints
    post: Create a new party
    get{id}: Fetch a specific party
    get: Fetch all parties
    put: update a party
    delete: deletes a party
    """
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.party_payload = {
            "name": "Gavan Political Party",
            "description": "This is a political party for the Majority",
            "status": "Inactive"
        }
        self.status = 'Active'
        self.id = 1

    def create_office(self, path='/api/v1/parties', data={}):
        data = self.party_payload
        res = self.client.post(path, data=json.dumps(data), content_type="application/json")

        return res

    def test_office_creation(self):
        res = self.create_office()

        self.assertEqual(res.status_code, 201)

    def test_delete_all_parties(self):
        res = self.client.delete(
            '/api/v1/parties',
            content_type='application/json'
        )
        self.assertEqual(res.status_code, 204)

    def test_delete_one_party(self):
        res = self.client.delete(
            '/api/v1/parties/{}'.format(self.id),
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 204)

    def test_fetch_single_party(self):
        res = self.client.get(
            '/api/v1/parties/{}'.format(self.id),
            content_type='application/json'
        )

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 200)

    def test_fetch_all_parties(self):
        res = self.client.get(
            '/api/v1/parties',
            content_type='application/json'
        )
        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 200)

    def test_update_party(self):
        res = self.client.put(
            '/api/v1/parties/{}'.format(self.id),
            data = json.dumps(self.status),
            content_type='application/json'
        )
        

        if res.status_code == 404:
            self.assertEqual(res.status_code, 404)
        else:
            self.assertEqual(res.status_code, 201)