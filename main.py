import pygame
from game import *
import math
pygame.init()

#generer fenetre jeu
pygame.display.set_caption("nomjeu")
screen = pygame.display.set_mode((1080, 650))

#arriere plan
background = pygame.image.load('assets/f.png')

#importer banniere
banner = pygame.image.load('assets/banniere.png')
banner = pygame.transform.scale(banner, (400,400))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)

#importer bouton de jeu
play_button = pygame.image.load('assets/play now.png')
play_button = pygame.transform.scale(play_button, (200,200))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3)
play_button_rect.y = math.ceil(screen.get_height()/2)

#lancer jeu
game = Game()


running = True

# boucle tant que running True
while running:

    # arriere plan jeu
    screen.blit(background, (0, -30))

    #verifier si jeu à commencé
    if game.is_playing:
        #declanché instruction partie
        game.update(screen)
    #verif si jeu n'a pas commencé
    else:
        #ajouter mon ecran de bvn
        screen.blit(banner, (banner_rect))
        screen.blit(play_button, (play_button_rect))



    #mettre à jour l'ecran
    pygame.display.flip()

    # si joueur ferme fenetre
    for event in pygame.event.get():
        #verifier fermeture fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu !")
        #Detecter clavier
        elif event.type == pygame.KEYDOWN:
            #Pression touche
            game.pressed[event.key] = True
            #detecter si espace utilisé
            if event.key == pygame.K_m:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #si clic souris en collision avec jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé
                game.is_playing = True
