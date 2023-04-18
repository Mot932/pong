import pygame
import sys
import degrees_to_velocity

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
player_y_1 = screen_height // 2 - player_1_height // 2
player_1 = pygame.Rect((player_x_1, player_y_1, player_1_width, player_1_height))
player_2_width = 20
player_2_height = 150
player_x_2 = screen_width - player_1_width - 50
player_y_2 = screen_height // 2 - player_2_height // 2
player_2 = pygame.Rect((player_x_2, player_y_2, player_2_width, player_2_height))


ball_width = 15
ball_height = 15
ball_x = screen_width // 2 - ball_width // 2
ball_y = screen_height // 2 - ball_height // 2
velocity = degrees_to_velocity.degrees_to_velocity(60, 10)
ball_speed_x = velocity[0]
ball_speed_y = velocity[1]
ball = pygame.Rect((ball_x, ball_y, ball_height, ball_width))

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
        player_2.y -= 8
        if player_2.y < 0:
            player_2.y = 0
    if keys[pygame.K_DOWN]:
        player_2.y += 8
        if player_2.y > screen_height - player_2_height:
            player_2.y = screen_height - player_2_height
    if keys[pygame.K_w]:
        player_1.y -= 8
        if player_1.y < 0:
            player_1.y = 0
    if keys[pygame.K_s]:
        player_1.y += 8
        if player_1.y > screen_height - player_1_height:
            player_1.y = screen_height - player_1_height

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.x < 0:
        ball_speed_x *= -1
    if ball.x > screen_width - ball_width:
        ball_speed_x *= -1
    if ball.y < 0:
        ball_speed_y *= -1
    if ball.y > screen_height - ball_height:
        ball_speed_y *= -1


    # отрисовка
    screen.fill(screen_color)                                               
    pygame.draw.rect(screen, WHITE, player_1)
    pygame.draw.rect(screen, WHITE, player_2)
    pygame.draw.rect(screen, WHITE, ball)
    pygame.display.flip()

    clock.tick(100)