from main_menu import *
from player import Player

def game_menu_func(screen):
    clock = pygame.time.Clock()

    # INTIALISATION DES JOUEURS
    player_1 = Player(200, 200, 1)
    #player_2 = Player(400, 200, 2)

    while True:
        clock.tick(60)
        screen.fill((0,0,0))

        player_1.move()

        # EVENT (REPLACER PAR CASE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_a:
                        print("left")
                        player_1.left_move = True
                    case pygame.K_d:
                        print("right")
                        player_1.right_move = True
                    case pygame.K_z:
                        if player_1.on_ground:
                            print("jump")
                            player_1.jump = True
            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_a:
                        player_1.left_move = False
                    case pygame.K_d:
                        player_1.right_move = False
        
        # Update l'affichage du sprite & de l'écran
        player_1.draw()
        pygame.display.update()