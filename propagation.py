from probabilites import *
from random import *
from depart_feu import depart
import numpy as np
from paysage import grille


def voisins(foret, i, j):
    """
    renvoie la liste des voisins en feu de (i,j) ,chaque voisin représenté par la direction voisin->(i,j)
    """
    L, n, p = [], len(foret), len(foret[0])
    if (i, j) == (0, 0):  # d'abord, on traite le cas des 4 coins
        if foret[0, 1, 0]:
            L.append('g')
        if foret[1, 0, 0]:
            L.append('h')
        if foret[1, 1, 0]:
            L.append('hg')
    elif (i, j) == (0, p-1):
        if foret[0, p-2, 0]:
            L.append('d')
        if foret[1, p-1, 0]:
            L.append('h')
        if foret[1, p-2, 0]:
            L.append('hd')
    elif (i, j) == (n-1, 0):
        if foret[n-1, 1, 0]:
            L.append('g')
        if foret[n-2, 0, 0]:
            L.append('b')
        if foret[n-2, 1, 0]:
            L.append('bg')
    elif (i, j) == (n-1, p-1):
        if foret[n-2, p-1, 0]:
            L.append('b')
        if foret[n-1, p-2, 0]:
            L.append('d')
        if foret[n-2, p-2, 0]:
            L.append('hd')
    elif i == 0:  # ensuite les 4 bords
        if foret[0, j-1, 0]:
            L.append('d')
        if foret[0, j+1, 0]:
            L.append('g')
        if foret[1, j, 0]:
            L.append('h')
        if foret[1, j-1, 0]:
            L.append('hd')
        if foret[1, j+1, 0]:
            L.append('hg')
    elif i == n-1:
        if foret[n-1, j-1, 0]:
            L.append('d')
        if foret[n-1, j+1, 0]:
            L.append('g')
        if foret[n-2, j, 0]:
            L.append('b')
        if foret[n-2, j-1, 0]:
            L.append('bd')
        if foret[n-2, j+1, 0]:
            L.append('bg')
    elif j == 0:
        if foret[i-1, 0, 0]:
            L.append('b')
        if foret[i+1, 0, 0]:
            L.append('h')
        if foret[i, 1, 0]:
            L.append('g')
        if foret[i-1, 1, 0]:
            L.append('bg')
        if foret[i+1, 1, 0]:
            L.append('hg')
    elif j == p-1:
        if foret[i-1, p-1, 0]:
            L.append('b')
        if foret[i+1, p-1, 0]:
            L.append('h')
        if foret[i, p-2, 0]:
            L.append('d')
        if foret[i-1, p-2, 0]:
            L.append('bd')
        if foret[i+1, p-2, 0]:
            L.append('hd')
    else:  # enfin le cas général
        if foret[i-1, j, 0]:
            L.append('b')
        if foret[i+1, j, 0]:
            L.append('h')
        if foret[i, j-1, 0]:
            L.append('d')
        if foret[i, j+1, 0]:
            L.append('g')
        if foret[i-1, j-1, 0]:
            L.append('bd')
        if foret[i-1, j+1, 0]:
            L.append('bg')
        if foret[i+1, j-1, 0]:
            L.append('hd')
        if foret[i+1, j+1, 0]:
            L.append('hg')
    return L

# fonction qui modifie l'état d'une case en fonction de ses voisins en feu:


def propagation(forest, i, j, V=(0, 0), Vmax=100):

    foret = forest.copy()

    if foret[i, j][0] == 0:

        p = probabilité_de_combustion[foret[i, j, 1]]

        for case in voisins(foret, i, j):
            # on traite tout les cas ( position de la case concerné par rapport à la case voisine en feu et la direction du vent)
            # --> déterminer le coefficient de l'effet du vent sur la propagation.
            if ((case == 'h') and (V[1] >= 0)) or ((case == 'b') and (V[1] < 0)):
                # simulation d'une épreuve de Bernoulli de paramètre p * facteur du vent
                t = random()
                if t < (p*fact_vent_y_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

            if ((case == 'h') and (V[1] < 0)) or ((case == 'b') and (V[1] >= 0)):
                t = random()
                if t < (p*fact_vent_y_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

            if ((case == 'g') and (V[0] >= 0)) or ((case == 'd') and (V[0] < 0)):
                t = random()
                if t < (p*fact_vent_x_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

            if ((case == 'g') and (V[0] < 0)) or ((case == 'd') and (V[0] >= 0)):
                t = random()
                if t < (p*fact_vent_x_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

            if ((case == 'hg') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'bd') and (V[0] <= 0) and (V[1] < 0)) or ((case == 'hd') and (V[0] <= 0) and (V[1] > 0)) or ((case == 'bg') and (V[0] >= 0) and (V[1] < 0)):
                t = random()
                if t < (p*fact_vent_y_plus(V, Vmax, foret[i, j][1])*fact_vent_x_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

            if ((case == 'hd') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'bg') and (V[0] < 0) and (V[1] <= 0)) or ((case == 'hg') and (V[0] < 0) and (V[1] >= 0)) or ((case == 'bd') and (V[0] > 0) and (V[1] <= 0)):
                t = random()
                if t < (p*fact_vent_y_plus(V, Vmax, foret[i, j][1])*fact_vent_x_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

            if ((case == 'bg') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'hd') and (V[0] <= 0) and (V[1] < 0)) or ((case == 'hg') and (V[0] >= 0) and (V[1] < 0)) or ((case == 'bd') and (V[0] <= 0) and (V[1] > 0)):
                t = random()
                if t < (p*fact_vent_y_moins(V, Vmax, foret[i, j][1])*fact_vent_x_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

            if ((case == 'bd') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'hg') and (V[0] < 0) and (V[1] < 0)) or ((case == 'hd') and (V[0] > 0) and (V[1] < 0)) or ((case == 'bg') and (V[0] < 0) and (V[1] > 0)):
                t = random()
                if t < (p*fact_vent_y_moins(V, Vmax, foret[i, j][1])*fact_vent_x_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1]]

    else:

        p = probabilité_feu_eteint[foret[i, j][1]]

        t = random()
        if (t < p) and (foret[i, j, 1] in {1, 2, 3}):
            # si non rocher et non eau, se transforme en cendres
            return [0, 0]
        else:
            # si rocher, feu s'eteint
            foret[i, j] = [0, foret[i, j, 1]]

    return foret[i, j]
