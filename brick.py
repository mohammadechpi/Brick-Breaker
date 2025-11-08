# brick.py
import pygame
import random
from config import BRICK_WIDTH, BRICK_HEIGHT, SCREEN_WIDTH, UI_HEIGHT, RED, GREEN, BLUE, YELLOW, ORANGE, WHITE

class Brick:
    COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE]

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.color = random.choice(self.COLORS)
        self.alive = True

class LevelManager:
    def __init__(self, level=1):
        self.level = level
        self.bricks = []
        self.create_level()

    def create_level(self):
        self.bricks = []
        rows = 4 + self.level
        cols = 10
        offset_x = (SCREEN_WIDTH - cols*BRICK_WIDTH)//2
        offset_y = UI_HEIGHT + 50
        for row in range(rows):
            for col in range(cols):
                self.bricks.append(Brick(offset_x + col*BRICK_WIDTH, offset_y + row*BRICK_HEIGHT))

    def draw(self, screen):
        for brick in self.bricks:
            if brick.alive:
                pygame.draw.rect(screen, brick.color, brick.rect)
                pygame.draw.rect(screen, WHITE, brick.rect, 2)
