from flask import Flask
from flask import render_template
from flask import request
from Controllers import *
from Controllers.LoginController import LoginController
from Controllers.PlayerController import PlayerController
from Controllers.PlaylistController import PlaylistController

template_dir = os.path.abspath('./Views/templates')
app = Flask(__name__, template_folder=template_dir)
player = PlayerController()


@app.route('/')
def __index__():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    logger.log("Iniciando a tela de login para {}/{}".format(request.form['email'], request.form['password']))
    authentication = LoginController()
    authentication.login(email=request.form['email'], password=request.form['password'])
    return render_template('logged.html')


@app.route('/play', methods=['POST'])
def play():
    playlist = PlaylistController()
    playlist.generatePlaylist()
    player.setPlaylist(playlist.playlist)
    player.play()
    return 'Iniciando o player'


@app.route('/pause', methods=['POST'])
def pause():
    player.pause()
    return 'Parando o player'


@app.route('/next', methods=['POST'])
def next():
    player.proxima()
    return "Mudando de Música"


@app.route('/prev', methods=['POST'])
def prev():
    player.anterior()
    return "Mudando de música"