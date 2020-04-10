import datetime


class LoggerController:

    def __init__(self, logDir):
        self._fileLog = open(logDir + '/app.log', 'a')

    def log(self, message: str = ''):
        dateTime = datetime.datetime.now()
        dateStr = dateTime.strftime('%Y %m %d - %H : %M : %S')
        self._fileLog.write(dateStr + ' - ' + message)
