import pygame
from math import *

#definir class projectile
class Projectile(pygame.sprite.Sprite):
    #def constructeur classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.v0 = player.power
        self.num = player.id
        self.alpha = radians(45)
        if player.flip == False:
            self.flip = -1
        else: 
            self.flip = 1
            
        self.player = player
        if player.id == 1 :
            self.image = pygame.image.load('Images/assets/red_bullet.png')
        else:
            self.image = pygame.image.load('Images/assets/blue_bullet.png')
        #modif taille
        self.rect = self.image.get_rect()
        if player.flip:
            self.rect.x = player.rect.x + 140
        else:
            self.rect.x = player.rect.x - 15
        self.rect.y = player.rect.y + 20
        self.constx = self.rect.x
        self.consty = self.rect.y
        #timer
        self.staticpoint = pygame.time.get_ticks() #temps en ms ou le missile à été lancé

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.t = (pygame.time.get_ticks()-self.staticpoint) /100 # temps t apres missile soit lancé en seconde
        self.rect.x = self.flip*cos(self.alpha)*self.v0*self.t +self.constx
        self.rect.y = -(-(1/2)*9.81*(self.t**2)  +  sin(self.alpha)*self.v0*self.t )+self.consty
        #print("y = ",-(self.rect.y-404),"x = ",self.rect.x)
        #verif si projectile touche monstre


       #IL MANQUE UNE PARTIE DU CODE PRESENT DANS L ANCIENNE VERSION DE LOUIS

        #si projec hors ecran
        if  0> self.rect.x or self.rect.x  > 1280 or self.rect.y>550:
            #sup projec
            self.kill()
          


    def draw(self):
        from main import screen
        screen.blit(screen,(self.rect.x,self.rect.y))

