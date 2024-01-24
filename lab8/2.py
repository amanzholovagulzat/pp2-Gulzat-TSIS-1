import random
import pygame
pygame.init()
WIDTH, HEIGHT = 800, 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLOCK_SIZE = 40
SIDE = "UP"
pygame.display.set_caption('Snake')
fps = 10
cnt = 0
lvl = 0
font = pygame.font.SysFont("Verdana", 70)
font_score = pygame.font.SysFont("Verdana", 30)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)
    @property
    def x(self):
        return self.location.x
    @property
    def y(self):
        return self.location.y
    def update(self):
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
class Snake:
    def __init__(self):
        self.points = [
            Point(WIDTH // BLOCK_SIZE // 2, HEIGHT // BLOCK_SIZE // 2),
            Point(WIDTH // BLOCK_SIZE // 2 + 1, HEIGHT // BLOCK_SIZE // 2),
        ]
    def update(self):
        head = self.points[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.points[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )
    def move(self, dx, dy):
        for idx in range(len(self.points) - 1, 0, -1):
            self.points[idx].x = self.points[idx - 1].x
            self.points[idx].y = self.points[idx - 1].y
        self.points[0].x += dx
        self.points[0].y += dy
        head = self.points[0]
        if head.x > WIDTH // BLOCK_SIZE - 1:
            pygame.quit()
            exit()
        elif head.x < 0:
            pygame.quit()
            exit()
        elif head.y > HEIGHT // BLOCK_SIZE - 1:
            pygame.quit()
            exit()
        elif head.y < 0:
            pygame.quit()
            exit()
    def check_collision(self, food):
        if self.points[0].x != food.x:
            return False
        if self.points[0].y != food.y:
            return False
        return True
running = True
snake = Snake()
food = Food(5, 5)
dx, dy = 0, 0
while running:
    SCREEN.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if SIDE != "DOWN":
                    dx, dy = 0, -3
                    SIDE = "UP"
            elif event.key == pygame.K_DOWN:
                if SIDE != "UP":
                    dx, dy = 0, +3
                    SIDE = "DOWN"
            elif event.key == pygame.K_LEFT:
                if SIDE != "RIGHT":
                    dx, dy = -3, 0
                    SIDE = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if SIDE != "LEFT":
                    dx, dy = +3, 0
                    SIDE = "RIGHT"
    snake.move(dx, dy)
    if snake.check_collision(food) == True:
        snake.points.append(Point(food.x, food.y))
        food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
        food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
        cnt += 1
        if cnt % 3 == 0:
            fps += 5
            lvl += 1
    score_str = font_score.render("Scores:", True, (255,255,0))
    SCREEN.blit(score_str, (10,0))
    score = font_score.render(str(cnt), True, (255,255,0))
    SCREEN.blit(score, (130,0))
    level_str = font_score.render("Level:", True, (0,255,0))
    SCREEN.blit(level_str, (665,0))
    level = font_score.render(str(lvl), True, (0,255,0))
    SCREEN.blit(level, (760,0))
    food.update()
    snake.update()
    pygame.display.flip()
    clock.tick(fps)