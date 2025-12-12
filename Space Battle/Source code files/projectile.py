import pygame
import random

class Bullet:
    def __init__(self, x, y, vel, color):
        self.rect = pygame.Rect(x, y, 10, 5)
        self.vel = vel
        self.color = color

    def move(self):
        self.rect.x += self.vel


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(2, 4)
        self.life = random.randint(10, 20)
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 1

    def draw(self, win):
        if self.life > 0:
            pygame.draw.circle(win, (255, 150, 0), (int(self.x), int(self.y)), self.radius)