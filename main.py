import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

background = "antiquewhite"
grid = "antiquewhite4"
line_width = 5

taille = 1
snake_positions = [(2, 2)]
snake_direction = (1, 0)

T = set()
nb_pomme = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake tu connais")

def draw_background():
    screen.fill(background)
    for i in range(0, 17):
        pygame.draw.line(screen, grid, (0, i * 50), (SCREEN_WIDTH, i * 50), line_width)
        pygame.draw.line(screen, grid, (i * 50, 0), (i * 50, SCREEN_HEIGHT), line_width)

def draw_snake(snake_positions):
    for i, pos in enumerate(snake_positions):
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0] * 50, pos[1] * 50, 50, 50))
        
        # Dessine les yeux seulement sur la tête du serpent (premier segment)
        if i == 0:
            eye_radius = 5
            left_eye_pos = (pos[0] * 50 + 15, pos[1] * 50 + 15)
            right_eye_pos = (pos[0] * 50 + 35, pos[1] * 50 + 15)
            
            # Dessine les yeux
            pygame.draw.ellipse(screen, WHITE, (left_eye_pos[0] - eye_radius, left_eye_pos[1] - eye_radius, eye_radius * 2, eye_radius * 2))
            pygame.draw.ellipse(screen, WHITE, (right_eye_pos[0] - eye_radius, right_eye_pos[1] - eye_radius, eye_radius * 2, eye_radius * 2))
            
            # Dessine les pupilles
            pygame.draw.circle(screen, BLACK, left_eye_pos, eye_radius)
            pygame.draw.circle(screen, BLACK, right_eye_pos, eye_radius)


def case():
    for ligne in range(0, 16):
        for colonne in range(0, 16):
            coord = (ligne, colonne)
            T.add(coord)

def draw_apple():
    global nb_pomme
    x = random.randint(0, 15)
    y = random.randint(0, 15)
    while (x, y) in snake_positions:
        x = random.randint(0, 15)
        y = random.randint(0, 15)
        
    apple_rect = pygame.Rect(x * 50 + 5, y * 50 + 5, 40, 40)
    pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    nb_pomme += 1 
    pygame.display.update()
    
    #print(x, y)
    return x, y

def score():
    global nb_pomme
    score_final = nb_pomme * 100
    return score_final

case()
apple_x, apple_y = draw_apple()
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_s and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_q and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_d and snake_direction != (-1, 0):
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
        print("score final :", score())
        run = False

    draw_background()
    draw_snake(snake_positions)

    apple_rect = pygame.Rect(apple_x * 50 + 5, apple_y * 50 + 5, 40, 40)
    pygame.draw.rect(screen, (255, 0, 0), apple_rect)
    
    pygame.display.update()

    time.sleep(0.1)

pygame.quit()
