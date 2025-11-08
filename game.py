# game.py
import pygame
import random
import time
from paddle import Paddle
from ball import Ball
from brick import LevelManager
from powerup import PowerUp
from ui import UI
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, POWERUP_PROB, UI_HEIGHT

class GameManager:
    def __init__(self, screen, clock, font, big_font):
        self.screen = screen
        self.clock = clock
        self.font = font
        self.big_font = big_font
        self.ui = UI(font, big_font)

        self.paddle = Paddle()
        self.ball = Ball()
        self.level_manager = LevelManager()
        self.powerups = []

        self.score = 0
        self.lives = 3
        self.level = 1
        self.game_over = False

        self.active_effects = {"PADDLE_UP":0, "BALL_SPEED":0}

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.game_over:
                    self.restart_game()

    def restart_game(self):
        self.__init__(self.screen, self.clock, self.font, self.big_font)

    def apply_effect(self, pu_type):
        current_time = time.time()
        if pu_type=="PADDLE_UP":
            self.paddle.rect.width += 20
            self.active_effects["PADDLE_UP"] = current_time
        elif pu_type=="BALL_SPEED":
            self.ball.speed_x *= 1.5
            self.ball.speed_y *= 1.5
            self.active_effects["BALL_SPEED"] = current_time
        elif pu_type=="EXTRA_LIFE":
            self.lives = min(3, self.lives + 1)

    def update_effects(self):
        current_time = time.time()
        if self.active_effects["PADDLE_UP"] !=0:
            if current_time - self.active_effects["PADDLE_UP"] >= PowerUp.EFFECT_DURATION:
                self.paddle.rect.width = 120
                self.active_effects["PADDLE_UP"]=0
        if self.active_effects["BALL_SPEED"] !=0:
            if current_time - self.active_effects["BALL_SPEED"] >= PowerUp.EFFECT_DURATION:
                speed = 5
                self.ball.speed_x = speed if self.ball.speed_x>0 else -speed
                self.ball.speed_y = -speed if self.ball.speed_y<0 else speed
                self.active_effects["BALL_SPEED"]=0

    def run(self):
        while True:
            self.handle_events()
            keys = pygame.key.get_pressed()
            if not self.game_over:
                if keys[pygame.K_LEFT]:
                    self.paddle.move("LEFT")
                if keys[pygame.K_RIGHT]:
                    self.paddle.move("RIGHT")

                self.ball.move()

                if self.ball.rect.colliderect(self.paddle.rect):
                    self.ball.bounce_off_paddle(self.paddle)

                for brick in self.level_manager.bricks:
                    if brick.alive and self.ball.rect.colliderect(brick.rect):
                        brick.alive = False
                        self.score += 10
                        self.ball.speed_y *= -1

                        if random.random() < POWERUP_PROB:
                            pu = PowerUp(brick.rect.centerx, brick.rect.centery)
                            self.powerups.append(pu)
                        break

                for pu in self.powerups[:]:
                    pu.move()
                    if pu.rect.colliderect(self.paddle.rect):
                        self.apply_effect(pu.type)
                        pu.active=False
                        self.powerups.remove(pu)
                    elif not pu.active:
                        self.powerups.remove(pu)

                self.update_effects()

                if self.ball.rect.bottom >= SCREEN_HEIGHT:
                    self.lives -=1
                    if self.lives<=0:
                        self.game_over=True
                    else:
                        self.ball.reset()

                if all(not b.alive for b in self.level_manager.bricks):
                    self.level +=1
                    self.level_manager = LevelManager(self.level)
                    self.ball.reset()

                self.screen.fill(BLACK)
                self.level_manager.draw(self.screen)
                self.paddle.draw(self.screen)
                self.ball.draw(self.screen)
                for pu in self.powerups:
                    pu.draw(self.screen)
                self.ui.show_score_lives(self.screen, self.score, self.lives, self.level)
                pygame.display.update()
                self.clock.tick(60)
            else:
                self.ui.game_over_screen(self.screen, self.score)
