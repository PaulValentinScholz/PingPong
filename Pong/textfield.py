import pygame

class TextField:
    def __init__(self, text, font_size, color, x, y):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont(None, self.font_size)


    def update(self, text):
        self.text = text
    def render(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.x, self.y))
