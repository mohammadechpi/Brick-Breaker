# ui.py
import pygame
from config import WHITE, RED, BLACK, SCREEN_WIDTH, UI_HEIGHT

class UI:
    def __init__(self, font, big_font):
        self.font = font
        self.big_font = big_font
        self.bar_height = UI_HEIGHT

    def show_score_lives(self, screen, score, lives, level):
        pygame.draw.rect(screen, (50,50,50,200), (0,0,SCREEN_WIDTH,self.bar_height), border_radius=10)
        pygame.draw.line(screen, (200,200,200), (0,self.bar_height), (SCREEN_WIDTH,self.bar_height), 2)

        score_text = self.font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 15))

        level_text = self.font.render(f"Level: {level}", True, WHITE)
        screen.blit(level_text, (SCREEN_WIDTH//2 - level_text.get_width()//2, 15))

        for i in range(lives):
            x = SCREEN_WIDTH - 40 - i*35
            y = 35
            self.draw_heart(screen, x, y)

    def draw_heart(self, screen, x, y):
        r = 7
        pygame.draw.circle(screen, RED, (x, y), r)
        pygame.draw.circle(screen, RED, (x + 2*r, y), r)
        points = [(x - r, y), (x + 3*r, y), (x + r, y + 2*r)]
        pygame.draw.polygon(screen, RED, points)


    def game_over_screen(self, screen, score):
        screen.fill(BLACK)
        text = self.big_font.render("GAME OVER!", True, RED)
        score_text = self.font.render(f"Final Score: {score}", True, WHITE)
        retry_text = self.font.render("Press ENTER to Restart", True, WHITE)
        screen.blit(text, [SCREEN_WIDTH//2 - text.get_width()//2, 200])
        screen.blit(score_text, [SCREEN_WIDTH//2 - score_text.get_width()//2, 280])
        screen.blit(retry_text, [SCREEN_WIDTH//2 - retry_text.get_width()//2, 340])
        pygame.display.flip()
