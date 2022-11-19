import pygame

from game import settings

class DrawableMixin:
    def render(self, surface):
        texture = settings.GAME_TEXTURES[self.texture]
        frame = settings.GAME_FRAMES[self.texture][self.frame]
        image = pygame.Surface((frame.width, frame.height), pygame.SRCALPHA)
        image.fill((0, 0, 0, 0))
        image.blit(texture, (0, 0), frame)
        surface.blit(image, (self.x, self.y))
