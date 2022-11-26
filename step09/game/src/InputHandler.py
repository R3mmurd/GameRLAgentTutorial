from typing import Any

from game import settings

class Action:
    def execute(self, *args: Any, **kwargs: Any) -> None:
        pass

class InputHandler:
    actions = {}
    
    @classmethod
    def add_action(cls, key: int, action: Action) -> None:
        cls.actions[key] = action
    
    @classmethod
    def handle_input(cls, *args: Any, **kwargs: Any) -> None:
        for k in settings.pressed_keys:
            if settings.pressed_keys[k] and k in cls.actions:
                cls.actions[k].execute(*args, **kwargs)
                settings.pressed_keys[k] = False

