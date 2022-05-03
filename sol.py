import pygame

class Sol(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.rect = pygame.rect(0,470,1080,170)

    def afficher(self, surface):
        couleur_sol = (255, 68, 29)

        # def position et aspect de la barre
        sol_position = [0, 1080, 1100, 300]

        # dessiner barre de vie
        pygame.draw.rect(surface, couleur_sol, sol_position)
        
