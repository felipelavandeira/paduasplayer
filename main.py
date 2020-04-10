import os
from flask import Flask
from flask import render_template
from flask import request
from Controllers.LoginController import LoginController
from Controllers import *

template_dir = os.path.abspath('./Views/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def __index__():
    logger.log("Teste")
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    logger.log("Teste")
    # authentication = LoginController()
    # authentication.login(email=request.args['email'], password=request.args['password'])
    # return render_template('logged.html')