import pygame
from ..component import Component
from .transform import TransformComponent


class TileMap(Component):
    def __init__(self):
        super().__init__()
        self.tiles = []
        self.tile_size = None
        self.entity = None

    def calculate_rects(self):
        rect = self.entity.get_component(TransformComponent).rect
        if not self.tiles:
            return
        tile_width, tile_height = (rect.width / len(self.tiles[0]), rect.height / len(self.tiles))
        self.tile_size = (tile_width, tile_height)
        for y in range(len(self.tiles)):
            for x in range(len(self.tiles[y])):
                self.tiles[y][x].rect = pygame.Rect((x*tile_width, y*tile_height, tile_width, tile_height))

    def applied_on_entity(self, entity):
        self.entity = entity
        self.calculate_rects()

    def get_tiles_around(self, pos):
        if pos[0] < 0 or pos[1] < 0:
            return None
        if self.tile_size is None:
            return None

        start_pos = (int(pos[0]/self.tile_size[0]), int(pos[1]/self.tile_size[1]))
        res_tiles = [self.tiles[start_pos[1]][start_pos[0]]]
        dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in dirs:
            if 0 <= start_pos[0] + d[0] < len(self.tiles[0]) and 0 <= start_pos[1] + d[1] < len(self.tiles):
                res_tiles.append(self.tiles[start_pos[1] + d[1]][start_pos[0] + d[0]])
        return res_tiles
