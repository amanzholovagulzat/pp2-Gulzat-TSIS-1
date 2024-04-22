import pygame
import psycopg2
import random
import time

pygame.init()

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=" "
)

cur = conn.cursor()

x = 0

width = 640
height = 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

green = (0, 255, 0)
light_green = (0, 200, 0)
blue = (0, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

snake_size = 20
snake_speed = 20
snake_x = width // (2 * snake_size) * snake_size
snake_y = height // (2 * snake_size) * snake_size
snake_dx = snake_speed
snake_dy = 0
snake_body = [(snake_x, snake_y)]

food_size = 20
food_x = random.randrange(0, width - food_size, food_size)
food_y = random.randrange(0, height - food_size, food_size)

score = 0
level = 1
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

def welcome():
    user_name = "Write user name:"
    global name
    FONT_SIZE = 24
    FONT = pygame.font.SysFont("Arial", FONT_SIZE)
    text_box = pygame.Rect(width / 2 - 100, height / 4 + 50, 200, 40)
    text = ""
    cursor = "|"
    ch = True
    while ch:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    ch = False
                else:
                    text += event.unicode

        name = text
        # Draw the screen
        screen.fill(white)
        pygame.draw.rect(screen, black, text_box, 2)

        # Draw the text
        text_surface = FONT.render(text + cursor, True, black)
        screen.blit(text_surface, (text_box.x + 5, text_box.y + 5))

        # Update the display
        pygame.display.flip()

def game_over():
    cur.execute(
        "INSERT INTO user_name (username) VALUES (%s)",
        (name,)
    )
    cur.execute("SELECT id FROM user_name WHERE username = %s", (name,))
    user_id = cur.fetchone()[0]
    cur.execute(
        'INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)',
        (user_id, score, level)
    )
    conn.commit()
    cur.close()
    conn.close()
    # создание объекта шрифта my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # создание текстовой поверхности, на которой текст
    # будет нарисовано
    game_over_surface = my_font.render(
        'Score is : ' + str(score) + '  Level :' + str(level), True, red)

    # создать прямоугольный объект для текста
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # установка положения текста
    game_over_rect.midtop = (height / 2, width / 4)

    # blit нарисует текст на экране
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # через 2 секунды мы выйдем из программы
    time.sleep(2)

    # деактивация библиотеки pygame
    pygame.quit()

    # quit the program
    quit()

welcome()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_dx = -snake_speed
                snake_dy = 0
            elif event.key == pygame.K_RIGHT:
                snake_dx = snake_speed
                snake_dy = 0
            elif event.key == pygame.K_UP:
                snake_dx = 0
                snake_dy = -snake_speed
            elif event.key == pygame.K_DOWN:
                snake_dx = 0
                snake_dy = snake_speed

    # move the snake
    snake_x += snake_dx
    snake_y += snake_dy

    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        pygame.quit()

    # wrap the snake around the screen
    if snake_x < 0:
        snake_x = width - snake_size
    elif snake_x >= width:
        snake_x = 0
    elif snake_y < 0:
        snake_y = height - snake_size
    elif snake_y >= height:
        snake_y = 0

    # check if the snake hit itself
    if (snake_x, snake_y) in snake_body:
        score = 0
        level = 1
        snake_x = width // (2 * snake_size) * snake_size
        snake_y = height // (2 * snake_size) * snake_size
        snake_dx = snake_speed
        snake_dy = 0
        snake_body = [(snake_x, snake_y)]

    # check if the snake ate the food
    if snake_x == food_x and snake_y == food_y:
        score += 1
        if score // x + 40:
            level += 1
            x += 5
        food_x = random.randrange(0, width - food_size, food_size)
        food_y = random.randrange(0, height - food_size, food_size)
        snake_body.append((snake_x, snake_y))


    # update the snake body
    snake_body.insert(0, (snake_x, snake_y))
    if len(snake_body) > score + 1:
        snake_body.pop()

    # draw the background
    for i in range(0, width, snake_size):
        for j in range(0, height, snake_size):
            if (i // snake_size + j // snake_size) % 2 == 0:
                pygame.draw.rect(screen, green, (i, j, snake_size, snake_size))
            else:
                pygame.draw.rect(screen, light_green, (i, j, snake_size, snake_size))

    # draw the snake
    for b in snake_body:
        pygame.draw.rect(screen, blue, (b[0], b[1], snake_size, snake_size))
        pygame.draw.rect(screen, black, (b[0] + 4, b[1] + 4, snake_size - 8, snake_size - 8))

    # draw the food
    pygame.draw.rect(screen, red, (food_x, food_y, food_size, food_size))

    if snake_x < 0 or snake_x > width - 10:
        game_over()
    if snake_y < 0 or snake_y > height - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_x == block[0] and snake_y == block[1]:
            game_over()

    # draw the score and level
    score_text = font.render("Score: " + str(score), True, white)
    level_text = font.render("Level: " + str(level), True, white)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    # update the display
    pygame.display.update()

    # wait for a while
    clock.tick(10)