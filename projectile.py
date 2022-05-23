import pygame
from math import *

#definir class projectile
class Projectile(pygame.sprite.Sprite):
    #def constructeur classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.v0 = player.power #la valeur devra changer plus tard
        self.num = player.id
        self.alpha = radians(45)
        if player.flip == False:
            self.flip = 1
        else: 
            self.flip = -1
            
        self.player = player
        self.image = pygame.image.load('Images/assets/bullet.png').convert()
        #modif taille
        self.image = pygame.transform.scale(self.image, (30,30))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
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
        print(self.num,self.v0)
        self.rect.x = self.flip*cos(self.alpha)*self.v0*self.t +self.constx
        self.rect.y = -(-(1/2)*9.81*(self.t**2)  +  sin(self.alpha)*self.v0*self.t )+self.consty
        #print("y = ",-(self.rect.y-404),"x = ",self.rect.x)
        #verif si projectile touche monstre


       #IL MANQUE UNE PARTIE DU CODE PRESENT DANS L ANCIENNE VERSION DE LOUIS

        #si projec hors ecran
        if  0> self.rect.x or self.rect.x  > 1280 or self.rect.y>2000:
            #sup projec
            self.remove()
          


    def draw(self):
        from main import screen
        screen.blit(screen,(self.rect.x,self.rect.y))
