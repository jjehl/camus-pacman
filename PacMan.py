# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 13:08:56 2020

@author: mathis.vigier
"""

import pygame as pg

fenetre = pg.display.set_mode((500, 500))

perso = pg.image.load("PacMan.png").convert_alpha()
position_perso = perso.get_rect()
position_perso.x = 200
position_perso.y = 200

fenetre.blit(perso, position_perso)
pg.display.flip()


continuer = 1
while continuer :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            continuer = 0

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:    #Si "flèche bas"
                    #On descend le perso
                position_perso = position_perso.move(0,3)
            if event.key == pg.K_UP:    #Si "flèche haut"
                        #On monte le perso
                position_perso = position_perso.move(0,-3)
            if event.key == pg.K_RIGHT:    #Si "flèche droite"
                        #On descend le perso
                position_perso = position_perso.move(3,0)
            if event.key == pg.K_LEFT:    #Si "flèche gauche"
                        #On descend le perso
                position_perso = position_perso.move(-3,0)
        
        
        fenetre.fill((0,0,0))
        #Re-collage
        fenetre.blit(perso, position_perso)
    
        #Rafraichissement
        pg.display.flip()

pg.quit()
