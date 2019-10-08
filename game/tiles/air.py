from core.tile import Tile
from core.colors import white


class AirTile(Tile):
    def render(self, screen, entity):
        screen.fill(white)
