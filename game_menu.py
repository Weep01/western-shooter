from main_menu import *

def game_menu(screen):
    clock = pygame.time.Clock()

    while True:
        screen.fill((0,0,0))
        # EVENT
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        
        pygame.display.update()
        clock.tick(60)
