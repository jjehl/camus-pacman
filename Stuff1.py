# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
class Stuff (object):
    def __init__(self):
      self.locate=[]
        
    def addstuff(self,x,y,look):
        self.locate.append((x,y,look))

         
stuff1=Stuff()

stuff1.addstuff(3,3,"fraise")
stuff1.addstuff(5,5,"banane")


i = 0
for element in stuff1.locate:
    element[0]
    i=i+1
    print("element",i)
    print(element[0],(","),element[1])
    
    
import random
import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame

p=50
t=50
H=850
L=850

ecran = pygame.display.set_mode((H ,L))

#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
fraise = pygame.image.load("fraise3.png")
banane = pygame.image.load("banane.png")
lampe = pygame.image.load("lampe.png")
fond = pygame.image.load("fond.png").convert_alpha()

multicolor1 = pygame.image.load("rond multicolor1.png").convert_alpha()


random.seed()
liste_test = []
with open('lvl1.txt', "r") as file:
    for o,line in enumerate(file):
        o = o * p
        for n,carac in enumerate(line):
            n = n * p
            if carac=="-":
                ecran.blit(multicolor1, (n,o))
                #print (carac,(x,y))
                liste_test.append((n,o))


wall = pygame.image.load("wall.png").convert_alpha()

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

continuer = 1
liste_fraise = []

random.seed()
r = random.randint(1, 17)*50
i = random.randint(1, 17)*50

while continuer :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0

position_perso = perso.get_rect()
position_fraise = fraise.get_rect()
position_banane = banane.get_rect()
position_lampe = lampe.get_rect()
position_fraise.y = r
position_fraise.x = i
position_banane.x = 360
position_banane.y = 300
position_lampe.x = 320
position_lampe.y = 240
ecran.blit(perso, position_perso)
ecran.blit(fraise,position_fraise)
ecran.blit(banane,position_banane)
ecran.blit(lampe,position_lampe)
#Rafraîchissement de l'écran
pygame.display.flip()

pygame.key.set_repeat(10,10)
#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():    #Attente des événements
        if event.type == pygame.QUIT:
            continuer = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:    #Si "flèche bas"
                #On descend le perso
                position_perso = position_perso.move(0,3)
            if event.key == pygame.K_UP:    #Si "flèche haut"
                #On monte le perso
                position_perso = position_perso.move(0,-3)
            if event.key == pygame.K_RIGHT:    #Si "flèche droite"
                #On descend le perso
                position_perso = position_perso.move(3,0)
            if event.key == pygame.K_LEFT:    #Si "flèche gauche"
                #On descend le perso
                position_perso = position_perso.move(-3,0)
    
    
    #Re-collage
    ecran.blit(perso, position_perso)
    ecran.blit(fraise,position_fraise)
    ecran.blit(banane,position_banane)
    ecran.blit(lampe,position_lampe)
    #Rafraichissement
    pygame.display.flip()
    

pygame.quit()

  