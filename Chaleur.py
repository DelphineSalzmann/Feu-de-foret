import numpy as np
from tkinter import *
from random import *
from probabilites import *
from depart_feu import depart
from pluie import effet_pluie
from propagation import voisins


def grille_c():
    G = np.zeros((20, 20, 3), dtype=np.uint8)
    for i in range(len(G)):
        for j in range(len(G[0])):
            G[i][j][0] = 0  # état initial: pas de feu
            G[i][j][2] = 0  # chaleur initialisé à 0
            a = random()
            if a < 0.1:
                G[i][j][1] = 5
            elif a > 0.45:
                G[i][j][1] = 1
            else:
                G[i][j][1] = 2
    # A la main on modèle le paysage
    G[18][18][1] = 3
    G[18][17][1] = 3
    G[16][18][1] = 3
    G[17][19][1] = 3
    G[15][17][1] = 4

    return G


cote = 40  # côté d'une cellule


def paysage_c(config):  # config est une matrice (lgr,lgr,3)
    root = Tk()
    root.title("Propagation d'un feu de forêt")
    dim = config.shape
    lgr = dim[0]  # nombre de cellules par ligne
    lgr_pix = lgr * cote  # nombre de pixels par ligne
    can = Canvas(root, bg='white', width=lgr_pix, height=lgr_pix)
    for i in range(lgr):
        can.create_line(0, i * cote, lgr_pix, i * cote, fill='black', width=1)
        can.create_line(i * cote, 0, i * cote, lgr_pix, fill='black', width=1)

    for i in range(lgr):
        for j in range(lgr):
            etat = config[i][j][0]
            type = config[i][j][1]
            chaleur = config[i][j][2]
            if etat == 1:  # l'arbre brûle
                can.create_rectangle(cote * j, cote * i,
                                     cote * (j+1), cote * (i+1), fill="red")
            elif chaleur > 0:  # la case ne brule pas mais elle est chaude
                can.create_rectangle(cote * j, cote * i,
                                     cote * (j+1), cote * (i+1), fill="orange")
            else:  # l'arbre ne brûle pas ou plus
                if type == 0:  # cendre
                    can.create_rectangle(
                        cote * j, cote * i, cote * (j+1), cote * (i+1), fill="black")
                if type == 1:  # arbre
                    can.create_rectangle(
                        cote * j, cote * i, cote * (j+1), cote * (i+1), fill='#024701')
                if type == 2:  # herbe sèche
                    can.create_rectangle(
                        cote * j, cote * i, cote * (j+1), cote * (i+1), fill="#55FF52")
                if type == 3:  # maison
                    can.create_rectangle(
                        cote * j, cote * i, cote * (j+1), cote * (i+1), fill="#835B07")
                if type == 4:  # eau
                    can.create_rectangle(
                        cote * j, cote * i, cote * (j+1), cote * (i+1), fill="blue")
                if type == 5:  # rocher
                    can.create_rectangle(
                        cote * j, cote * i, cote * (j+1), cote * (i+1), fill="grey")

    can.grid()
    root.mainloop()


def propagation_c(Wald, i, j, V=(0, 0), Vmax=100):

    foret = Wald.copy()

    if foret[i, j][0] == 0:

        p = min(
            probabilité_de_combustion[foret[i, j, 1]]*(1+(foret[i, j, 2]/5)), 1)

        for case in voisins(foret, i, j):
            # on traite tout les cas ( position de la case concerné par rapport à la case voisine en feu et la direction du vent)
            # --> déterminer le coefficient de l'effet du vent sur la propagation.
            if ((case == 'h') and (V[1] >= 0)) or ((case == 'b') and (V[1] < 0)):
                # simulation d'une épreuve de Bernoulli de paramètre p * facteur du vent
                t = random()
                if t < (p*fact_vent_y_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    # la chaleur augmente lorsque des voisins sont en feu
                    foret[i, j, 2] += 1

            if ((case == 'h') and (V[1] < 0)) or ((case == 'b') and (V[1] >= 0)):
                t = random()
                if t < (p*fact_vent_y_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    foret[i, j, 2] += 1

            if ((case == 'g') and (V[0] >= 0)) or ((case == 'd') and (V[0] < 0)):
                t = random()
                if t < (p*fact_vent_x_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    foret[i, j, 2] += 1

            if ((case == 'g') and (V[0] < 0)) or ((case == 'd') and (V[0] >= 0)):
                t = random()
                if t < (p*fact_vent_x_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    foret[i, j, 2] += 1

            if ((case == 'hg') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'bd') and (V[0] <= 0) and (V[1] < 0)) or ((case == 'hd') and (V[0] <= 0) and (V[1] > 0)) or ((case == 'bg') and (V[0] >= 0) and (V[1] < 0)):
                t = random()
                if t < (p*fact_vent_y_plus(V, Vmax, foret[i, j][1])*fact_vent_x_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    foret[i, j, 2] += 1

            if ((case == 'hd') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'bg') and (V[0] < 0) and (V[1] <= 0)) or ((case == 'hg') and (V[0] < 0) and (V[1] >= 0)) or ((case == 'bd') and (V[0] > 0) and (V[1] <= 0)):
                t = random()
                if t < (p*fact_vent_y_plus(V, Vmax, foret[i, j][1])*fact_vent_x_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    foret[i, j, 2] += 1

            if ((case == 'bg') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'hd') and (V[0] <= 0) and (V[1] < 0)) or ((case == 'hg') and (V[0] >= 0) and (V[1] < 0)) or ((case == 'bd') and (V[0] <= 0) and (V[1] > 0)):
                t = random()
                if t < (p*fact_vent_y_moins(V, Vmax, foret[i, j][1])*fact_vent_x_moins(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    foret[i, j, 2] += 1

            if ((case == 'bd') and (V[0] >= 0) and (V[1] >= 0)) or ((case == 'hg') and (V[0] < 0) and (V[1] < 0)) or ((case == 'hd') and (V[0] > 0) and (V[1] < 0)) or ((case == 'bg') and (V[0] < 0) and (V[1] > 0)):
                t = random()
                if t < (p*fact_vent_y_moins(V, Vmax, foret[i, j][1])*fact_vent_x_plus(V, Vmax, foret[i, j][1])):
                    return [1, foret[i, j][1], foret[i, j][2]]
                elif p > 0:
                    foret[i, j, 2] += 1

        if len(voisins(foret, i, j)) == 0:
            # si pas de voisins en feu, la chaleur diminue
            foret[i, j, 2] = max(0, foret[i, j, 2]-1)


    else:

        p = probabilité_feu_eteint[foret[i, j][1]]

        t = random()
        if (foret[i, j, 1] in {1, 2, 3}):
            if t < p :
                # si non rocher et non eau, se transforme en cendres
                return [0, 0, 0]
        else:
            # si rocher, feu s'eteint mais reste chaud
            foret[i, j] = [0, foret[i, j, 1], 2]

    return foret[i, j]


def generation_suivante_c(foret, pluie, vent=(0, 0)):
    """
    prend en argument une grille et renvoie la forêt à la génération suivante
    """
    effet_pluie(foret, pluie)
    return np.array([[propagation_c(foret, x, y, vent) for y in range(len(foret[0]))] for x in range(len(foret))])


def evolution_c(foret, pluie, vent=(0, 0)):
    F2 = foret.copy()
    paysage_c(F2)
    continuer = True
    while continuer:
        F2 = generation_suivante_c(F2, pluie, vent)
        paysage_c(F2)
        continuer = False
        for i in range(len(foret)):
            if not continuer:
                for j in range(len(foret[0])):
                    if F2[i, j, 0] or F2[i, j, 2] > 0:
                        # la simulation ne s'arrete pas lorsqu'il y a encore des cases en feu ou bien des cases chaudes.
                        continuer = True
                        break
            else:
                break


if __name__ == "__main__":
     evolution_c(depart(np.array([[[0, 1, 0] for y in range(5)]
               for x in range(5)], dtype=np.uint8), 2, 2), pluie=0.1*np.ones((5, 5)))
