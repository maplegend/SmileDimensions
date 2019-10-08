import pygame
from ..component import Component
from .transform import TransformComponent
from ..events.update import UpdateEvent
from .collision_handler import CollisionsHandler


class MoveComponent(Component):
    def __init__(self, acceleration, max_speed, normalize=True):
        super().__init__()
        self.velocity = pygame.Vector2()
        self.direction = pygame.Vector2()
        self.acceleration = acceleration
        self.max_speed = max_speed
        self.entity = None
        self.normalize = normalize

    def set_direction(self, x, y):
        self.direction = pygame.Vector2(x, y)

    def add_direction(self, x, y):
        self.direction += pygame.Vector2(x, y)

    def update(self, event):
        trans = self.entity.get_component(TransformComponent)
        if not trans:
            return

        if self.normalize and self.direction.magnitude() != 0:
            self.direction.normalize_ip()

        if self.direction.magnitude() == 0:
            self.velocity = pygame.Vector2()
        elif (self.velocity + self.direction*self.acceleration).magnitude() > self.max_speed:
            self.velocity = self.direction*self.max_speed
        else:
            self.velocity += self.direction * self.acceleration

        new_rect = trans.rect.move(self.velocity)
        collide = False
        col_handlers = self.entity.get_components(CollisionsHandler)
        if col_handlers is not None:
            for col in col_handlers:
                collide = collide or col.detect_collision(self.entity, new_rect)

        if not collide:
            trans.rect = new_rect
        self.direction *= 0

    def applied_on_entity(self, entity):
        self.entity = entity
        event_manager = entity.scene.game.event_manager
        event_manager.bind(UpdateEvent, self.update)
