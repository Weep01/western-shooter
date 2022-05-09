import pygame
from player import Player

class Game:
    def __init__(self):
        self.is_playing = False
        self.players = pygame.sprite.Group()
        self.player_1 = Player(200, 200, 1)
        self.player_2 = Player(800, 200, 2)
        self.players.add(self.player_1)
        self.players.add(self.player_2)
        self.pressed = {}
    
    def get_input(self):
        for event in pygame.event.get():
            #verifier fermeture fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu !")
                exit()
            #Detecter clavier
            elif event.type == pygame.KEYDOWN:
                #Pression touche
                self.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False
    
    def update(self, screen, clock):
        screen.fill((0,0,0))

        self.get_input()

        # Dégueulasse mais j'ai pas pu faire autrement

        if self.pressed.get(pygame.K_RIGHT):
            self.player_1.right_move = True
        else:
            self.player_1.right_move = False
        if self.pressed.get(pygame.K_LEFT):
            self.player_1.left_move = True
        else:
            self.player_1.left_move = False
        if self.pressed.get(pygame.K_UP):
            self.player_1.jump = True
        else:
            self.player_1.jump = False
        #if self.pressed.get(pygame.K_DOWN):
        #    self.player_1.launch_projectile()
        if self.pressed.get(pygame.K_SPACE):
            self.player_1.fire = True
        else:
            self.player_1.fire = False

        if self.pressed.get(pygame.K_d):
            self.player_2.right_move = True
        else:
            self.player_2.right_move = False
        if self.pressed.get(pygame.K_a):
            self.player_2.left_move = True
        else:
            self.player_2.left_move = False
        if self.pressed.get(pygame.K_z):
            self.player_2.jump = True
        else:
            self.player_2.jump = False
        #if self.pressed.get(pygame.K_s):
        #    self.player_2.launch_projectile()

        for player in self.players:    
            # Actualisation de la position des joueurs
            player.move()
            # Affichage des joueurs
            player.draw(screen)
            # Actualisation de la barre de vie des joueurs
            player.update_health_bar(screen)
            # Actualisation de la force des joueurs
            if player.power == player.max_power:
                player.power = 0
            else:
                player.power += 1 
            player.update_power_bar(screen)

            player.all_projectiles.draw(screen)
            for projectile in player.all_projectiles:
                projectile.move()
        clock.tick(60)
        pygame.display.update()
    
    def start(self, screen):
        clock = pygame.time.Clock()

        self.is_playing = True
        while self.is_playing:
            self.update(screen, clock)