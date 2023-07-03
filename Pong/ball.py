import math
import random
import time

import pygame


class Ball:

    def __init__(self, window):
        self.speed = [-1, 1]
        self.window = window
        self.radius = 30
        self.x = self.window.get_width() // 2
        self.y = self.window.get_height() // 2
        self.dx = random.choice(self.speed)
        self.dy = random.choice(self.speed)
        self.color = (105, 131, 161)
        self.color_changed_time = 0
        self.points = 0
        self.attempts = 1
        self.bottom_hit = False
        self.paddle_hit = False

    def reset(self):
        self.x = self.window.get_width() // 2
        self.y = self.window.get_height() // 2
        self.dx = random.choice(self.speed)
        self.dy = random.choice(self.speed)
        self.color = (105, 131, 161)
        self.color_changed_time = 0
        self.points = 0
        self.attempts = 1
        self.bottom_hit = False
        self.paddle_hit = False

    def update(self, paddle):
        self.x += self.dx
        self.y += self.dy

        # Check collision with window boundaries
        if self.x < self.radius or self.x > self.window.get_width() - self.radius:
            self.dx = -self.dx * 1.05
            paddle.color = (211, 219, 43)
            self.paddle_hit = False

        if self.y > self.window.get_height() + self.radius:
            self.bottom_hit = True
            self.paddle_hit = False

        if self.y < self.radius:
            self.dy = -self.dy * 1.05
            paddle.color = (211, 219, 43)
            self.paddle_hit = False

            # Check collision with paddle
        if not self.paddle_hit:
            if self.ball_object_collided(paddle):
                self.paddle_hit = True
                # Ball has collided with the paddle
                paddle.color = (105, 131, 161)
                paddle_center_x = paddle.x + paddle.width / 2
                hit_offset = self.x - paddle_center_x  # Calculate the offset from the center of the paddle
                normalized_offset = hit_offset / (
                        paddle.width / 2)  # Normalize the offset to a value between -1 and 1
                angle = normalized_offset * (math.pi / 4)  # Scale the offset to an angle between -45 and 45 degrees
                original_speed = math.sqrt(
                    self.dx ** 2 + self.dy ** 2)  # Calculate the original speed of the ball
                self.dx = original_speed * math.sin(angle)  # Adjust the x-component of velocity based on the angle
                self.dy = -original_speed * math.cos(angle)  # Adjust the y-component of velocity based on the angle
                if paddle.speed <= 4:
                    paddle.speed *= 1.05
                self.points += 1

    def ball_object_collided(self, object):
        if self.x + self.radius >= object.x and self.x - self.radius <= object.x + object.width:
            if self.y + self.radius >= object.y and self.y - self.radius <= object.y + object.height:
                return True
        return False

    def render(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)
