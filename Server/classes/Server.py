class Server:
	"""docstring for Server"""
	def __init__(self, serverid, servername):
		self.ServerID = serverid
		self.ServerName = servername

	def serverInfo(self, serverid):
		output = "[Server has this name: {ServerName}]".format(ServerID=serverid, ServerName=self.ServerName)
		return output
		