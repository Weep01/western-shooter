import pygame
from pygame.locals import *
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    # Attribution des caractéristiques du sprite "joueur"
    def __init__(self, x, y, player_id):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.flip = False
        self.left_move = False
        self.right_move = False
        if player_id == 1:
            self.image = pygame.image.load('Images/Assets/char_1.png')
            self.image2 = pygame.image.load('Images/0x72_16x16DungeonTileset.v4.png')
        else: 
            self.image = pygame.image.load('Images/Assets/char_1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y+280)
        self.speed = 6
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.on_ground = True
        self.jump = False
        self.jump_force = 25
        self.gravity = 2

        self.fire = False
        self.all_projectiles = pygame.sprite.Group()
    
    # Fonction d'affichage du sprite en prenant en compte le sens (flip)
    def draw(self):
        from main import screen
        screen.blit(pygame.transform.flip(self.image, not self.flip, False), self.rect)

    # Fonction d'application du mouvement du joueur
    def move(self):
        mouv_x = mouv_y = 0

        # MOUVEMENT GAUCHE
        if self.left_move:
            mouv_x = -self.speed
            self.flip = True
            self.direction = -1
        # MOUVEMENT DROITE
        if self.right_move:
            mouv_x = self.speed
            self.flip = False
            self.direction = 1
        
        # MOUVEMENT SAUT
        if self.on_ground and self.jump:
            self.vitesse_y = self.jump_force
            self.jump = False
            self.on_ground = False

        #TIRE PROJECTILE non fonctionnelle
        if self.fire :
            print("on fire")
            self.all_projectiles.add(Projectile(self))
            self.fire = False

        # CHECK COLLISION BORDURE
        # BORDURE GAUCHE
        if self.rect.center[0] - (self.width/2) < 0:
            if self.flip:
                print("yes")
                print(self.rect.center[0])
                self.rect.x -= mouv_x
        # BORDURE DROITE
        if self.rect.center[0] + (self.width/2) > 1280:
            if not self.flip:
                print("yes")
                print(self.rect.center[0])
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

