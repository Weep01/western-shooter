import pygame
from main_menu import *
from functions import *


clock = pygame.time.Clock()

class credits:
    def __init__(self):
        self.x = 10
        self.y = 620
        self.image = pygame.image.load('Images/menu/back_button.png')
        self.menu_bg = pygame.image.load('Images/assets/game_background.png')
        self.menu_blur = pygame.image.load('Images/menu/menu_background.png')

def credits_menu(screen):
    button = credits()
    while True:
        mouse_x, mouse_y = mouse_get()

        # Affichage des images (fond, transparence, bouton retour)
        screen.blit(button.menu_bg, (0,0))
        screen.blit(button.menu_blur, (0,0))
        screen.blit(button.image, (30,600))


        # Affichage du texte grâce à la fonction "draw_text"
        def credits_names():
            draw_text("Crédits", pygame.font.SysFont(None, 125), "White", screen, 640, 75)
            draw_text("Développeurs", pygame.font.SysFont(None, 75), "White", screen, 640, 175)
            draw_text("Dizdarevic Tom", pygame.font.SysFont(None, 50), "White", screen, 640, 225)
            draw_text("Amiotte Thomas", pygame.font.SysFont(None, 50), "White", screen, 640, 275)
            draw_text("Vanlaeres Louis", pygame.font.SysFont(None, 50), "White", screen, 640, 325)
            draw_text("Nazrul Islam Thambir", pygame.font.SysFont(None, 50), "White", screen, 640, 375)
            draw_text("Graphismes", pygame.font.SysFont(None, 75), "White", screen, 640, 450)
            draw_text("Merle Clara", pygame.font.SysFont(None, 50), "White", screen, 640, 500)
            draw_text("Travouillon Eva", pygame.font.SysFont(None, 50), "White", screen, 640, 550)
            return 
        credits_names()    

        # Détection de pointeur + clic sur le bouton -> Retour au menu principal
        if button.image.get_rect().collidepoint(mouse_x - button.x, mouse_y - button.y):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    return
    
        # Quitter le jeu avec la croix de fermeture du programme
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            
        
        pygame.display.update()
        clock.tick(60)
        
