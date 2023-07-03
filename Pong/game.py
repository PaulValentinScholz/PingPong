import math

import pygame
from paddle import Paddle
from ball import Ball
from damagefield import DamageField
from textfield import TextField


class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.highscore = 0
        self.color = (255, 255, 255)
        self.window.fill(self.color)
        self.paddle = Paddle(self.window)
        self.ball = Ball(self.window)
        self.damagefield = DamageField(self.window)
        self.home = True
        self.game = False
        self.game_ende = False

        self.textfield_points = TextField("Punktzahl: " + str(self.ball.points), 46, (105, 131, 161), 950, 50)
        self.textfield_highscore = TextField("Highscore: " + str(self.highscore), 46, (105, 131, 161), 500, 50)
        self.textfield_attempts = TextField("Versuche: " + str(self.ball.attempts), 46, (105, 131, 161), 50, 50)
        self.textfield_start = TextField("Drücke [Leertaste] um das Spiel zu starten!", 60, (105, 131, 161), 170, 200)
        self.textfield_lose = TextField("Du hast verloren!" + str(self.ball.attempts), 60, (105, 131, 161), 425, 350)
        self.textfield_restart = TextField("Drücke [Leertaste] um das Spiel neu zu starten!", 60, (105, 131, 161), 160,
                                           450)

    def restart_game(self):
        self.ball.reset()
        self.paddle.reset()

    def update(self):
        keys = pygame.key.get_pressed()
        if self.home:
            self.home_game(keys)
        if self.game:
            self.start_game()
        if self.game_ende:
            self.end_game(keys)

    def home_game(self, keys):
        self.textfield_start.update("Drücke Leertaste um das Spiel zu starten!")
        self.restart_game()
        if keys[pygame.K_SPACE]:
            print("SPACE")
            self.home = False
            self.game = True

    def start_game(self):
        #    self.restart_game()
        self.paddle.update()
        self.ball.update(self.paddle)
        self.textfield_points.update("Punktzahl: " + str(self.ball.points))
        self.textfield_attempts.update("Versuche: " + str(self.ball.attempts))
        if self.ball.points == 25:
            self.paddle.width = 210
        if self.ball.points == 50:
            self.paddle.width = 225
        if self.ball.points == 100:
            self.paddle.width = 250
        if self.ball.bottom_hit:
            if self.ball.points > self.highscore:
                self.highscore = self.ball.points
                self.textfield_highscore.update("Highscore: " + str(self.highscore))
            self.game = False
            self.game_ende = True

    def end_game(self, keys):
        self.textfield_lose.update("Du hast verloren!")
        self.textfield_restart.update("Drücke Leertaste um das Spiel neu zu starten!")
        if keys[pygame.K_SPACE]:
            self.game_ende = False
            self.home = True

    def render(self):
        # Clear the window
        if self.home:
            self.textfield_start.render(self.window)
            self.textfield_highscore.render(self.window)
            self.paddle.render()
            self.ball.render()
            self.damagefield.render()
            pygame.display.flip()

        if self.game:
            self.paddle.render()
            self.ball.render()
            self.damagefield.render()
            self.textfield_points.render(self.window)
            self.textfield_attempts.render(self.window)
            self.textfield_highscore.render(self.window)
            pygame.display.flip()

        if self.game_ende:
            self.textfield_lose.render(self.window)
            self.textfield_restart.render(self.window)
            self.textfield_highscore.render(self.window)
            pygame.display.flip()
