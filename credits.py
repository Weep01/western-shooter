import pygame
from main_menu import *
from functions import *


BLACK = (0,0,0)
clock = pygame.time.Clock()


class credits:
    def __init__(self):
        self.x = 10
        self.y = 620
        self.image = pygame.image.load('Images/menu/back_button.png')
        self.menu_bg = pygame.image.load('Images/assets/game_background.png')
        self.menu_blur = pygame.image.load('Images/menu/menu_background.png')

button_list = [credits]

def credits_menu(screen):
    button = credits()
    while True:
        mouse_x, mouse_y = mouse_get()

        screen.blit(button.menu_bg, (0,0))
        screen.blit(button.menu_blur, (0,0))
        screen.blit(button.image, (30,600))
        if button.image.get_rect().collidepoint(mouse_x - button.x, mouse_y - button.y):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return

        # SI BOUTON CLIQUE
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        clock.tick(60)
        
