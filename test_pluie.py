from pluie import *
from random import seed, random

seed('')
for i in range(4):
    a = random()


def test_depart():
    p = début_pluie()
    assert p[1, 1] == 1
    assert p[19, 19] == 0
    assert p[2, 1] == 1
    assert p[3, 2] == 0


def test_evolution_vent():
    p = évolution_pluie_vent(début_pluie(), (-40, 40))
    assert p[2, 1] == 0
    assert p[1, 1] == 1
    assert p[0, 0] == 1
    p = évolution_pluie_vent(début_pluie(), (100, 100))
    assert (p[1] == np.zeros(20)).all()
    assert p[0, 1] == 0
    assert p[0, 2] == 1


def test_évolution_spontané():
    p = début_pluie()
    seed('')
    évolution_pluie_spontanée(p)
    assert p[0, 0] == 1
    assert p[0, 3] == (a-0.5)/10


def test_effet_pluie():
    foret1 = np.array([[[0, 2, 0] for y in range(20)] for x in range(20)])
    foret2 = np.array([[[1, 2, 0] for y in range(20)] for x in range(20)])
    p = début_pluie()
    effet_pluie(foret1, p)
    effet_pluie(foret2, p)
    assert list(foret1[0, 0]) == [0, foret1[0, 0, 1], 0]
    assert list(foret1[3, 2]) == [0, 2, 0]
    assert list(foret2[0, 0]) == [0, 0, 0]
    assert list(foret2[2, 3]) == [1, 2, 0]


test_depart()
test_evolution_vent()
test_évolution_spontané()
test_effet_pluie()
