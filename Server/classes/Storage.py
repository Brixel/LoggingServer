class DataStorage:
	def __init__(self, serverid, appid):
		self.ServerID = serverid
		self.appID = appid

	def store(self, data):
		return "Stored:",data
