import pygame
from core.tile import Tile
from core.colors import green


class GrassTile(Tile):
    def render(self, screen, entity):
        pygame.draw.rect(screen, green, screen.get_rect())
