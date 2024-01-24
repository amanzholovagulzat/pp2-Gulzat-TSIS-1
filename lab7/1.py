import pygame
import datetime

pygame.init()

size = w,h = (1400, 1050)

time = datetime.datetime.now()

# angle = -(int(time.strftime("%S")) * 6) - 6
# angleM = -(int(time.strftime("%M")) * 6) + (int(time.strftime("%S")) * 6 / 60) - 54

angle = -(int(time.strftime("%S")) * 6) - 6#pchsvminus
angleM = -(int(time.strftime("%M")) * 6 + (int(time.strftime("%S")) * 6 / 60)) - 54

def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center = rect.center)
    return new_image, rect

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Mickey clock')

mickey = pygame.image.load('images/clock.jpeg')
seconds = pygame.image.load('images/hl.jpeg')
minutes = pygame.image.load('images/hr.jpeg')

imagem = pygame.Surface(size, pygame.SRCALPHA)#surface-поверзностьбчтобы можно было двигать относитюдругдруга
imagem.blit(minutes, (450, 290))
newm = imagem
rectm = imagem.get_rect(center = (w//2, h//2))

image = pygame.Surface((63, h), pygame.SRCALPHA)
image.blit(seconds, (0, 0))
new = image
rect = image.get_rect(center = (635, 465))

clock = pygame.time.Clock()
done = False

FPS = 60

while not done:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(mickey, (0, 0))
    screen.blit(image, rect)
    screen.blit(imagem, rectm)

    image, rect = rotate(new, rect, angle)
    imagem, rectm = rotate(newm, rectm, angleM)

    angle -= 0.099
    angleM -= 0.099/60

    pygame.display.update()
pygame.quit()