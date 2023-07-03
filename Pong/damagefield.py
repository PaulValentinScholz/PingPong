import pygame

class DamageField:
    def __init__(self, window):
        self.window = window
        self.width = self.window.get_width()
        self.height = 5
        self.x = 0
        self.y = 895
        self.color = (255, 77, 77)

    def render(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
