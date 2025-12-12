import pygame

class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.health = 10

    def move(self, keys, border, screen_w, screen_h, vel):
        if self.color == "yellow":
            if keys[pygame.K_a] and self.rect.x - vel > 0:
                self.rect.x -= vel

            if keys[pygame.K_d] and self.rect.x + vel + self.rect.width < border.x:
                self.rect.x += vel

            if keys[pygame.K_w] and self.rect.y - vel > 0:
                self.rect.y -= vel

            if keys[pygame.K_s] and self.rect.y + vel + self.rect.height < screen_h:
                self.rect.y += vel
                
        elif self.color == "red":
            if keys[pygame.K_LEFT] and self.rect.x - vel > border.x + border.width:
                self.rect.x -= vel

            if keys[pygame.K_RIGHT] and self.rect.x + vel + self.rect.width < screen_w:
                self.rect.x += vel

            if keys[pygame.K_UP] and self.rect.y - vel > 0:
                self.rect.y -= vel

            if keys[pygame.K_DOWN] and self.rect.y + vel + self.rect.height < screen_h:
                self.rect.y += vel