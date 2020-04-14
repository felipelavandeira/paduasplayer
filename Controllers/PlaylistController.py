import random
from Controllers import *


# Classe responsavel pela manipulação da playlist
class PlaylistController:
    def __init__(self):
        self._playlist = []

    @property
    def playlist(self):
        return self._playlist

    @playlist.setter
    def playlist(self, playlist):
        self._playlist = playlist

    def generatePlaylist(self):  # Metodo que gera uma playlist a partir das musicas na pasta 'Musics'
        musicDir = os.path.abspath('./musics')
        self._playlist = os.listdir(musicDir)
        logger.logList(self._playlist)
        return self._playlist

    def randomizePlaylist(self):  # Metodo para randomizar lista
        if len(self._playlist) == 0:
            self.generatePlaylist()
        random.shuffle(self._playlist)
        logger.logList(self._playlist)

    def clearPlaylist(self):  # Metodo que limpa a Playlist
        self._playlist.clear()
        logger.logList(self._playlist)
