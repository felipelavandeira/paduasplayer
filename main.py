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
    playlist = PlaylistController()#executar quando abrir a pagina do player, possivelmente mudar a rota
    playlist.generatePlaylist()# same here ^
    player.setPlaylist(playlist.playlist)# same here ^
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
# ==================Rotas da Playlist=========================
@app.route('/rand', methods=['POST'])
def rand():
    playlist.randomizePlaylist()
    player.setPlaylist(playlist.getPlaylist())
    return "Randomizando a Playlist"    

@app.route('/clear', methods=['POST'])
def clear():
    playlist.clearPlaylist()
    player.setPlaylist(playlist.getPlaylist())
    return "Limpando a Playlist"

@app.route('/add/<musica>', methods=['POST','GET'])    
def add(musica:str):
    playlist.addToPlaylist(musica)
    player.setPlaylist(playlist.getPlaylist())
    return "Adicionando a musica {} a playlist".format(musica)

@app.route('/remove/<musica>', methods=['POST', 'GET'])    
def remove(musica:str):
    playlist.removeFromPlaylist(musica)
    player.setPlaylist(playlist.getPlaylist())
    return "Removendo a musica {} da playlist".format(musica)
