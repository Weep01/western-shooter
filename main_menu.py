import pygame
from pygame.locals import *
from game import Game
from credits import credits_menu

def main_menu_func(screen):
    # Initialisation des boutons du menu principal sous forme de classes
    class button:
        class play_button:
            def __init__(self):
                self.x = 565
                self.y = 250
                self.image = pygame.image.load('Images/menu/play_button.png')
                #self.unpressed = pygame.image.load('')
        class credits_button:
            def __init__(self):
                self.x = 480
                self.y = 375
                self.image = pygame.image.load('Images/menu/credits_button.png')
                #self.unpressed = pygame.image.load('')
        class stop_button:
            def __init__(self):
                self.x = 490
                self.y = 505
                self.image = pygame.image.load('Images/menu/quit_button.png')
                #self.unpressed = pygame.image.load('')


    menu_bg = pygame.image.load('Images/assets/game_background.png')
    menu_blur = pygame.image.load('Images/menu/menu_background.png')
    menu_square = pygame.image.load('Images/menu/menu_square.png')

    button_list = [button.play_button, button.credits_button, button.stop_button]

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 100)

    from functions import draw_text, mouse_get

    while True:
        screen.blit(menu_bg, (0, 0))
        screen.blit(menu_blur, (0, 0))
        screen.blit(menu_square, (335, 175))

        draw_text('Western Shooter', font, (255, 255, 255), screen, 640, 90)

        mouse_x, mouse_y = mouse_get()

        # Animation en pointant les boutons + action au clic
        for i in button_list:
            temp = i()
            if temp.image.get_rect().collidepoint(mouse_x - temp.x, mouse_y - temp.y):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if (i == button.stop_button):
                            print("\nVous avez quitté le jeu.\nMerci d'avoir joué au Western Shooter !\n")
                            pygame.quit()
                            exit()
                        if (i == button.play_button):
                            game = Game()
                            game.start(screen)
                            return
                        if (i == button.credits_button):
                            credits_menu(screen)
            screen.blit(temp.image, (temp.x, temp.y))

        # Action en cas de fermeture du programme (afin d'éviter les erreurs)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        
        # Actualisation de l'affichage
        pygame.display.update()
        clock.tick(60)