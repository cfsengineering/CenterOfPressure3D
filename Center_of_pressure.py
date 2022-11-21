from cop import calculate_minimal_moment, find_another_point_on_cop_line
import streamlit as st
import numpy as np


st.title("Center of pressure 3D")
st.markdown("Find the aerodynamic center of pressure by giving the total moment, "
            "the total force and the point where it is applied. Units are not defined, "
            "but moment, force and length must be consistent with each other.")

st.markdown("### Moment")

col_Mx, col_My, col_Mz = st.columns(3)
with col_Mx:
    Mx = st.number_input("Mx",value=0.0,help="x component of the total moment")
with col_My:
    My = st.number_input("My",value=0.0,help="y component of the total moment")
with col_Mz:
    Mz = st.number_input("Mz",value=0.0,help="z component of the total moment")

st.markdown("### Force")

col_Fx, col_Fy, col_Fz = st.columns(3)
with col_Fx:
    Fx = st.number_input("Fx",value=0.0,help="x component of the total force")
with col_Fy:
    Fy = st.number_input("Fy",value=0.0,help="y component of the total force")
with col_Fz:
    Fz = st.number_input("Fz",value=0.0,help="z component of the total force")
    
st.markdown("### Point of reference")

col_x, col_y, col_z = st.columns(3)
with col_x:
    x = st.number_input("x",value=0.0, help="Point of reference in x")
with col_y:
    y = st.number_input("y",value=0.0,help="Point of reference in y")
with col_z:
    z = st.number_input("z",value=0.0,help="Point of reference in z")
    
st.markdown("### Center of pressure")
st.markdown("In 3D the center of pressure is a line")
st.markdown("If you set a plane to 0 (e.g. the symmetry plane) you can get a point which correspond to your center of pressure.")

F = np.array([Fx, Fy, Fz])
Mref = np.array([Mx, My, Mz])
Pref = np.array([x, y, z])

plane = st.selectbox("Set a plane to 0:",("x","y","z"))

st.markdown(f"With {plane} set to 0, your center of pressure is")

print(F)
print(Mref)
print(Pref)


res = calculate_minimal_moment(F, Mref, Pref)
print(res)
point, msg = find_another_point_on_cop_line(res, F, plane)

if msg:
    st.warning(msg)
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("x", f"{point[0]:.4f}")
    col2.metric("y", f"{point[1]:.4f}")
    col3.metric("z", f"{point[2]:.4f}")
