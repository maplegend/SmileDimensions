import pygame


class GameScreen:
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(size)
        self.full_screen = False

    def toggle_full_screen(self):
        self.full_screen = not self.full_screen
        pygame.display.quit()
        pygame.display.init()
        if self.full_screen:
            self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.size)
