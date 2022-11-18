import streamlit as st
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

def find_antother_point_on_copline(Pcop, plane):
    """Find point on cop line crossing a plane

    Args:
        Pcop (_type_): _description_
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


st.title("Center of pressure 3D")

st.markdown("Find the aerodynamic center of pressure by giving the total moment,"
            "the total force and the point where it is applyied.")

st.markdown("### Moment")

col_Mx, col_My, col_Mz = st.columns(3)

with col_Mx:
    Mx = st.number_input("Mx",value=0.0,help="x componant of the total moment")
with col_My:
    My = st.number_input("My",value=0.0,help="y componant of the total moment")
with col_Mz:
    Mz = st.number_input("Mz",value=0.0,help="z componant of the total moment")
    
    
st.markdown("### Force")

col_Fx, col_Fy, col_Fz = st.columns(3)

with col_Fx:
    Fx = st.number_input("Fx",value=0.0,help="x componant of the total force")
with col_Fy:
    Fy = st.number_input("Fy",value=0.0,help="y componant of the total force")
with col_Fz:
    Fz = st.number_input("Fz",value=0.0,help="z componant of the total force")
    
    
st.markdown("### Point of reference")

col_x, col_y, col_z = st.columns(3)

with col_x:
    x = st.number_input("x",value=0.0, help="Point of reference in x")
with col_y:
    y = st.number_input("y",value=0.0,help="Point of reference in y")
with col_z:
    z = st.number_input("z",value=0.0,help="Point of reference in z")
    
       
F = np.array([Fx, Fy, Fz])
Mref = np.array([Mx, My, Mz])
Pref = np.array([x, y, z])


st.markdown("### Center of pressure")

st.markdown("In 3D the center of pressure is a line")

st.markdown("If you set a plane to 0 (e.g. the symetry plane) you can get a point which correspond to your center of pressure.")

plane = st.selectbox("Set a plane to 0:",("x","y","z"))

st.markdown(f"With {plane} set to 0, your center of pressure is")

res = calculate_minimal_moment(F, Mref, Pref)
point, msg = find_antother_point_on_copline(res, plane)

if msg:
    st.warning(msg)
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("x", f"{point[0]:.4f}")
    col2.metric("y", f"{point[1]:.4f}")
    col3.metric("z", f"{point[2]:.4f}")
