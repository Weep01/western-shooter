import pygame

from projectile import Projectile

#classe joueur
class Player(pygame.sprite.Sprite) :

    def __init__(self, game):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.image = pygame.image.load('assets/personnage.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 400
        self.all_projectiles = pygame.sprite.Group()


    def launch_projectile(self):
        #creer instance projectile
        self.all_projectiles.add(Projectile(self))



    def move_right(self):
        #si joueur pas collision avec joueur2
        if not self.game.check_collision(self, self.game.player2):
            self.rect.x += self.velocity

    def move_left(self):
        if not self.game.check_collision(self, self.game.player2):
            self.rect.x -= self.velocity



