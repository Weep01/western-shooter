import pygame
from pygame.locals import *
from functions import init
from main_menu import main_menu_func

global screen
screen = init()
main_menu_func(screen)