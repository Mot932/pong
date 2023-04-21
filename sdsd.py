import pygame
import sys
from degrees_to_velocity import degrees_to_velocity
import random

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

player_x = 800
player_y = 0
player_color_1 = WHITE
player_color_2 = WHITE
screen_width = 900
screen_height = 700
screen_color = (0, 0, 0)
screen = pygame.display.set_mode((screen_width, screen_height)) # экран
pygame.display.set_caption("Моя программа")

player_1_width = 20
player_1_height = 150
player_x_1 = 50
player_1_score = 0
player_y_1 = screen_height // 2 - player_1_height // 2
player_1 = pygame.Rect((player_x_1, player_y_1, player_1_width, player_1_height))
player_1_speed = 8
player_2_width = 20
player_2_height = 150
player_2_score = 0
player_x_2 = screen_width - player_1_width - 50
player_y_2 = screen_height // 2 - player_2_height // 2
player_2 = pygame.Rect((player_x_2, player_y_2, player_2_width, player_2_height))
player_2_speed = 8

ball_width = 15
ball_height = 15
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
velocity = degrees_to_velocity(60, 7)
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]
ball = pygame.Rect((ball_x, ball_y, ball_height, ball_width))

def ball_to_center():
    ball.x = ball_x
    
"""
    if random.randint(0, 1) == 0:
        velocity = degrees_to_velocity(random.randint(215, 305), 7)
    else:
        velocity = degrees_to_velocity(random.randint(215, 305), 7)
    
    ball_speed_x = velocity[0]
    ball_speed_y = velocity[1]
"""
    
    
    
score_right = pygame.font.Font(None, 60)
score_left = pygame.font.Font(None, 60)



game = True
while game: # главный цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_2.y -= player_1_speed
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:
        player_2.y += player_1_speed
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height
    if keys[pygame.K_w]:
        player_1.y -= player_2_speed
        if player_1.y < 0:
            player_1.y = 0
    if keys[pygame.K_s]:
        player_1.y += player_2_speed
        if player_1.y > screen_height - player_1_height:
            player_1.y = screen_height - player_1_height

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.x < 0:
        player_2_score += 1
        ball_to_center()
    if ball.x > screen_width - ball_width:
        player_1_score += 1
        ball_to_center()
    if ball.y < 0:
        ball_speed_y *= -1
    if ball.y > screen_height - ball_height:
        ball_speed_y *= -1

    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1


    # отрисовка
    screen.fill(screen_color)                                               
    pygame.draw.rect(screen, WHITE, player_1)
    pygame.draw.rect(screen, WHITE, player_2)
    pygame.draw.rect(screen, WHITE, ball)
    score_left_img = score_left.render(str(player_1_score), True, WHITE)
    score_right_img = score_right.render(str(player_2_score), True, WHITE)
    screen.blit(score_left_img, (screen_width * 0.25, 20))
    screen.blit(score_right_img, (screen_width * 0.75, 20))
    line = pygame.draw.line(
        screen,
        WHITE, 
        [screen_width // 2, 0], 
        [screen_width // 2, screen_height],
        5)
    
    pygame.display.flip()

    clock.tick(100)