import pygame
from game import GameManager
from config import SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker Pro")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 25)
big_font = pygame.font.SysFont("arial", 60)

if __name__ == "__main__":
    game = GameManager(screen, clock, font, big_font)
    game.run()
