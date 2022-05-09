from turtle import screensize
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
        self.image = pygame.image.load('Images/assets/bullet.png').convert()
        #modif taille
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 80
        self.rect.y = player.rect.y + 5
        self.constx = self.rect.x
        self.consty = self.rect.y
        #timer
        self.staticpoint = pygame.time.get_ticks() #temps en ms ou le missile à été lancé

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        from main import screen
        self.t = (pygame.time.get_ticks()-self.staticpoint) /100 # temps t apres missile soit lancé en seconde
        #print(self.t)
        self.rect.x = cos(self.alpha)*self.v0*self.t +self.constx
        self.rect.y = -(-(1/2)*9.81*(self.t**2)  +  sin(self.alpha)*self.v0*self.t )+self.consty
        #print("y = ",-(self.rect.y-404),"x = ",self.rect.x)
        #verif si projectile touche monstre


    

        #si projec hors ecran
        if  0> self.rect.x or self.rect.x  > 1280 or self.rect.y>2000:
            #sup projec
            self.remove()
          


    def draw(self):
        from main import screen
        screen.blit(screen,(self.rect.x,self.rect.y))
