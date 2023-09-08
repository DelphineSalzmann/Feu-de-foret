from propagation import *
import numpy as np
from random import *
from depart_feu import *
from Chaleur import *


def test_voisins():
    foret = np.array([[[0, 3, 0] for y in range(3)] for x in range(3)])
    assert (set(voisins(depart(depart(foret, 0, 0), 2, 1), 1, 1))
            == {'bd', 'h'})


def test_propagation_c():
    seed(1)
    paysage_c(depart(np.array([[[0, 3, 0] for y in range(3)]
                               for x in range(3)]), 0, 1))
    print(propagation_c(depart(
        np.array([[[0, 3, 0] for y in range(3)] for x in range(3)]), 0, 1), 1, 1))
    assert np.array(np.array(propagation_c(depart(np.array([[[0, 3, 0] for y in range(
        3)] for x in range(3)]), 0, 1), 1, 1)) == np.array([1, 3, 0])).any()


test_voisins()
test_propagation_c()
