import pygame
import random
from config import POWERUP_TYPES, POWERUP_COLORS, SCREEN_HEIGHT

class PowerUp:
    EFFECT_DURATION = 5

    def __init__(self, x, y, type=None):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.type = type if type else random.choice(POWERUP_TYPES)
        self.color = POWERUP_COLORS[self.type]
        self.speed_y = 3
        self.active = True
        self.effect_time = 0

    def move(self):
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT:
            self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)
