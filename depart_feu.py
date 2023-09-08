import numpy as np
from paysage import paysage, grille

# La fonction départ() prend en entrée la foret et les coord. de la case de départ de feu et renvoie la matrice modifiée
# La fonction depart_feu() prend en entrée la foret et les coord. case de départ de feu et affiche la foret modifiée (utilisation de depart + paysage)


def depart(forêt, x, y):
    f = forêt.copy()
    f[x, y, 0] = 1
    return f


def depart_feu(foret, x, y):
    paysage(depart(foret, x, y))


if __name__ == "__main__":
    depart_feu(np.zeros((3, 3, 3)), 0, 1)
    assert (depart(np.zeros((3, 3, 3)), 0, 1) == np.array(
        [[[0, 0, 0], [1, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]])).all()
