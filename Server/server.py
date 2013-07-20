#This is the LoggingServer
import time
from classes.Storage import *
serverID = 100
appID = 0
DataStore = DataStorage(serverID, appID)
def LogValidation(appID, formdata, headers, sessiondata, datetime, validationerror, failedfield, loglevel):
	print DataStore.store(formdata,currentTime)


currentTime = time.asctime(time.localtime(time.time()))
LogValidation(appID, 'formData', 'headers', 'sessionData', currentTime, 'validationError', 'failedField', 'logLevel')
