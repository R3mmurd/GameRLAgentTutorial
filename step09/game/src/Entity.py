from typing import Dict, Callable, Any, TypeVar

from gale.state_machine import StateMachine
from gale.animation import Animation

from game.src.mixins import DrawableMixin

class Entity(DrawableMixin):
    def __init__(self, x: int, y: int, width: int, height: int, texture: str, game_level: TypeVar('GameLevel'),
                 states: Dict[str, Callable] = {}, animations: Dict[str, Any] = {}) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vx = 0
        self.vy = 0
        self.texture = texture
        self.game_level = game_level
        self.tile_map = self.game_level.tile_map
        self.state_machine = StateMachine(states)
        self.animations = {}
        self.current_animation = None
        self._generate_animations(animations)

    def update(self, dt: float) -> None:
        self.state_machine.update(dt)
        self.current_animation.update(dt)
        self.frame = self.current_animation.get_current_frame()

    def change_animation(self, animation_name: str) -> None:
        animation = self.animations.get(animation_name)
        if animation and animation != self.current_animation:
            self.current_animation = animation
            self.current_animation.reset()
            self.frame = self.current_animation.get_current_frame()
    
    def _generate_animations(self, animations: Dict[str, Any]) -> None:
        for k, v in animations.items():
            animation = Animation(
                v['frames'],
                v.get('interval', 0),
                loops=v.get('loops')
            )
            self.animations[k] = animation