import pygame
from core.entity import Entity
from core.game import Game
from core.components.transform import TransformComponent
from core.components.tile_map import TileMap
from core.components.tile_loader import TileLoader
from core.components.exit_on_escape import ExitOnEscape
from core.components.renderer_component import RendererComponent
from core.components.move import MoveComponent
from core.components.key_control import KeyControlComponent
from core.components.collisions.tile_map_collsion import TileMapCollisionHandler
from core.components.collisions.screen_bounds_collsion import ScreenBoundsCollisionHandler
from core.renderers.tile import TileRenderer
from core.renderers.text import TextRenderer

from .tiles.air import AirTile
from .tiles.grass import GrassTile
from .tiles.finish import FinishTile
from .components.reset_game import ResetGameComponent
from .components.map_swap import MapSwap
from .components.hide_on_key import HideOnKeyComponent
from .components.reset_when_swap_and_collide import ResetWhenSwapAndCollideComponent
from .renderers.smile import SmileRenderer


class SmileDimensions:
    @staticmethod
    def start():
        key_bindings = [[pygame.K_a], [pygame.K_d], [pygame.K_w], [pygame.K_s]]

        pygame.init()

        size = width, height = (640, 480)
        game = Game(size)

        game.add_component(ExitOnEscape())

        scene = game.scene

        map1 = "G      GGG\n         G\nGGGGGGG  G\n         F"
        map2 = "GGGGGGGG G\nG         \nGGGGGGGG G\n         G"
        tiles = {" ": AirTile, "G": GrassTile, "F": FinishTile}

        tile_map = Entity()
        player = Entity()

        scene.add_entity(tile_map)
        tile_map.add_component(TransformComponent(pygame.Rect(0, 0, width, height)))
        tile_map.add_component(TileMap())
        tile_map.add_component(TileLoader(map1, tiles))
        tile_map.add_component(MapSwap(pygame.K_f, map1, map2, tiles, [tile_map, player]))
        tile_map.add_component(RendererComponent(TileRenderer()))

        scene.add_entity(player)
        player.add_component(TransformComponent(pygame.Rect(width // 2, height // 2, 50, 50)))
        player.add_component(MoveComponent(1, 4))
        player.add_component(ScreenBoundsCollisionHandler(pygame.Rect(0, 0, width, height)))
        player.add_component(TileMapCollisionHandler(tile_map.get_component(TileMap), {AirTile}))
        player.add_component(KeyControlComponent(key_bindings))
        player.add_component(RendererComponent(SmileRenderer()))
        player.add_component(ResetWhenSwapAndCollideComponent(tile_map))

        game.add_component(ResetGameComponent(tile_map, player))

        start_text = Entity()
        scene.add_entity(start_text)
        start_text.add_component(TransformComponent(pygame.Rect(width // 2 - 200, height // 2, 400, 50)))
        start_text.add_component(RendererComponent(TextRenderer("Smile Dimensions", 40)))

        controls_text = "WASD - to move, F - swap dimension, Enter - continue"
        controls = Entity()
        scene.add_entity(controls)
        controls.add_component(TransformComponent(pygame.Rect(width // 2 - 200, height // 2 + 50, 400, 20)))
        controls.add_component(RendererComponent(TextRenderer(controls_text, 14)))

        rules = "If you collide with wall in other dimension, game will be reset"
        rules_text = Entity()
        scene.add_entity(rules_text)
        rules_text.add_component(TransformComponent(pygame.Rect(width // 2 - 220, height // 2 + 70, 450, 20)))
        rules_text.add_component(RendererComponent(TextRenderer(rules, 14)))

        game.add_component(HideOnKeyComponent([start_text, controls, rules_text], pygame.K_RETURN))

        game.run()
