import pygame
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Space Shooter"
)

clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,100,255)
BLACK = (0,0,0)

# Player
player = pygame.Rect(
    WIDTH//2,
    HEIGHT-70,
    50,
    50
)

player_speed = 6

# Bullets
bullets = []

# Enemies
enemies = []

enemy_speed = 4

# Score
score = 0

font = pygame.font.SysFont(
    "Arial",
    30
)

running = True

while running:

    screen.fill(BLACK)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullet = pygame.Rect(
                    player.centerx - 3,
                    player.y,
                    6,
                    15
                )

                bullets.append(
                    bullet
                )

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    player.x = max(
        0,
        min(player.x, WIDTH-50)
    )

    # Spawn Enemies
    if random.randint(1,40) == 1:

        enemy = pygame.Rect(
            random.randint(
                0,
                WIDTH-40
            ),
            0,
            40,
            40
        )

        enemies.append(enemy)

    # Update Bullets
    for bullet in bullets[:]:

        bullet.y -= 8

        if bullet.y < 0:

            bullets.remove(bullet)

    # Update Enemies
    for enemy in enemies[:]:

        enemy.y += enemy_speed

        if enemy.y > HEIGHT:

            enemies.remove(enemy)

        # Collision with Player
        if enemy.colliderect(player):

            running = False

    # Bullet Hits Enemy
    for bullet in bullets[:]:

        for enemy in enemies[:]:

            if bullet.colliderect(enemy):

                bullets.remove(bullet)

                enemies.remove(enemy)

                score += 10

                break

    # Draw Player
    pygame.draw.rect(
        screen,
        BLUE,
        player
    )

    # Draw Bullets
    for bullet in bullets:

        pygame.draw.rect(
            screen,
            WHITE,
            bullet
        )

    # Draw Enemies
    for enemy in enemies:

        pygame.draw.rect(
            screen,
            RED,
            enemy
        )

    # Score
    score_text = font.render(
        f"Score: {score}",
        True,
        WHITE
    )

    screen.blit(
        score_text,
        (10,10)
    )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
