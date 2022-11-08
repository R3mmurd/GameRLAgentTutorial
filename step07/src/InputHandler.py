
import settings

class Action:
    def execute(self, *args, **kwargs):
        pass

class InputHandler:
    actions = {}
    
    @classmethod
    def add_action(cls, key, action):
        cls.actions[key] = action
    
    @classmethod
    def handle_input(cls, *args, **kwargs):
        for k in settings.pressed_keys:
            if settings.pressed_keys[k] and k in cls.actions:
                cls.actions[k].execute(*args, **kwargs)
                settings.pressed_keys[k] = False
