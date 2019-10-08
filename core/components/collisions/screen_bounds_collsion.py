from ..collision_handler import CollisionsHandler


class ScreenBoundsCollisionHandler(CollisionsHandler):
    def __init__(self, bounds):
        super().__init__()
        self.bounds = bounds

    def detect_collision(self, entity, new_rect):
        return not self.bounds.contains(new_rect)
