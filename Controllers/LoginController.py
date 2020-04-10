from Controllers import *


class LoginController:

    def __init__(self):
        self._auth = firebase.auth()
        self._login = None

    def login(self, email: str = '', password: str = ''):
        # logar
        self._login = self.auth.sign_in_with_email_and_password(email, password)
        logger.log("Usuário logado com sucesso")

    def signUp(self, email: str = '', password: str = ''):
        # criar usuario
        user = self.auth.create_user_with_email_and_password(email, password)
        logger.log("Usuário {} cadastrado com sucesso".format(email))
        # enviar email de confirmacao
        self._auth.send_email_verification(self._login['idToken'])

    def forgotPass(self, email: str = ''):
        # enviar email de recuperacao de senha
        self._auth.send_password_reset_email(email)

    @property
    def auth(self):
        return self._auth
