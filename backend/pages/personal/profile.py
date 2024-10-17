import streamlit as st
from datetime import datetime
from PIL import Image

st.title("Profile")

@st.dialog("Chi tiết món ăn", width="large")
def editPersonal():
    new_fullname = st.text_input("Họ và Tên")
    new_dob = st.date_input("Ngày sinh")
    new_weight = st.text_input("Cân nặng (kg)")
    new_height = st.text_input("Chiều cao (cm)")
    new_activity_level = st.selectbox("Tần suất hoạt động", ["Active", "Sometimes", "Inactive"])
    uploaded_image = st.file_uploader("Avatar của bạn", type=["jpg", "jpeg", "png"])

    register_button = st.button("Chỉnh sửa", type="primary", use_container_width=True)

    if register_button:
            st.session_state.fullname = new_fullname
            st.session_state.dob = new_dob.strftime("%d-%m-%Y")
            st.session_state.weight = new_weight
            st.session_state.height = new_height
            st.session_state.activity_level = new_activity_level
            if uploaded_image is not None:
                st.session_state.avatar = uploaded_image
            st.rerun()


col1, col2 = st.columns([31, 69])

with col1:
    if st.session_state.avatar == "":
        st.image("avatar/macdinh.jpg", width=300, use_column_width=True)
    
    else:
        # Open the uploaded image
        image = Image.open(st.session_state.avatar)
        # Display the image in the app
        st.image(image, width=300, use_column_width=True)

    st.write(f"**{st.session_state.fullname}**")

with col2:
    with st.container(border=True):
        st.write("- " + "**Ngày sinh**" + f":  {str(st.session_state.dob)}")
        st.write("- " + "**Cân nặng**" + f":  {str(st.session_state.weight)} kg")
        st.write("- " + "**Chiều cao**" + f":  {str(st.session_state.height)} cm")
        st.write("- " + "**Tần số hoạt động**" + f":  {str(st.session_state.activity_level)}")

    if st.button("Chỉnh sửa thông tin cá nhân", type="primary", use_container_width=True):
         editPersonal()