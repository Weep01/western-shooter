import re
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

        def credits_names():
            text = pygame.font.SysFont(None, 100).render("Crédits", True, "White")
            text_ = pygame.font.SysFont(None, 75).render("Développeurs", True, "White")
            text1 = pygame.font.SysFont(None, 50).render("Dizdarevic Tom", True, "White")
            text2 = pygame.font.SysFont(None, 50).render("Amiotte Thomas", True, "White")
            text3 = pygame.font.SysFont(None, 50).render("Vanlaeres Louis", True, "White")
            text4 = pygame.font.SysFont(None, 50).render("Nazrul Islam Thambir", True, "White")
            text5 = pygame.font.SysFont(None, 75).render("Graphismes", True, "White")
            text6 = pygame.font.SysFont(None, 50).render("Merle Clara", True, "White")
            text7 = pygame.font.SysFont(None, 50).render("Travouillon Eva", True, "White")
            position_text  = text.get_rect(center=(640, 50))
            position_text_ = text_.get_rect(center=(640, 125))
            position_text1 = text1.get_rect(center=(640, 175))
            position_text2 = text2.get_rect(center=(640, 225))
            position_text3 = text3.get_rect(center=(640, 275))
            position_text4 = text4.get_rect(center=(640, 325))
            position_text5 = text5.get_rect(center=(640, 400))
            position_text6 = text6.get_rect(center=(640, 450))
            position_text7 = text7.get_rect(center=(640, 500))
            screen.blit(text, position_text)
            screen.blit(text1, position_text1)
            screen.blit(text2, position_text2)
            screen.blit(text3, position_text3)
            screen.blit(text4, position_text4)
            screen.blit(text5, position_text5)
            screen.blit(text6, position_text6)
            screen.blit(text7, position_text7)
            screen.blit(text_, position_text_)
            return 
        credits_names()    

        #Retourner au menu
        if button.image.get_rect().collidepoint(mouse_x - button.x, mouse_y - button.y):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return
            
        

        # Quitter le jeu 
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
        
        pygame.display.update()
        clock.tick(60)
        
