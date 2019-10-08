from ..component import Component


class TransformComponent(Component):
    def __init__(self, rect):
        super().__init__()
        self.rect = rect
