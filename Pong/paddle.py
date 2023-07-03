import pygame

class Paddle:
    def __init__(self, window):
        self.window = window
        self.width = 200
        self.height = 25
        self.x = self.window.get_width() // 2 - self.width // 2
        self.y = 860
        self.speed = 2
        self.color = (211, 219, 43)

    def reset(self):
        self.x = 300
        self.y = 860
        self.width = 200
        self.speed = 2
        self.color = (211, 219, 43)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:           # Hier ganz einfach die Tastenblegung für Paddle schneller ändern
            self.speed = 4
            self.window.fill((255, 249, 249))
        elif keys[pygame.K_DOWN]:       # Hier ganz einfach die Tastenblegung für Paddle langsamer ändern
            self.speed = 1
            self.window.fill((249, 249, 255))
        else:
            self.speed = 2
            self.window.fill((255, 255, 255))

        # Ensure paddle stays within window boundaries
        if self.x < 0:
            self.x = 0
        if self.x > self.window.get_width() - self.width:
            self.x = self.window.get_width() - self.width

    def render(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height), border_radius=20)
