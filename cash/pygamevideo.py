import os
import pygame
from pygame.locals import *
from algorithm import *
import Tools
pygame.init()
pygame.mixer.quit()
movie = pygame.movie.Movie('gif/Move.avi')
movie.set_display(pygame.display.set_mode((563,720)))
movie.set_volume(1)
movie.play()

for event in pygame.event.get():
  if event.type == QUIT:
    exit()