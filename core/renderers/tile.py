import pygame
from ..renderer import Renderer
from ..components.tile_map import TileMap
from ..colors import white


class TileRenderer(Renderer):
    def render(self, screen, entity):
        tile_map = entity.get_component(TileMap)
        if tile_map is None:
            return

        screen.set_colorkey(white)

        tiles = tile_map.tiles
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                tile = tiles[y][x]
                image = pygame.Surface((tile.rect.width, tile.rect.height))
                tile.render(image, entity)
                screen.blit(image, tile.rect)
