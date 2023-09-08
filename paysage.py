# La fonction grille() établit le paysage de départ sous forme matricielle
# La fonction paysage() prend en entrée la matrice crée et l'affiche

from tkinter import *
import numpy as np
from random import *


def grille():
    G = np.zeros((20, 20, 2), dtype=np.uint8)
    for i in range(len(G)):
        for j in range(len(G[0])):
            G[i][j][0] = 0  # état initial: pas de feu
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


def paysage(config):  # config est une matrice (lgr,lgr,2)
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
            if etat == 1:  # l'arbre brûle
                can.create_rectangle(cote * j, cote * i,
                                     cote * (j+1), cote * (i+1), fill="red")
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
