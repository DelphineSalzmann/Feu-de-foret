from depart_feu import *
import numpy as np

def test_depart():
    test_equality = np.array(depart(np.array([[[0,3] for y in range(3)] for x in range(3)],dtype=np.uint8),0,1) == np.array([[[0,3],[1,3],[0,3]],[[0,3],[0,3],[0,3]],[[0,3],[0,3],[0,3]]],dtype=np.uint8))
    assert(test_equality.all())

test_depart()