import pygame
from game import Game
pygame.init()

#generer fenetre jeu
pygame.display.set_caption("nomjeu")
screen = pygame.display.set_mode((1080, 650))

#arriere plan
background = pygame.image.load('assets/f.png')


#charger le jeu
game = Game()


running = True

# boucle tant que running True
while running:

    # arriere plan jeu
    screen.blit(background, (0,-30))

    # recup projec joueurs
    for projectile in game.player.all_projectiles:
        projectile.move()

    #appliquer image joueur
    screen.blit(game.player.image, game.player.rect)
    screen.blit(game.player2.image, game.player2.rect)

    #limite ecran
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 1020 :
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -5:
        game.player.move_left()
    if game.pressed.get(pygame.K_RIGHT) and game.player2.rect.x < 1020 :
        game.player2.move_right()
    if game.pressed.get(pygame.K_LEFT) and game.player2.rect.x > -5:
        game.player2.move_left()

    # appliquer image projectile
    game.player.all_projectiles.draw(screen)

    print(game.player.rect.x)

    game.player2.all_projectiles.draw(screen)

    print(game.player2.rect.x)



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
            if event.key == pygame.K_RSHIFT:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

