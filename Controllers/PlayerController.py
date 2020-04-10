from Controllers import *
import pygame
import os

pygame.init()


class PlayerController:
    def __init__(self, playlist=[]):
        self.indexMusicaAtual = 0
        self.playlist = playlist
        self.tocando = False
        self.SONG_END = pygame.USEREVENT + 1

    def setPlaylist(self, playlist=[]):
        self.playlist = playlist

    def verificaSongEnd(self):
        for event in pygame.event.get():
            if event.type == self.SONG_END:
                self.proxima()

    def play(self):
        musicDir = os.path.abspath('./Controllers/Musics')
        pygame.mixer_music.load(musicDir + '/' + self.playlist[self.indexMusicaAtual])
        pygame.mixer_music.play(1, 0.0)
        pygame.mixer.music.set_endevent(self.SONG_END)
        self.tocando = True
        logger.log("Iniciando a reprodução da música {}".format(self.playlist[self.indexMusicaAtual]))

    def proxima(self):
        if self.indexMusicaAtual + 2 <= len(self.playlist):
            self.indexMusicaAtual = self.indexMusicaAtual + 1
        else:
            self.indexMusicaAtual = 0
        logger.log("Reproduzindo a próxima música")
        self.play()

    def anterior(self):
        if self.indexMusicaAtual - 1 >= 0:
            self.indexMusicaAtual = self.indexMusicaAtual - 1
        else:
            self.indexMusicaAtual = len(self.playlist) - 1
        logger.log("Reproduzindo a música anterior")
        self.play()

    def pause(self):
        if self.tocando:
            pygame.mixer_music.pause()
            self.tocando = False
            logger.log("Pausando a reprodução da música {}".format(self.playlist[self.indexMusicaAtual]))
        elif not self.tocando:
            pygame.mixer_music.unpause()
            self.tocando = True
            logger.log("Retomando a reprodução da música {}".format(self.playlist[self.indexMusicaAtual]))
