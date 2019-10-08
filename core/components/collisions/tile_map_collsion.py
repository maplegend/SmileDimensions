from ..collision_handler import CollisionsHandler


class TileMapCollisionHandler(CollisionsHandler):
    def __init__(self, tile_map, collisions_tiles):
        super().__init__()
        self.col_tiles = collisions_tiles
        self.tile_map = tile_map

    def detect_collision(self, entity, new_rect):
        tiles = self.tile_map.get_tiles_around((new_rect.x, new_rect.y))
        if tiles is None:
            return False

        for tile in tiles:
            if tile.__class__ in self.col_tiles:
                if tile.rect.colliderect(new_rect):
                    return True
        return False
