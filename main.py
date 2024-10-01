import pygame
from pygame.locals import *


root = pygame.display.set_mode((700, 700))
pygame.display.set_caption('CLICK_FIG')
pygame.display.update()

r_ps = None
l_ps = None

run = True
while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                r_ps = i.pos
            if i.button == 3:
                l_ps = i.pos

        root.fill((0, 0, 0))
        if r_ps is not None:
            pygame.draw.circle(root, (225, 0, 50), r_ps, 20)
            pygame.display.update()

        if l_ps is not None:
            pygame.draw.circle(root, (0, 0, 225), l_ps, 20)
            pygame.draw.rect(root, (0, 225, 0), (l_ps[0] - 10, l_ps[1] - 10, 20, 20))
            pygame.display.update()


pygame.quit()
