import unittest
import json
from app import app  # Adjust the import according to your app's file structure

class ComedyGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        """Set up the test client and other test prerequisites."""
        self.app = app.test_client()
        self.app.testing = True

    def test_generate_comedy(self):
        """Test the /api/generate_comedy endpoint."""
        response = self.app.post('/api/generate_comedy',
                                 data=json.dumps({
                                     'style': 'Stand-up',
                                     'gender': 'female',
                                     'dimension': 4
                                 }),
                                 content_type='application/json')

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('comedy_show', data)
        self.assertTrue(data['comedy_show'].startswith('Welcome to the 4th dimension'))

    def test_generate_comedy_missing_fields(self):
        """Test the /api/generate_comedy endpoint with missing fields."""
        response = self.app.post('/api/generate_comedy',
                                 data=json.dumps({
                                     'style': 'Stand-up',
                                     'dimension': 4
                                 }),
                                 content_type='application/json')

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 422)
        self.assertIn('errors', data)
        self.assertIn('gender', data['errors']['json'])
        self.assertEqual(data['errors']['json']['gender'][0], 'Missing data for required field.')

if __name__ == '__main__':
    unittest.main()
