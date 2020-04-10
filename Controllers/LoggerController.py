import datetime


class LoggerController:

    def __init__(self, logDir):
        self._lodDir = logDir

    def log(self, message: str = ''):
        dateTime = datetime.datetime.now()
        dateStr = dateTime.strftime('%Y %m %d - %H : %M : %S')
        fileLog = open(self._lodDir + '/app.log', 'a+')
        fileLog.write(dateStr + ' - ' + message + '\n')
        fileLog.close()
