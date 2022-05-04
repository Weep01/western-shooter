from functions import *
from game_menu import game_menu

def main_menu(screen):
    class button:
        class play_button:
            def __init__(self):
                self.x = 500
                self.y = 250
                self.pressed = pygame.image.load('Images/Buttons/play.pressed.png')
                self.unpressed = pygame.image.load('Images/Buttons/play.unpressed.png')
        class credits_button:
            def __init__(self):
                self.x = 1095
                self.y = 620
                self.pressed = pygame.image.load('Images/Buttons/info.pressed.png')
                self.unpressed = pygame.image.load('Images/Buttons/info.unpressed.png')
        class stop_button:
            def __init__(self):
                self.x = 10
                self.y = 620
                self.pressed = pygame.image.load('Images/Buttons/stop.pressed.png')
                self.unpressed = pygame.image.load('Images/Buttons/stop.unpressed.png')

    
    icon = pygame.image.load('Images/Buttons/stop.unpressed.png')
    pygame.display.set_icon(icon)

    menu_background = pygame.image.load('Images/Buttons/menu_background.png')

    button_list = [button.play_button, button.credits_button, button.stop_button]

    clock = pygame.time.Clock()

    font = pygame.font.SysFont(None, 100)

    while True:
        screen.blit(menu_background, (0, 0))
        draw_text('Projet Transverse', font, (255, 255, 255), screen, 350, 100)

        mouse_x, mouse_y = mouse_get()

        # HOVER ANIMATION
        for i in button_list:
            temp = i()
            if temp.unpressed.get_rect().collidepoint(mouse_x - temp.x, mouse_y - temp.y):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if (i == button.stop_button):
                        pygame.quit()
                        exit()
                    if (i == button.play_button):
                        game_menu(screen)
                        return
                screen.blit(temp.pressed, (temp.x, temp.y))
            else:
                screen.blit(temp.unpressed, (temp.x, temp.y))
    
        # EVENT
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        
        pygame.display.update()
        clock.tick(60)




# MOUSE
#if button.x < mouse_pos[0] < button.x+button.width and button.y < mouse_pos[1] < button.y+button.height:
#    screen.blit(button.play_pressed, (button.x,button.y))
#else:
#    screen.blit(button.play_unpressed, (button.x,button.y))
# PLAY BUTTON DRAW
#pygame.draw.rect(screen, button.bgcolor, pygame.Rect(button.x, button.y, button.width, button.height))
#pygame.draw.rect(screen, button.color, pygame.Rect(button.x+button.gap, button.y+button.gap, button.width-button.gap*2, button.height-button.gap*2))