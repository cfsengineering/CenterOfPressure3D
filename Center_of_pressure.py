import streamlit as st

st.title("Center of pressure 3D")

st.markdown("Find the aerodynamic center of pressure by giving the total moment,"
            "the total force and the point where it is applyied.")

st.markdown("### Force")

col_Mx, col_My, col_Mz = st.columns(3)

with col_Mx:
    st.number_input("Mx",0.0,help="x componant of the total moment")
with col_My:
    st.number_input("My",0.0,help="y componant of the total moment")
with col_Mz:
    st.number_input("Mz",0.0,help="z componant of the total moment")
    
    
st.markdown("### Moment")

col_Fx, col_Fy, col_Fz = st.columns(3)

with col_Fx:
    st.number_input("Fx",0.0,help="x componant of the total force")
with col_Fy:
    st.number_input("Fy",0.0,help="y componant of the total force")
with col_Fz:
    st.number_input("Fz",0.0,help="z componant of the total force")
    
    
st.markdown("### Point of reference")

col_x, col_y, col_z = st.columns(3)

with col_x:
    st.number_input("x",0.0,help="Point of reference in x")
with col_y:
    st.number_input("y",0.0,help="Point of reference in y")
with col_z:
    st.number_input("z",0.0,help="Point of reference in z")
    

with st.columns([4,2,4])[1]:
    if st.button("**Calculate**"):
        pass
    
st.markdown("### Center of pressure")

st.warning("Not calculated yet.")

st.markdown("In 3D the center of pressure is a line, the equation of this line is: ??")

st.markdown("If you set a plane to 0 (e.g. the symetry plane) you can get a point which correspond to your center of pressure.")

plane = st.selectbox("Set a plane to 0:",("x","y","z"))

st.markdown(f"With {plane} set to 0, your center of pressure is: ??")

