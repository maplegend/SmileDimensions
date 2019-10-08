from core.component import Component
from core.components.transform import TransformComponent
from .map_swap import MapSwap
from ..events.reset_game import ResetGameEvent


class ResetGameComponent(Component):
    def __init__(self, tile_map, player):
        super().__init__()
        self.tile_map = tile_map
        self.player = player
        self.player_pos = player.get_component(TransformComponent).rect.copy()

    def reset(self, _):
        map_swap = self.tile_map.get_component(MapSwap)
        if map_swap.current_map == 1:
            map_swap.swap()

        self.player.get_component(TransformComponent).rect = self.player_pos.copy()

    def applied_on_entity(self, entity):
        event_manager = entity.scene.game.event_manager
        event_manager.bind(ResetGameEvent, self.reset)
