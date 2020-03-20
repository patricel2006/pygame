import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.fill((255, 0, 0))

    pygame.draw.rect(screen, (0, 0, 255), [50, 50, 100, 100])

    pygame.display.flip()