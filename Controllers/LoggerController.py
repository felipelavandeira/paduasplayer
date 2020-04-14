import datetime


class LoggerController:

    def __init__(self, logDir):
        self._lodDir = logDir
        self._dateTime = datetime.datetime.now()
        self._dateStr = self._dateTime.strftime('%Y %m %d - %H : %M : %S')

    def log(self, message: str = ''):
        fileLog = open(self._lodDir + '/app.log', 'a+')
        fileLog.write(self._dateStr + ' - ' + message + '\n')
        fileLog.close()

    def logList(self, messages: list = []):
        with open(self._lodDir + '/app.log', 'a+') as fileLog:
            fileLog.write('{} - Playlist é: ['.format(self._dateStr))
            for item in messages:
                fileLog.write(item + ',')
            fileLog.write(']\n')
