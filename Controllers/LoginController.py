from Controllers import *


class LoginController:

    def __init__(self, firebase, logger: LoggerController):
        self._auth = firebase.auth()
        self._logger = logger
        self._login = None
        self._loggedUSer = None

    def login(self, email: str = '', password: str = ''):
        # logar
        self._login = self.auth.sign_in_with_email_and_password(email, password)
        self._logger.log("Usuário de email {} logado com sucesso".format(email))
        self._loggedUSer = self._login['localId']

    def signUp(self, email: str = '', password: str = ''):
        # criar usuario
        user = self.auth.create_user_with_email_and_password(email, password)
        self._logger.log("Usuário {} cadastrado com sucesso".format(email))
        self._loggedUSer = user['localId']

    def forgotPass(self, email: str = ''):
        # enviar email de recuperacao de senha
        self._auth.send_password_reset_email(email)

    @property
    def auth(self):
        return self._auth

    @property
    def loggedUSer(self):
        return self._loggedUSer
