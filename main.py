import pygame
from pygame.locals import *

root = pygame.display.set_mode((640, 480))
pygame.display.set_caption('CLICK_FIG')

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                root.fill((0, 0, 0))
                pygame.draw.circle(root, (225, 0, 50), i.pos, 20)
                pygame.display.update()
            elif i.button == 3:
                root.fill((0, 0, 0))
                pygame.draw.circle(root, (0, 0, 225), i.pos, 20)
                pygame.draw.rect(root, (0, 225, 0), (i.pos[0] - 10, i.pos[1] - 10, 20, 20))
                pygame.display.update()


pygame.quit()
