import pygame
from ..component import Component


class RendererComponent(Component):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer
        self.image = None
        self.need_redraw = True

    def render(self, rect, ent):
        if self.renderer.rendering_size is None:
            self.renderer.rendering_size = (rect.width, rect.height)
        self.image = pygame.Surface(self.renderer.rendering_size)
        self.renderer.render(self.image, ent)
        self.image = pygame.transform.scale(self.image, (rect.width, rect.height))
