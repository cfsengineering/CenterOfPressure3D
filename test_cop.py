
import numpy as np
from pytest import approx

from cop import calculate_minimal_moment, find_antother_point_on_copline


def test_cop():
     
    # Test1 : simple values
    
    Mref = np.array([0., 0., 1.])
    F = np.array([0., 1., 1.])
    Pref = np.array([1., 0., 0.])
    
    Px = calculate_minimal_moment(F, Mref, Pref)
    
    assert Px[0] == approx(1.49995, 1e-5)
    assert Px[1] == 0
    assert Px[2] == 0
    
    Pcop, msg = find_antother_point_on_copline(Px, F, "x")
    assert msg == "Center of pressure line is parallel to the x plane"
    
    Pcop, msg = find_antother_point_on_copline(Px, F, "y")
    print(Pcop)
    assert msg == ""
    assert Pcop[0] == approx(1.49995, 1e-5)
    assert Pcop[1] == 0
    assert Pcop[2] == 0
    
    Pcop, msg = find_antother_point_on_copline(Px, F, "z")
    print(Pcop)
    assert msg == ""
    assert Pcop[0] == approx(1.49995, 1e-5)
    assert Pcop[1] == 0
    assert Pcop[2] == 0
    
    # Test 2 : complex values

    Mref = np.array([27406144, -56507355, 7762585])
    F = np.array([229793, 395290, 1609545])
    Pref = np.array([0., 0., 0.])
    
    Px = calculate_minimal_moment(F, Mref, Pref)
    Pcop, msg = find_antother_point_on_copline(Px, F, "z")

    assert msg == ""
    assert Pcop[0] == approx(34.7967, 1e-5)
    assert Pcop[1] == approx(17.2080, 1e-5)
    assert Pcop[2] == 0
    