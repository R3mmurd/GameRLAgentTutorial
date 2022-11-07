from gale.state_machine import StateMachine
from gale.animation import Animation

class Entity:
    def __init__(self, x, y, width, height, texture, game_level,
                 states = {}, animations = {}):
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

    def update(self, dt):
        self.state_machine.update(dt)
        self.current_animation.update(dt)
        self.frame = self.current_animation.get_current_frame()

    def change_animation(self, animation_name):
        animation = self.animations.get(animation_name)
        if animation and animation != self.current_animation:
            self.current_animation = animation
            self.current_animation.reset()
            self.frame = self.current_animation.get_current_frame()
    
    def _generate_animations(self, animations):
        for k, v in animations.items():
            animation = Animation(
                v['frames'],
                v.get('interval', 0),
                loops=v.get('loops')
            )
            self.animations[k] = animation