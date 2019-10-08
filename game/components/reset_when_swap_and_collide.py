from core.component import Component
from core.components.transform import TransformComponent
from core.components.collisions.tile_map_collsion import TileMapCollisionHandler
from .fade_animation import FadeAnimationComponent
from ..events.map_swap import MapSwapEvent
from ..events.reset_game import ResetGameEvent


class ResetWhenSwapAndCollideComponent(Component):
    def __init__(self, tile_map):
        super().__init__()
        self.entity = None
        self.tile_map = tile_map

    def on_swap(self, _):
        p_rect = self.entity.get_component(TransformComponent).rect
        if self.entity.get_component(TileMapCollisionHandler).detect_collision(self.tile_map, p_rect):
            anim = FadeAnimationComponent()
            self.tile_map.add_component(anim)
            anim.animate(lambda: self.entity.scene.game.event_manager.trigger_event(ResetGameEvent()))

    def applied_on_entity(self, entity):
        self.entity = entity
        event_manager = entity.scene.game.event_manager
        event_manager.bind(MapSwapEvent, self.on_swap)
