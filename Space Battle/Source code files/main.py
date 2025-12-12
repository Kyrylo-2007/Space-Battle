import pygame
import os
from player import Player
from projectile import Bullet, Particle

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Battle")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 80)

HIT_SOUND = pygame.mixer.Sound('Assets/Grenade+1.mp3')
FIRE_SOUND = pygame.mixer.Sound('Assets/Gun+Silencer.mp3')
sound_on = True

YELLOW_IMG = pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load(os.path.join('Assets','spaceship_yellow.png')), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_IMG = pygame.transform.rotate(pygame.transform.scale(
    pygame.image.load(os.path.join('Assets','spaceship_red.png')), (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')), (WIDTH, HEIGHT))


def draw_health(yellow, red):
    yellow_text = HEALTH_FONT.render(f"HEALTH: {yellow.health}", True, WHITE)
    red_text = HEALTH_FONT.render(f"HEALTH: {red.health}", True, WHITE)
    WIN.blit(yellow_text, (10, 10))
    WIN.blit(red_text, (WIDTH - red_text.get_width() - 10, 10))


def draw_winner(text):
    winner_text = WINNER_FONT.render(text, True, WHITE)
    WIN.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2 - winner_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    clock = pygame.time.Clock()

    yellow = Player(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, "yellow")
    red = Player(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT, "red")

    yellow_bullets = []
    red_bullets = []
    particles = []

    bg_y = 0

    global sound_on
    run = True

    while run:
        clock.tick(FPS)
        
        bg_y = (bg_y + 1) % HEIGHT
        WIN.blit(SPACE, (0, bg_y - HEIGHT))
        WIN.blit(SPACE, (0, bg_y))

        pygame.draw.rect(WIN, BLACK, BORDER)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                
                if event.key == pygame.K_m:
                    sound_on = not sound_on

                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = Bullet(
                        yellow.rect.x + yellow.rect.width,
                        yellow.rect.y + yellow.rect.height // 2, BULLET_VEL, YELLOW
                    )
                    yellow_bullets.append(bullet)
                    if sound_on: FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = Bullet(
                        red.rect.x,
                        red.rect.y + red.rect.height // 2, - BULLET_VEL, RED
                    )
                    red_bullets.append(bullet)
                    if sound_on: FIRE_SOUND.play()

        keys = pygame.key.get_pressed()
        yellow.move(keys, BORDER, WIDTH, HEIGHT, VEL)
        red.move(keys, BORDER, WIDTH, HEIGHT, VEL)

        for b in yellow_bullets[:]:
            b.move()
            if red.rect.colliderect(b.rect):
                red.health -= 1
                yellow_bullets.remove(b)
                if sound_on: HIT_SOUND.play()
                for _ in range(20):
                    particles.append(Particle(b.rect.x, b.rect.y))
            elif b.rect.x > WIDTH:
                yellow_bullets.remove(b)

        for b in red_bullets[:]:
            b.move()
            if yellow.rect.colliderect(b.rect):
                yellow.health -= 1
                red_bullets.remove(b)
                if sound_on: HIT_SOUND.play()
                for _ in range(20):
                    particles.append(Particle(b.rect.x, b.rect.y))
            elif b.rect.x < 0:
                red_bullets.remove(b)

        for p in particles[:]:
            p.update()
            if p.life <= 0:
                particles.remove(p)
            else:
                p.draw(WIN)

        WIN.blit(YELLOW_IMG, (yellow.rect.x, yellow.rect.y))
        WIN.blit(RED_IMG, (red.rect.x, red.rect.y))

        for b in yellow_bullets:
            pygame.draw.rect(WIN, YELLOW, b.rect)
        for b in red_bullets:
            pygame.draw.rect(WIN, RED, b.rect)

        draw_health(yellow, red)

        if yellow.health <= 0:
            draw_winner("RED WINS!")
            main()
            return

        if red.health <= 0:
            draw_winner("YELLOW WINS!")
            main()
            return
        pygame.display.update()

if __name__ == "__main__":
    main()