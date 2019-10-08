from ..component import Component
from .tile_map import TileMap


class TileLoader(Component):
    def __init__(self, map_string, tiles_dictionary):
        super().__init__()
        self.map_string = map_string
        self.tiles_dictionary = tiles_dictionary

    def applied_on_entity(self, entity):
        tile_map = entity.get_component(TileMap)
        if tile_map is None:
            return False

        tiles = [[]]
        r = 0
        for c in self.map_string:
            if c == "\n":
                r += 1
                tiles.append([])
            elif c in self.tiles_dictionary:
                tiles[r].append(self.tiles_dictionary[c]())
            else:
                tiles[r].append(self.tiles_dictionary[" "]())

        tile_map.tiles = tiles
        tile_map.calculate_rects()