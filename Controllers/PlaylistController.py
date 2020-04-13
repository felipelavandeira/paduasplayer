import random
import os
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

    def randomizePlaylist(self):  # Metodo para randomizar lista
        random.shuffle(self._playlist)
        print(self._playlist)

    def generatePlaylist(self):  # Metodo que gera uma playlist a partir das musicas na pasta 'Musics'
        musicDir = os.path.abspath('./musics')
        self._playlist = os.listdir(musicDir)

        return self._playlist

    def clearPlaylist(self):  # Metodo que limpa a Playlist
        self._playlist.clear()
        print(self._playlist)

    def addToPlaylist(self, musica):  # Metodo que Adiciona uma nova musica na Playlist
        self._playlist.append(musica)
