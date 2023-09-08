import numpy as np
import random as rd
from depart_feu import *
from propagation import propagation
from paysage import paysage
from pluie import effet_pluie


def generation_suivante(forêt,pluie,vent=(0, 0)):
    """
    prend en argument une grille et renvoie la forêt à la génération suivante
    """
    effet_pluie(forêt, pluie)
    return np.array([[propagation(forêt, x, y, vent) for y in range(len(forêt[0]))] for x in range(len(forêt))])
