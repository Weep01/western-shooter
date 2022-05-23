import pygame
from pygame.locals import *
from projectile import Projectile
import time 

class Player(pygame.sprite.Sprite):

    # Attribution des caractéristiques du sprite "joueur"
    def __init__(self, x, y, player_id):
        pygame.sprite.Sprite.__init__(self)
        self.max_health = 100
        self.health = 100
        self.left_move = False
        self.right_move = False
        self.id = player_id
        if player_id == 1:
            self.image = pygame.image.load('Images/assets/blue_char.png')
            self.flip = True
        else: 
            self.image = pygame.image.load('Images/assets/red_char.png')
            self.flip = False
        self.rect = self.image.get_rect()
        self.rect.center = (x, y+280)
        self.speed = 7
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.on_ground = True
        self.jump = False
        self.jump_force = 30
        self.gravity = 1.5
        self.power = 100
        self.max_power = 100

        self.projectile_cooldown = False # est ce que l'arme est en cooldown
        self.fire = False
        self.all_projectiles = pygame.sprite.Group()

    # Fonction d'affichage du sprite en prenant en compte le sens (flip)
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, not self.flip, False), self.rect)
    
    # Fonction d'application du mouvement du joueur
    def move(self):
        mouv_x = mouv_y = 0

        # MOUVEMENT GAUCHE
        if self.left_move:
            mouv_x = -self.speed
            self.flip = False
            self.direction = -1
        # MOUVEMENT DROITE
        if self.right_move:
            mouv_x = self.speed
            self.flip = True
            self.direction = 1
        
        # MOUVEMENT SAUT
        if self.on_ground and self.jump:
            self.vitesse_y = self.jump_force
            self.jump = False
            self.on_ground = False

        #TIRE PROJECTILE non fonctionnelle
        if self.fire :
            #self.fire = False
            self.all_projectiles.add(Projectile(self))



        # CHECK COLLISION BORDURE
        # BORDURE GAUCHE
        if self.rect.center[0] - (self.width/2) < 40:
            if not self.flip:
                self.rect.x -= mouv_x
        # BORDURE DROITE
        if self.rect.center[0] + (self.width/2) > 1240:
            if self.flip:
                self.rect.x -= mouv_x
        
        # APPLICATION GRAVITE
        if not self.on_ground:
            mouv_y = -self.vitesse_y
            self.vitesse_y -= self.gravity

        # CONTACT AU SOL
        if self.rect.bottom + mouv_y > 550:
                self.on_ground = True
                self.vitesse_y = 0

        # APPLICATION DU MOUVEMENT SUR LE JOUEUR
        self.rect.x += mouv_x
        self.rect.y += mouv_y

        


    def update_health_bar(self, screen):
        # definir couleur barre ( htmlcolorcodes.com)
        bar_color = (250, 68, 29)

        # def position et aspect de la barre
        bar_position = [self.rect.x - 10, self.rect.y - 10, self.health, 5]

        # dessiner barre de vie
        pygame.draw.rect(screen, bar_color, bar_position)
    def update_power_bar(self,screen):


        #dessine bar de puissance

        bar_color2=(0,51,255)
        bar_position2 = [self.rect.x - 10 , self.rect.y -30, self.power, 5]
        pygame.draw.rect(screen,bar_color2,bar_position2)
    
    def attack(self):
        self.health -= 20
    