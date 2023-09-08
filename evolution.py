import numpy as np
from random import *
from generation import generation_suivante
from paysage import paysage
from depart_feu import depart, depart_feu
from paysage import grille
from pluie import début_pluie


def evolution(foret, pluie, vent=(0, 0)):
    F2 = foret.copy()
    paysage(F2)
    continuer = True
    while continuer:
        F2 = generation_suivante(F2, pluie, vent)
        paysage(F2)
        continuer = False
        for i in range(len(foret)):
            if not continuer:
                for j in range(len(foret[0])):
                    if F2[i, j, 0]:
                        # la simulation ne s'arrete pas lorsqu'il y a encore des cases en feu.
                        continuer = True
                        break
            else:
                break


if __name__ == "__main__":
    evolution(depart(np.array([[[0, 1, 0] for y in range(5)]
              for x in range(5)], dtype=np.uint8), 2, 2), pluie=0.1*np.ones((5, 5)))
