import random
import os
# Classe responsavel pela manipulação da playlist
class PlaylistController():
    def __init__(self):
        self.playlist = []

    def randomizePlaylist(self): #Metodo para randomizar lista
        random.shuffle(self.playlist)
        print(self.playlist)

    def generatePlaylist(self):# Metodo que gera uma playlist a partir das musicas na pasta 'Musics'
        musicDir = os.path.abspath('./Controllers/Musics')
        self.playlist = os.listdir(musicDir)
        print(self.playlist)
        pass

    def clearPlaylist(self):# Metodo que limpa a Playlist
        self.playlist.clear()
        print(self.playlist)

    def removeFromPlaylist(self, musica: str):# Metodo que Remove uma musica da Playlist
        self.playlist.remove(musica)
        print(self.playlist)

    def addToPlaylist(self, musica: str):# Metodo que Adiciona uma nova musica na Playlist
        self.playlist.append(musica)
        print(self.playlist)
