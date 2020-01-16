# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 15:19:21 2020

@author: mathis.vigier
"""

import pygame

pygame.init()

t=50
H=850
L=850

ecran = pygame.display.set_mode((H ,L))

fond = pygame.image.load("fond.png").convert_alpha()
point = pygame.image.load("rond multicolor.png").convert_alpha()

#ecran.blit(fond, (0,0))

liste_wall = []
with open('lvl1.txt', "r") as file:
    for u,line in enumerate(file):
        u = u * p
        for c,carac in enumerate(line):
            c = c * p
            if carac=="-":
                ecran.blit(point, (c,u))
                #print (carac,(x,y))
                liste_wall.append((c, u))
pygame.display.flip()

continuer = 1

while continuer :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

pygame.quit()




