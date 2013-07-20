import unittest
import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import Messages

import json

class TestMessage(unittest.TestCase):
	
	def test_constructWithInvalidJsonShouldThrowException(self):
		jsonMessage = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
		message = Message(jsonMessage)
		self.assertRaises(NoValidJsonException)

if __name__ == '__main__':
	unittest.main()