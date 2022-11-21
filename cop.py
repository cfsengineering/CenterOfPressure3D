import numpy as np
from scipy import optimize


def MPref_to_MPx_norm(Px, F, Mref, Pref):
    """Transfer moment of point Pref to point Px and return norm.
    
    Args:
        Px (np.array): Current point
        F (np.array): Total force
        Mref (np.array): Total moment
        Pref (np.array): Point of reference

    Returns:
        Mx_norm: Norm of Mx
    """
    
    r  = Pref - Px
    Mx = Mref + np.cross(r,F)
    Mx_norm = np.linalg.norm(Mx)
    
    return Mx_norm

def calculate_minimal_moment(F, Mref, Pref):
    """Calculate minimal moment by minimizing norm of the moment transfer function

    Args:
        F (np.array): Total force
        Mref (np.array): Total moment
        Pref (np.array): Point of reference

    Returns:
        Px: Point where the moment is minimal
    """

    optimize_result = optimize.minimize(MPref_to_MPx_norm, x0=Pref, args=(F, Mref, Pref), method="CG" ,options={'gtol': 1e-03})
    
    # if (optimize_result.status != 0):
    #     print("Error when calculating point with minimal moment!")
    #     print(optimize_result)

    Px = optimize_result.x

    return Px

def find_antother_point_on_copline(Pcop, F, plane):
    """Find point on cop line crossing a plane

    Args:
        Pcop (_type_): _description_
        F (np.array): Total force
        plane (str): "x","y" of "z" plane

    Returns:
        Pplane: Point of intersection between the cop line and the selected plane
    """
    
    PLANE_2_COMP = {"x":0, "y":1, "z":2}
    plane_comp = PLANE_2_COMP[plane]
    
    if(F[plane_comp] == 0):
        return None, f"Center of pressure line is parallel to the {plane} plane"

    s = - Pcop[plane_comp]/F[plane_comp]
    Pplane = Pcop + s*F
    
    return Pplane, ""