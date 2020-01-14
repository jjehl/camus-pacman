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
    
    

import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))


#Chargement et collage du personnage
perso = pygame.image.load("perso.png").convert_alpha()
fraise = pygame.image.load("fraise3.png")
banane = pygame.image.load("banane.png")
lampe = pygame.image.load("lampe.png")
position_perso = perso.get_rect()
position_fraise = fraise.get_rect()
position_banane = banane.get_rect()
position_lampe = lampe.get_rect()
position_fraise.y = 300
position_fraise.x = 280
position_banane.x = 360
position_banane.y = 300
position_lampe.x = 320
position_lampe.y = 240
fenetre.blit(perso, position_perso)
fenetre.blit(fraise,position_fraise)
fenetre.blit(banane,position_banane)
fenetre.blit(lampe,position_lampe)
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
    
    
    fenetre.fill((150,0,255))
    #Re-collage
    fenetre.blit(perso, position_perso)
    fenetre.blit(fraise,position_fraise)
    fenetre.blit(banane,position_banane)
    fenetre.blit(lampe,position_lampe)
    #Rafraichissement
    pygame.display.flip()
    

pygame.quit()

  