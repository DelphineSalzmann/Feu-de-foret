from paysage import grille, paysage
import numpy as np


def test_grille():
    G = grille()
    assert G[16][18][1] == 3
    assert G[15][17][1] == 4
    assert type(G[10][10]) == np.ndarray


def test_paysage():
    grid = grille()
    print(grid)
    paysage(grid)
    #rep = input("Les résultats correspondent-ils ? [y/n]")
    #assert rep


if __name__ == "__main__":
    test_grille()
    test_paysage()
