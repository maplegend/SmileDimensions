from core.component import Component
from core.components.renderer_component import RendererComponent
from core.events.update import UpdateEvent
from .effects.fade import FadeEffect


class FadeAnimationComponent(Component):
    def __init__(self):
        super().__init__()
        self.fade_progress = 0
        self.animating = False
        self.finish_callback = None
        self.entity = None

    def animate(self, callback=lambda: None):
        self.animating = True
        self.finish_callback = callback
        self.entity.add_component(FadeEffect())

    def update(self, _):
        if self.animating:
            self.fade_progress += 2
            self.entity.get_component(FadeEffect).strength = 255 - self.fade_progress*(255/100)
            self.entity.get_component(RendererComponent).need_redraw = True
            if self.fade_progress > 100:
                self.entity.remove_component(FadeEffect)
                self.finish_callback()
                self.animating = False

    def applied_on_entity(self, entity):
        self.entity = entity
        event_manager = entity.scene.game.event_manager
        event_manager.bind(UpdateEvent, self.update)
