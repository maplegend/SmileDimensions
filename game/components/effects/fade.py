import pygame
from core.components.renderer_effect import RendererEffect


class FadeEffect(RendererEffect):
    def __init__(self):
        super().__init__()
        self.strength = 0
        self.mode = 0

    def process(self, img):
        if self.mode == 0:
            img.set_alpha(self.strength)
        else:
            surf = pygame.Surface(img.get_size(), pygame.SRCALPHA)
            surf.fill((0, 0, 0, self.strength))
            img.blit(surf, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        return img
