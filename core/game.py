import pygame
import sys
from .entity import Entity
from .event_manager import EventManager
from .game_screen import GameScreen
from .game_renderer import GameRender
from .scene import Scene
from .events.key_press import KeyPressEvent
from .events.key_pressed import KeyPressedEvent
from .events.update import UpdateEvent


class Game(Entity):
    def __init__(self, screen_size):
        super().__init__()
        self.event_manager = EventManager()
        self.game_screen = GameScreen(screen_size)
        self.renderer = GameRender(self)
        self.scene = Scene(self)

    def game_tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.event_manager.trigger_event(KeyPressEvent(event.key))

        for i, k in enumerate(pygame.key.get_pressed()):
            if k != 0:
                self.event_manager.trigger_event(KeyPressedEvent(i))
        self.event_manager.trigger_event(UpdateEvent())
        self.renderer.draw()

    def run(self):
        clock = pygame.time.Clock()

        while 1:
            self.game_tick()
            clock.tick(60)
