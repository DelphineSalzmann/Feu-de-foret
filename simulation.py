# Fonction principale de la simulation

from paysage import grille, paysage
from evolution import evolution
from depart_feu import depart
from Chaleur import *

def simulation(vent, x, y):
    foret = grille_c()
    init = depart(foret, x, y)
    evolution_c(init,np.zeros((20,20)) , vent)


if __name__ == '__main__':
    simulation((0, 0), 5, 6)
