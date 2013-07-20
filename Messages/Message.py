import json

class Message:
	def __init__(self, jsonObject):
		messageAttributes = json.JSONDecoder(jsonObject)
		if(not 'AppID' in messageAttributes):
			raise Exception("I know python!")