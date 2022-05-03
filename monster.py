import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/player.jpg')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 400
        self.velocity = 5


    def damage(self, amount):
        #infliger des degats
        self.health -= amount

        #vefifier nb points de vie < ou = à 0
        if self.health <= 0:
            #sup entité
            self.rect.x = 15000




    def update_health_bar(self, surface):
        #definir couleur barre ( htmlcolorcodes.com)
        bar_color = (250, 68, 29)

        # def position et aspect de la barre
        bar_position= [self.rect.x, self.rect.y -10, self.health, 5]

        #dessiner barre de vie
        pygame.draw.rect(surface, bar_color, bar_position)


    #def forward(self):
        #deplacement si pas de collision
        #if not self.game.check_collision(self, self.game.all_players):
            #self.rect.x -= self.velocity

    def move_right_monster(self):
        # si joueur pas collision avec monstre
        self.rect.x += self.velocity

    def move_left_monster(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
