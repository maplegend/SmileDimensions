from core.component import Component
from core.components.renderer_component import RendererComponent
from core.events.key_press import KeyPressEvent


class HideOnKeyComponent(Component):
    def __init__(self, entities, key):
        super().__init__()
        self.entities = entities
        self.key = key
        self.entity = None

    def key_press(self, event):
        if event.key == self.key:
            [ent.remove_component(RendererComponent) for ent in self.entities]

    def applied_on_entity(self, entity):
        event_manager = entity.scene.game.event_manager
        event_manager.bind(KeyPressEvent, self.key_press)
