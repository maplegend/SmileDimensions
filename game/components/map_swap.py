from core.component import Component
from core.components.tile_loader import TileLoader
from core.components.renderer_component import RendererComponent
from core.components.effects.inverted_color import InvertColorEffect
from core.events.key_press import KeyPressEvent
from ..events.map_swap import MapSwapEvent


class MapSwap(Component):
    def __init__(self, key, map1, map2, tiles, invert_entities):
        super().__init__()
        self.key = key
        self.map1 = map1
        self.map2 = map2
        self.current_map = 0
        self.tiles = tiles
        self.entity = None
        self.invert_entities = invert_entities

    def swap(self):
        self.current_map ^= 1
        self.entity.remove_component(TileLoader)
        self.entity.add_component(TileLoader(self.map1 if self.current_map == 0 else self.map2, self.tiles))
        self.entity.get_component(RendererComponent).need_redraw = True

        for ent in self.invert_entities:
            if self.current_map == 1:
                ent.add_component(InvertColorEffect())
            else:
                ent.remove_component(InvertColorEffect)
            ent.get_component(RendererComponent).need_redraw = True
        self.entity.scene.game.event_manager.trigger_event(MapSwapEvent())

    def key_pressed(self, key):
        if key.key == self.key:
            self.swap()

    def applied_on_entity(self, entity):
        self.entity = entity
        event_manager = entity.scene.game.event_manager
        event_manager.bind(KeyPressEvent, self.key_pressed)
