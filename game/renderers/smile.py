import pygame
from math import pi
from core.renderer import Renderer
from core.colors import white, yellow, dark_yellow, dark, gray
from core.utils import gen_circle_segment


class SmileRenderer(Renderer):
    def __init__(self):
        super().__init__()
        self.rendering_size = (200, 200)

    def render(self, screen, _):
        # pygame.draw.rect(screen, black, rect)
        pos = (100, 100)

        screen.set_colorkey(white)
        screen.fill(white)

        # body
        pygame.draw.circle(screen, yellow, (pos[0], pos[1]), 100)

        # shadow
        pygame.draw.polygon(screen, dark_yellow, gen_circle_segment((pos[0], pos[1]), -0.40, 140, 100))
        pygame.draw.polygon(screen, yellow, gen_circle_segment((pos[0] - 50, pos[1] - 50), pi / 35, 85, 140))

        # mouth
        pygame.draw.arc(screen, dark, (pos[0] - 60, pos[1] - 35, 120, 100), pi, 0, 4)

        # right eye
        pygame.draw.ellipse(screen, dark, (pos[0] + 15, pos[1] - 50, 35, 45))
        pygame.draw.circle(screen, gray, (pos[0] + 37, pos[1] - 35), 5)

        # left eye
        pygame.draw.ellipse(screen, dark, (pos[0] - 50, pos[1] - 50, 35, 45))
        pygame.draw.circle(screen, gray, (pos[0] - 27, pos[1] - 35), 5)
