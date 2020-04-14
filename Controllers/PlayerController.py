from Controllers import *
import pygame
import os

pygame.init()


class PlayerController:
    def __init__(self, playlist: list = []):
        self._indexMusicaAtual = 0
        self._playlist = playlist
        self._tocando = False
        self._SONG_END = pygame.USEREVENT + 1

    @property
    def playlist(self):
        return self._playlist

    @playlist.setter
    def playlist(self, playlist=[]):
        self._playlist = playlist

    def verificaSongEnd(self):
        for event in pygame.event.get():
            if event.type == self._SONG_END:
                self.proxima()

    def play(self):
        musicDir = os.path.abspath('./musics')
        pygame.mixer_music.load(musicDir + '/' + self._playlist[self._indexMusicaAtual])
        pygame.mixer_music.play(1, 0.0)
        pygame.mixer.music.set_endevent(self._SONG_END)
        self._tocando = True
        logger.log("Iniciando a reprodução da música {}".format(self._playlist[self._indexMusicaAtual]))

    def proxima(self):
        if self._indexMusicaAtual + 2 <= len(self._playlist):
            self._indexMusicaAtual = self._indexMusicaAtual + 1
        else:
            self._indexMusicaAtual = 0
        logger.log("Reproduzindo a próxima música")
        self.play()

    def anterior(self):
        if self._indexMusicaAtual - 1 >= 0:
            self._indexMusicaAtual = self._indexMusicaAtual - 1
        else:
            self._indexMusicaAtual = len(self._playlist) - 1
        logger.log("Reproduzindo a música anterior")
        self.play()

    def pause(self):
        if self._tocando:
            pygame.mixer_music.pause()
            self._tocando = False
            logger.log("Pausando a reprodução da música {}".format(self._playlist[self._indexMusicaAtual]))
        elif not self._tocando:
            pygame.mixer_music.unpause()
            self._tocando = True
            logger.log("Retomando a reprodução da música {}".format(self._playlist[self._indexMusicaAtual]))

    def stop(self):
        self._indexMusicaAtual = 0
        logger.log("Parando a reprodução por completo")
        pygame.mixer_music.stop()
