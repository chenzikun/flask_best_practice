import unittest
from flask import request
from ..app import create_app

class RequestTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")

    def test_url(self):
        with self.app.test_request_context('/hello', method='POST'):
            assert request.method == 'POST'


    def tearDown(self):
        self.app.shutdown()
