from probabilites import *

def test_fact_vent_x_plus():
    assert(fact_vent_x_plus((0,10), 100, 1) == 1)
    
def test_fact_vent_x_moins():
    assert(fact_vent_x_moins((150,10), 100, 1) == 0)

def test_fact_vent_y_plus():
    assert(fact_vent_y_plus((40,0), 100, 1) == 1)

def test_fact_vent_y_moins():
    assert(fact_vent_y_moins((10,150), 100, 1) == 0)
    
test_fact_vent_x_plus()
test_fact_vent_x_moins()
test_fact_vent_y_plus()
test_fact_vent_y_moins()