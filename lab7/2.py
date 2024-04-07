import pygame
pygame.init()
Width, Height = 500,500
x,y = 50,50
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock()
current_song = 0
l = ["lab7/1.mp3", 
     "lab7/2.mp3",
     "lab7/3.mp3"]
pygame.mixer.music.load(l[current_song])
pygame.mixer.music.play()
running = True
while running:
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_song  = (current_song + 1) % (len(l))
                pygame.mixer.music.load(l[current_song])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                current_song = (current_song - 1) % (len(l))
            pygame.mixer.music.load(l[current_song])
            pygame.mixer.music.play()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_s]:
        pygame.mixer.music.pause()
    if pressed[pygame.K_c]:
        pygame.mixer.music.unpause()
    pygame.display.flip()