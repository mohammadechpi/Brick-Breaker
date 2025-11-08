import pygame
import random
import math
from config import BALL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, UI_HEIGHT

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH//2, SCREEN_HEIGHT - 100, BALL_SIZE, BALL_SIZE)
        self.speed_x = random.choice([-5,5])
        self.speed_y = -5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= UI_HEIGHT:
            self.rect.top = UI_HEIGHT
            self.speed_y *= -1

    def reset(self):
        self.rect.center = (SCREEN_WIDTH//2, SCREEN_HEIGHT - 100)
        self.speed_x = random.choice([-5,5])
        self.speed_y = -5

    def bounce_off_paddle(self, paddle):
        paddle_center = paddle.rect.x + paddle.rect.width/2
        ball_center = self.rect.x + self.rect.width/2
        offset = (ball_center - paddle_center) / (paddle.rect.width/2)
        max_angle = 60
        angle = offset * max_angle
        speed = (self.speed_x**2 + self.speed_y**2)**0.5
        rad = math.radians(angle)
        self.speed_x = speed * math.sin(rad)
        self.speed_y = -abs(speed * math.cos(rad))

    def draw(self, screen):
        pygame.draw.ellipse(screen, (255,255,255), self.rect)
