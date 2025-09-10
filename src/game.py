import pygame
import main

pygame.init()
naytto = pygame.display.set_mode((400, 400))
naytto.fill((0,0,0))

green = (0, 255, 0)

for room in main.rooms:
    pygame.draw.rect(naytto, green, room.get_rect(20))

pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()