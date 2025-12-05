import pygame
from constants import SCREEN_WIDTH,SCREEN_HEIGHT,DIMENSIONS
from logger import log_state

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DIMENSIONS) 
        self.running = True
    
    def run(self):

        while self.running:
            # Log the state for debugging
            log_state()
            screen = self.screen
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")
            pygame.display.update()
        
        #To Properly close pygame and free resources
        pygame.quit()

        

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    Game().run()


if __name__ == "__main__":
    main()
