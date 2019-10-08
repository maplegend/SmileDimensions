import pygame
from core.tile import Tile
from core.colors import yellow


class FinishTile(Tile):
    def render(self, screen, entity):
        pygame.draw.rect(screen, yellow, screen.get_rect())
