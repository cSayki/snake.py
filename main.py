import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

background = "antiquewhite"
grid = "antiquewhite4"
line_width = 5

taille = 1
snake_positions = [(2, 2)]
snake_direction = (1, 0)

T = set()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake tu connais")

def draw_background():
    screen.fill(background)
    for i in range(0, 17):
        pygame.draw.line(screen, grid, (0, i * 50), (SCREEN_WIDTH, i * 50), line_width)
        pygame.draw.line(screen, grid, (i * 50, 0), (i * 50, SCREEN_HEIGHT), line_width)

def draw_snake():
    for pos in snake_positions:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50))

def case():
    for ligne in range(0, 16):
        for colonne in range(0, 16):
            coord = (ligne, colonne)
            T.add(coord)

def draw_apple():
    x = random.randint(0, 15)
    y = random.randint(0, 15)
    while x and y in snake_positions:
        apple_rect = pygame.Rect(x * 50 + 5, y * 50 + 5, 40, 40)
        pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    pygame.display.update()
    print(x, y)
    return x, y


case()
apple_x, apple_y = draw_apple()
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    snake_head = (snake_positions[0][0] + snake_direction[0], snake_positions[0][1] + snake_direction[1])
    snake_positions.insert(0, snake_head)

    if snake_head[0] == apple_x and snake_head[1] == apple_y:
        apple_x, apple_y = draw_apple()
        taille += 1
    else:
        snake_positions.pop()

    if (
        snake_head[0] < 0 or snake_head[0] >= 16 or
        snake_head[1] < 0 or snake_head[1] >= 16 or
        snake_head in snake_positions[1:]
    ):
        run = False

    draw_background()
    draw_snake()

    apple_rect = pygame.Rect(apple_x * 50 + 5, apple_y * 50 + 5, 40, 40)
    pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    
    pygame.display.update()

    time.sleep(0.1)

pygame.quit()
