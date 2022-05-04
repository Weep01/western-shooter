import pygame
from pygame.locals import *

def init():
    global screen
    screen = ""
    pygame.init()
    pygame.display.set_caption('Projet Transverse')
    screen = pygame.display.set_mode((1280, 720))
    return screen


def draw_text(content, font, color, surface, x, y):
    text = font.render(content, 1, color)
    textsize = text.get_rect()
    textsize.topleft = (x, y)
    surface.blit(text, textsize)

def mouse_get():
    x,y = pygame.mouse.get_pos()
    return x,y