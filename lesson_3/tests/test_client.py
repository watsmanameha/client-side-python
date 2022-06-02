import time
import unittest
from lesson_3.client import create_presence, process_ans
from lesson_3.common.variables import *


class TestClient(unittest.TestCase):

    def test_create_presence(self):
        self.assertEqual(create_presence(), {ACTION: PRESENCE, TIME: time.time(), USER: {ACCOUNT_NAME: 'Guest'}})

    def test_200_ans(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')