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
        self.mort_background = pygame.transform.scale(pygame.image.load('Images/assets/Cadre_victoire.png'), (1000,500))

        self.mort_blue = pygame.transform.scale(pygame.image.load('Images/assets/win_blue.png'), (600,300))
        self.mort_red = pygame.transform.scale(pygame.image.load('Images/assets/win_red.png'), (600,300))
        self.press = False
        self.press2 = False
        
    def get_input(self):
        for event in pygame.event.get():
            #verifier fermeture fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
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
            self.player_2.right_move = True
        else:
            self.player_2.right_move = False
        if self.pressed.get(pygame.K_LEFT):
            self.player_2.left_move = True
        else:
            self.player_2.left_move = False
        if self.pressed.get(pygame.K_UP):
            self.player_2.jump = True
        else:
            self.player_2.jump = False


        if self.pressed.get(pygame.K_s):
            self.press = True
        else:
            self.player_1.fire = False
        if (self.press and self.pressed.get(pygame.K_s)==False ):
            self.player_1.fire = True
            self.press = False
        
        # PLAYER 2 TIRE
        if self.pressed.get(pygame.K_DOWN):
            self.press2 = True
        else:
            self.player_2.fire = False
        if (self.press2 and self.pressed.get(pygame.K_DOWN)==False ):
            self.player_2.fire = True
            self.press2 = False
            
        
        if self.pressed.get(pygame.K_d):
            self.player_1.right_move = True
        else:
            self.player_1.right_move = False
        if self.pressed.get(pygame.K_q):
            self.player_1.left_move = True
        else:
            self.player_1.left_move = False
        if self.pressed.get(pygame.K_z):
            self.player_1.jump = True
        else:
            self.player_1.jump = False
        #if self.pressed.get(pygame.K_s):
        #    self.player_2.launch_projectile()

        for player in self.players:
            # Actualisation de la position des joueurs
            player.move()
            # Affichage des joueurs
            player.draw(screen)
            # Actualisation de la force de joueur 1

            if self.pressed.get(pygame.K_s):
                if self.player_1.power < self.player_1.max_power:
                    self.player_1.power += 1
            self.player_1.update_power_bar(screen)


            # JOUEUR 2
            if self.pressed.get(pygame.K_DOWN):
                if self.player_2.power < self.player_2.max_power:
                    self.player_2.power += 1
            self.player_2.update_power_bar(screen)
         




            player.all_projectiles.draw(screen)
            for projectile in self.player_1.all_projectiles: 
                projectile.move()
                if projectile.rect.colliderect(self.player_2.rect):
                    self.player_2.attack()
                    projectile.kill()

            for projectile in self.player_2.all_projectiles: 
                projectile.move()
                if projectile.rect.colliderect(self.player_1.rect):
                    self.player_1.attack()
                    projectile.kill()
 
            # Actualisation de la barre de vie
            if player.health >= 66:
                screen.blit(player.health_bar[0], player.health_bar_pos)
            elif player.health >= 33:
                screen.blit(player.health_bar[1], player.health_bar_pos)
            elif player.health > 0:
                screen.blit(player.health_bar[2], player.health_bar_pos)
            elif player.health == 0:
                screen.blit(player.health_bar[3], player.health_bar_pos)
            
            # Affichage du logo du joueur
            screen.blit(player.logo, player.logo_pos)
    
            if self.player_1.health <= 0:
                from main_menu import main_menu_func
                self.player_1.kill()
                self.player_2.kill()
                screen.blit(self.mort_background, (150, 100))
                screen.blit(self.mort_blue,(350, 200))
                main_menu_func(screen)
            if self.player_2.health <= 0:
                from main_menu import main_menu_func
                self.player_1.kill()
                self.player_2.kill()
                screen.blit(self.mort_background, (150, 100))
                screen.blit(self.mort_red,(350, 200))
                main_menu_func(screen)
        
        clock.tick(60)
        pygame.display.update()
    
    def start(self, screen):
        clock = pygame.time.Clock()

        self.is_playing = True
        while self.is_playing:
            self.update(screen, clock)