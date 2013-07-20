from classes.Server import *

class DataStorage:

	def __init__(self, serverid, appid):
		self.ServerID = serverid
		self.appID = appid
		self.server = Server(self.ServerID, "Webserverrrr")
	def store(self, data, currentDateTime):
		output = "Stored: {data} from app {appid} on server {serverid} {servername} at {currentDateTime}".format(data=data, appid=self.appID, serverid=self.ServerID,servername=self.server.serverInfo(self.ServerID),currentDateTime=currentDateTime)
		return output
		# return "Stored:",data,"from",self.appID,"on",self.ServerID,"at",currentDateTime
