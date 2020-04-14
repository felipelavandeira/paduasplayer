from flask import Flask, redirect
from flask import render_template
from flask import request

from Controllers import *
from Controllers.LoginController import LoginController
from Controllers.PlayerController import PlayerController
from Controllers.PlaylistController import PlaylistController

template_dir = os.path.abspath('./Views/templates')
assets_dir = os.path.abspath('./Views/assets')
app = Flask(__name__, template_folder=template_dir, static_folder=assets_dir)
player = PlayerController()
authentication = LoginController(firebase, logger)
playlistSet = PlaylistController()
playlist = playlistSet.generatePlaylist()


@app.route('/')
def __index__():
    if authentication.loggedUSer is not None:
        return redirect('/player')
    else:
        return render_template('index.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/createuser', methods=['POST'])
def createUser():
    logger.log("Cadastrando o usuário com e-mail {}".format(request.form['email']))
    authentication.signUp(email=request.form['email'], password=request.form['password'])
    return redirect('/player')


@app.route('/player')
def playerScreen():
    if authentication.loggedUSer is not None:
        logger.log("Usuário logado com id {}".format(authentication.loggedUSer))
        return render_template('music.html')
    else:
        logger.log("Usuário não logado, redirecionando para o login")
        return redirect('/')


@app.route('/login', methods=['POST'])
def login():
    authentication.login(email=request.form['email'], password=request.form['password'])
    return redirect('/player')


@app.route('/play', methods=['POST'])
def play():
    player.play()
    # Loop infinito é para que a reprodução não acabe
    # após o fim da primeira música
    while True:
        player.verificaSongEnd()
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


@app.route('/rand', methods=['POST'])
def rand():
    player.stop()
    playlistSet.randomizePlaylist()
    player.playlist = playlistSet.playlist
    return "Randomizando a Playlist"


@app.route('/generate', methods=['POST'])
def generate():
    player.stop()
    generatedPlaylist = playlistSet.generatePlaylist()
    player.playlist = generatedPlaylist
    return "Gerando uma nova playlist"


@app.route('/clear', methods=['POST'])
def clear():
    playlistSet.clearPlaylist()
    player.playlist = playlistSet.playlist
    player.stop()
    return "Limpando a Playlist"
