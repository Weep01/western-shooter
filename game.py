from pickle import TRUE
import pygame
from player import Player

class Game:
    def __init__(self):
        self.is_playing = False
        self.players = pygame.sprite.Group()
        self.player_1 = Player(240, 200, 1)
        self.player_2 = Player(1064, 200, 2)
        self.players.add(self.player_1)
        self.players.add(self.player_2)
        self.pressed = {}
        self.background = pygame.image.load('Images/assets/game_background.png')
        self.mort_background = pygame.image.load('Images/assets/Cadre_victoire.png')
        self.mort_background = pygame.transform.scale(self.mort_background, (1000,500))

        self.mort_blue = pygame.image.load('Images/assets/win_blue.png')
        self.mort_blue = pygame.transform.scale(self.mort_blue, (600,300))
        self.mort_red = pygame.image.load('Images/assets/win_red.png')
        self.mort_red = pygame.transform.scale(self.mort_red, (600,300))
        self.press = False
        self.press2 = False
        
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
        screen.blit(self.background, (0, 0))

        self.get_input()

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
        # PLAYER 1 TIRE
        if self.pressed.get(pygame.K_SPACE):
            self.press = True
        else:
            self.player_1.fire = False
        if (self.press and self.pressed.get(pygame.K_SPACE)==False ):
            self.player_1.fire = TRUE
            self.press = False
        
        # PLAYER 2 TIRE
        if self.pressed.get(pygame.K_KP0):
            self.press2 = True
        else:
            self.player_2.fire = False
        if (self.press2 and self.pressed.get(pygame.K_KP0)==False ):
            self.player_2.fire = True
            self.press2 = False
            
        
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
            # Actualisation de la force de joueur 1

            if self.pressed.get(pygame.K_SPACE):
                if  self.player_1.power < self.player_1.max_power:
                    self.player_1.power += 1
            self.player_1.update_power_bar(screen)
            if self.pressed.get(pygame.K_SPACE)!= True:
                self.player_1.power = 0
            # JOUEUR 2
            if self.pressed.get(pygame.K_KP0):
                if  self.player_2.power < self.player_2.max_power:
                    self.player_2.power += 1
            self.player_2.update_power_bar(screen)
            if self.pressed.get(pygame.K_KP0)!= True:
                self.player_2.power = 0            


            player.all_projectiles.draw(screen)
            for projectile in self.player_1.all_projectiles: # probleme
                projectile.move()
                if projectile.rect.colliderect(self.player_2.rect):
                    self.player_2.attack()
                    projectile.kill()

            for projectile in self.player_2.all_projectiles: # probleme
                projectile.move()
                if projectile.rect.colliderect(self.player_1.rect):
                    self.player_1.attack()
                    projectile.kill()
            if self.player_1.health <= 0:
                print("joueur 1 mort")
                screen.blit(self.mort_background, (150, 100))
                screen.blit(self.mort_red,(350, 200))
                self.player_1.kill()
            if self.player_2.health <= 0:
                self.player_2.kill()
                screen.blit(self.mort_background, (150, 100))
                screen.blit(self.mort_blue,(350, 200))
                #screen.blit(self.background, (0, 0))
                print("joueur 2 mort")
        clock.tick(60)
        pygame.display.update()
    
    def start(self, screen):
        clock = pygame.time.Clock()

        self.is_playing = True
        while self.is_playing:
            self.update(screen, clock)