# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

              #fenetre https://zestedesavoir.com/tutoriels/846/pygame-pour-les-zesteurs/1381_a-la-decouverte-de-pygame/creer-une-simple-fenetre-personnalisable/


import pygame

pygame.init()

p=50
t=50
H=850
L=850

ecran = pygame.display.set_mode((H ,L))
fond = pygame.image.load("fond.png").convert_alpha()
wall = pygame.image.load("wall.png").convert_alpha()

ecran.blit(fond, (0,0))

liste_tab = []
tab = []
liste_wall = []

with open('lvl1.txt', "r") as file:
    for y,line in enumerate(file):
        y = y * t
        for x,carac in enumerate(line):
            x = x * t
            if carac=="o":
                liste_tab.append(1)
                ecran.blit(wall, (x,y))
                print (carac,(x,y))
                liste_wall.append((x, y))   
            else:
                liste_tab.append(0)
        print (liste_tab)
        tab.append(liste_tab)

pygame.display.flip()
continuer = 1

while continuer :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

pygame.quit()








































class Board (object):
    def __init__(self,size):
        self.size=size

