import pygame
from player import *
from monster import *
from sol import *
#creer classe jeu
class Game:

    def __init__(self):
        #definir si le jeu à commencé ou non
        self.is_playing = False
        #generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.monster = Monster(self)
        self.all_monster.add(self.monster)




    def update(self, screen):
        # recup projec joueurs
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recup monstre jeu
        for monster in self.all_monster:
            # monster.forward()
            monster.update_health_bar(screen)

        # appliquer image joueur
        screen.blit(self.player.image, self.player.rect)

        screen.blit(self.monster.image, self.monster.rect)

        # limite ecran + mouvement joueur
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1020:
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -5:
            self.player.move_left()

        # limite ecran + deplacement monstre
        if self.pressed.get(pygame.K_d) and self.monster.rect.x < 980:
            self.monster.move_right_monster()
        if self.pressed.get(pygame.K_q) and self.monster.rect.x > -5:
            self.monster.move_left_monster()

        # appliquer image projectile
        self.player.all_projectiles.draw(screen)

        for player in self.all_players:
            player.update_health_bar(screen)
        print(self.player.rect.x)



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        #self.all_monster.add(monster)




