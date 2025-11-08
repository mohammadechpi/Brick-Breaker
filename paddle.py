import pygame
from config import PADDLE_WIDTH, PADDLE_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_SPEED

class Paddle:
    def __init__(self):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.rect = pygame.Rect(SCREEN_WIDTH//2 - self.width//2, SCREEN_HEIGHT - 50, self.width, self.height)
        self.speed = PADDLE_SPEED

    def move(self, direction):
        if direction == "LEFT":
            self.rect.x -= self.speed
        elif direction == "RIGHT":
            self.rect.x += self.speed
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, (200,200,255), self.rect, border_radius=8)
