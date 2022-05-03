import pygame

#definir class projectile
class Projectile(pygame.sprite.Sprite):
    #def constructeur classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/bullet.png')
        #modif taille
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y + 5

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        #verif si projectile touche monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            #sup projectile
            self.remove()
            #infliger degats
            monster.damage(self.player.attack)

        #si projec hors ecran
        if self.rect.x > 1080:
            #sup projec
            self.remove()



