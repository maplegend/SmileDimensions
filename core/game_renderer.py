import pygame
from .components.renderer_component import RendererComponent
from .components.transform import TransformComponent
from .components.renderer_effect import RendererEffect
from .colors import white


class GameRender:
    def __init__(self, game):
        self.game = game

    def draw(self):
        screen = self.game.game_screen.screen
        screen.fill(white)
        for ent in self.game.scene.get_entities_with_component(RendererComponent):
            rend = ent.get_component(RendererComponent)
            trans = ent.get_component(TransformComponent)
            if not rend or not trans:
                continue
            if rend.need_redraw or rend.image is None:
                rend.render(trans.rect, ent)
                effects = ent.get_components(RendererEffect)
                if effects is not None:
                    for ef in effects:
                        rend.image = ef.process(rend.image)
                rend.need_redraw = False

            screen.blit(rend.image, trans.rect)

        pygame.display.flip()
