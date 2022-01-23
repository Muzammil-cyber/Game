import pygame

pygame.init()
main = pygame.display.set_mode((600,400))

pygame.display.set_caption("Space Raiders","pew pew")
logo = pygame.image.load("ufo.png")
pygame.display.set_icon(logo)


running = True
while running:
    main.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

