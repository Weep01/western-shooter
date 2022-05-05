import pygame

# Fonction d'initialisation du programme
def init():
    screen = ""
    pygame.init()
    pygame.display.set_caption('Projet Transverse')
    screen = pygame.display.set_mode((1280, 720))
    return screen

# Fonction pour afficher un texte donné en argument
def draw_text(content, font, color, surface, x, y):
    text = font.render(content, 1, color)
    textsize = text.get_rect()
    textsize.topleft = (x, y)
    surface.blit(text, textsize)

# Fonction pour afficher la position de la souris (dev)
def mouse_get():
    x,y = pygame.mouse.get_pos()
    return x,y