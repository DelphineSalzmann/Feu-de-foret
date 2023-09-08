import numpy as np
import random as rd
import numpy.random as nr


def début_pluie(n=20, m=20, intensité=1, x=0, y=0, taille=(3, 3)):
    """
    n et m représentent les dimensions du tableau, x et y une position de départ du nuage.
    taille représente les dimensions du nuage
    """
    pluie = np.zeros((n, m))
    for i in range(x, x+taille[0]):
        for j in range(y, y+taille[1]):
            pluie[i, j] = intensité
    return pluie


def évolution_pluie_vent(pluie, vent=(0, 0)):
    """
    effectue les modifications dues à la pluie, renvoie un nouveau tableau
    """
    (n, m) = np.shape(pluie)
    a, b = int(vent[0]/40), int(vent[1]/40)
    nouv_pluie = np.zeros((n, m))
    for j in range(max(0, a), m+min(a, 0)):
        for i in range(max(0, -b), n+min(-b, 0)):
            nouv_pluie[i, j] = pluie[i+b, j-a]
    return nouv_pluie


def évolution_pluie_spontanée(pluie):
    """
    effectue l'évoolution aléatoire, ne renvoie rien
    """
    for i in range(len(pluie)):
        for j in range(len(pluie[0])):
            a = (rd.random()-0.5)/10
            pluie[i, j] = max(0, min(1, pluie[i, j]+a))


def évolution_pluie(pl, vent=(0, 0)):
    """
    prend la pluie à la génération n, la renvoie à la génération n+1
    """
    p = évolution_pluie_vent(pl, vent)
    # évolution_pluie_spontanée(p)
    return p


def effet_pluie(foret, pluie):
    """
    éteint le feu ou humidifie l'herbe si la pluie est assez intense
    """
    n, m = len(foret), len(foret[0])
    assert (n, m) == (np.shape(pluie)[0], np.shape(pluie)[
        1]), "les 2 tableaux n'ont pas la même dimension"
    for i in range(n):
        for j in range(m):
            if foret[i, j, 0]:
                if nr.binomial(1, pluie[i, j]):
                    foret[i, j] = [0, 0, 0]
            else:
                if nr.binomial(1,pluie[i,j]):
                    foret[i, j] = [0, foret[i, j, 1], 0]