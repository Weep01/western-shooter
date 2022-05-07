import pygame
from math import *
#definir class projectile
class Projectile(pygame.sprite.Sprite):
    #def constructeur classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.v0 = 100 #la valeur devra changer plus tard
        self.alpha = radians(45)
        self.player = player
        self.image = pygame.image.load('assets/bullet.png')
        #modif taille
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y + 5
        self.staticpoint = pygame.time.get_ticks() #temps en ms ou le missile à été lancé

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):

        self.t = (pygame.time.get_ticks()-self.staticpoint) /100 # temps t ou apres que le missile soit lancé en seconde
        print(self.t)
        self.rect.x = cos(self.alpha)*self.v0*self.t +self.player.rect.x
        self.rect.y = -(-(1/2)*9.81*(self.t**2)  +  sin(self.alpha)*self.v0*self.t )+self.player.rect.y #l'axe y est à l'envers dans pygame je ne met dans pas de - au debut de la formule
        print("y = ",-(self.rect.y-404),"x = ",self.rect.x)
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



