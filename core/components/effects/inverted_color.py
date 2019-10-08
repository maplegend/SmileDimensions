import pygame
from ..renderer_effect import RendererEffect
from ..renderer_component import RendererComponent


class InvertColorEffect(RendererEffect):
    def process(self, img):
        inv = pygame.Surface(img.get_rect().size, pygame.SRCALPHA)
        inv.fill((255, 255, 255, 255))
        inv.blit(img, (0, 0), None, pygame.BLEND_RGB_SUB)
        return inv

    def applied_on_entity(self, entity):
        entity.get_component(RendererComponent).need_redraw = True
