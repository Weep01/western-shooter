import pygame
from main_menu import *
from functions import *







BLACK = (0,0,0)
clock = pygame.time.Clock()


class exit_button:
            def __init__(self):
                self.x = 10
                self.y = 620
                self.unpressed = pygame.image.load('Images\menu\quit_button.png')

               
icon = pygame.image.load('Images\menu\quit_button.png') 
pygame.display.set_icon(icon)  

button_list = [exit_button]

def credits_menu(screen):
    while True:
        screen.fill(BLACK)


        mouse_x, mouse_y = mouse_get()


        screen.blit(icon,(10,620))
        for i in button_list:
            temp = i()
            if temp.unpressed.get_rect().collidepoint(mouse_x - temp.x, mouse_y - temp.y):
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if (i == exit_button):
                            main_menu_func()
                        




                screen.blit(temp.pressed, (temp.x, temp.y))
            else:
                screen.blit(temp.unpressed, (temp.x, temp.y))





        # SI BOUTON CLIQUE
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                            

        

        pygame.display.update()
        clock.tick(60)
        
        
        
        
