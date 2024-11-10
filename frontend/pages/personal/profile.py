import streamlit as st
from datetime import datetime
from PIL import Image
import os

save_path = 'images/avatar'
os.makedirs(save_path, exist_ok=True)

@st.dialog("Chỉnh sửa thông tin cá nhân", width="large")
def editPersonal():
    col1, col2 = st.columns([45, 55])
    with col2:
        dob = datetime.strptime(st.session_state.user["dob"], "%d-%m-%Y")
        new_fullname = st.text_input("Họ và Tên", value=st.session_state.user["fullname"])
        
        c1, c2, c3 = st.columns(3)
        with c1:
            new_date = st.text_input("Ngày sinh", value=str(dob.day))
        with c2:
            new_month = st.text_input("Tháng sinh", value=str(dob.month))
        with c3:
            new_year = st.text_input("Năm sinh", value=str(dob.year))
        new_dob = datetime(int(new_year), int(new_month), int(new_date))

        c1, c2, c3 = st.columns(3)
        with c1:
            new_weight = st.text_input("Cân nặng (kg)", value=st.session_state.user["weight"])
        with c2:
            new_height = st.text_input("Chiều cao (cm)", value=st.session_state.user["height"])
        with c3:
            new_activity_level = st.selectbox("Tần suất hoạt động", ["Active", "Sometimes", "Inactive"])

    with col1:
        uploaded_image = st.file_uploader("Avatar của bạn", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            image = Image.open(uploaded_image).convert("RGB")
            st.image(image, use_container_width=True)
        else:
            image = Image.open(st.session_state.user["avatar"]).convert("RGB")
            st.image(image, use_container_width=True)

    edit_button = st.button("Chỉnh sửa", type="primary", use_container_width=True)
    if edit_button:
            st.session_state.user["fullname"] = new_fullname
            st.session_state.user["dob"] = new_dob.strftime("%d-%m-%Y")
            st.session_state.user["weight"] = new_weight
            st.session_state.user["height"] = new_height
            st.session_state.user["activity_level"] = new_activity_level
            if uploaded_image is not None:
                # Define the full save path
                image_path = os.path.join(save_path + '/' + st.session_state.user["username"], "macdinh.jpg")
                
                # Save the image
                with open(image_path, "wb") as f:
                    image.save(f, format="JPEG")
            st.rerun()

st.title("Profile")

st.subheader("Thông tin cá nhân", divider='gray')

col1, col2 = st.columns([31, 69])

with col1:
    st.image(f"{st.session_state.user["avatar"]}", use_container_width=True)

    st.write(f"**{st.session_state.user["fullname"]}**")

with col2:
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.write("- " + "**Ngày sinh**" + f":  {str(st.session_state.user["dob"])}")
            st.write("- " + "**Giới tính**" + f":  {str(st.session_state.user["gender"])}")
            st.write("- " + "**Cân nặng**" + f":  {str(st.session_state.user["weight"])} kg")
            st.write("- " + "**Chiều cao**" + f":  {str(st.session_state.user["height"])} cm")
            st.write("- " + "**Tần số hoạt động**" + f":  {str(st.session_state.user["activity_level"])}")
        with c2:
            st.write("**Mục tiêu:**")
            st.write("- " + "**Calories**" + f":  {str(st.session_state.user["target_calories"])} calories")
            st.write("- " + "**Carbs**" + f":  {str(st.session_state.user["target_carbs"])} g")
            st.write("- " + "**Fat**" + f":  {str(st.session_state.user["target_fat"])} g")
            st.write("- " + "**Protein**" + f":  {str(st.session_state.user["target_protein"])} g")

    if st.button("Chỉnh sửa thông tin cá nhân", type="primary", use_container_width=True):
         editPersonal()