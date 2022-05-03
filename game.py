import pygame
from player import Player
from player2 import Player2
#creer classe jeu
class Game:
     def __init__(self):
         #generer notre joueur
        self.player = Player()
        self.pressed = {}
        self.player2 = Player2()

     def check_collision(self, sprite, group):
         return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


