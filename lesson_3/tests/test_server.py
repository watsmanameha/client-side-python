import time
from unittest import TestCase
from lesson_3.server import process_client_message
from lesson_3.common.variables import *


class TestServer(TestCase):

    def test_client_message(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}}),
                         {RESPONSE: 200})

    def test_client_bad_request(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: 'NotGuest'}}),
            {RESPONSE: 400, ERROR: 'Bad Request'})

