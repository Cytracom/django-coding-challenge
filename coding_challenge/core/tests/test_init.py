from rest_framework.test import APITestCase

class BasicTestCase(APITestCase):
    def test_true(self):
        self.assertTrue(True)