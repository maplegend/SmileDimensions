from abc import ABC
from ..component import Component


class CollisionsHandler(Component, ABC):
    @staticmethod
    def detect_collision(self, entity, new_rect):
        pass
