from generation import *
from Chaleur import *
import numpy as np
import random as rd


# def test_generation():
#     rd.seed(1)
#     paysage(depart(np.array([[[0, 3] for y in range(3)]
#             for x in range(3)]), 2, 2))
#     gen_suiv = generation_suivante(
#         depart(np.array([[[0, 3] for y in range(3)] for x in range(3)]), 2, 2), pluie=0.1*np.ones((3, 3)))
#     paysage(gen_suiv)
#     assert ((gen_suiv == np.array([[[0, 3], [0, 3], [0, 3]], [
#             [0, 3], [1, 3], [0, 3]], [[0, 3], [0, 3], [0, 0]]], dtype=np.uint8)).all())


def test_generation_c():
    rd.seed(1)
    paysage_c(depart(np.array([[[0, 3, 0] for y in range(3)]
                               for x in range(3)]), 2, 2))
    gen_suiv = generation_suivante_c(
        depart(np.array([[[0, 3, 0] for y in range(3)] for x in range(3)]), 2, 2), pluie=0.1*np.ones((3, 3)))
    paysage_c(gen_suiv)
    assert np.array(gen_suiv == np.array([[[0, 3, 0], [0, 3, 0], [0, 3, 0]], [
        [0, 3, 0], [1, 3, 0], [0, 3, 1]], [[0, 3, 0], [0, 3, 1], [0, 0, 0]]], dtype=np.uint8)).all()


test_generation_c()
