# импортируем pygame
import time

import pygame
import random

WIDTH = 1200
HEIGHT = 700
FPS = 60

# РАКЕТКА
paddle_w = 330
paddle_h = 35
paddle_speed = 15
dx = 1
dy = -1
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)

# Шарик
ball_radius = 20
ball_speed = 8
ball = pygame.Rect(300, 300, (ball_radius * 2 ** 1 / 2), (ball_radius * 2 ** 1 / 2))

blocks = []
colors = []
for i in range(10):
    for k in range(4):
        blocks.append(pygame.Rect(10 + 120 * i, 10 + 70 * k, 100, 50))
        colors.append((random.randrange(20, 255), random.randrange(20, 255), random.randrange(20, 255)))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
timer = pygame.time.Clock()
img = pygame.image.load("1.jpg").convert()


def detect_colision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(img, (0, 0))
    pygame.draw.rect(screen, pygame.Color("red"), paddle)
    pygame.draw.circle(screen, pygame.Color("white"), ball.center, ball_radius)

    # Рисуем блоки
    for block in blocks:
        for color in colors:
            pygame.draw.rect(screen, color, block)

    # Столкновение с блоками
    hit = ball.collidelist(blocks)
    if hit != -1:
        hit_rect = blocks.pop(hit)
        dx, dy = detect_colision(dx, dy, ball, hit_rect)




    # Конец игры
    if ball.bottom > HEIGHT:
        print("Game Over")
        time.sleep(1)
        exit()
    elif len(blocks) == 0:
        print("Win")
        time.sleep(2)
        exit()



    # Движение шарика
    ball.x = ball.x + ball_speed * dx
    ball.y = ball.y + ball_speed * dy

    # Столкновения
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = - dx
    if ball.centery < ball_radius or ball.centery > HEIGHT - ball_radius:
        dy = - dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_colision(dx, dy, ball, paddle)

    # Управление ракеткой
    key = pygame.key.get_pressed()  # {"A": DESCRIPTION}
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left = paddle.left - paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right = paddle.right + paddle_speed

    pygame.display.flip()
    timer.tick(FPS)
