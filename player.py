import pygame

from projectile import Projectile

#classe joueur
class Player(pygame.sprite.Sprite) :

    def __init__(self, game):
        super().__init__()
        self.game = game
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
        # si joueur pas collision avec monstre
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self, surface):
        # definir couleur barre ( htmlcolorcodes.com)
        bar_color = (250, 68, 29)

        # def position et aspect de la barre
        bar_position = [self.rect.x, self.rect.y - 10, self.health, 5]

        # dessiner barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)

