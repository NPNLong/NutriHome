import streamlit as st
from datetime import datetime
from PIL import Image
import os

save_path = 'images/avatar'
os.makedirs(save_path, exist_ok=True)

if "inFamily" not in st.session_state:
     st.session_state.inFamily = False

if "family_image" not in st.session_state:
     st.session_state.family_image = ""

if "family_name" not in st.session_state:
     st.session_state.family_name = ""

if "family_description" not in st.session_state:
     st.session_state.family_description = ""

if "family_members" not in st.session_state:
    st.session_state.family_members = [
        {
            "name": "Nguyễn Phước Ngưỡng Long",
            "dob": "18/10/2005",
            "weight": 62,
            "height": 175,
            "active": "Sometimes"
        },
        {
            "name": "Hoàng Khánh Chi",
            "dob": "14/01/2005",
            "weight": 52,
            "height": 168,
            "active": "Sometimes"
        },
        {
            "name": "Vũ Mạnh Cường",
            "dob": "09/10/2005",
            "weight": 56,
            "height": 170,
            "active": "Sometimes"
        },
        {
            "name": "Nguyễn Huy Thái",
            "dob": "15/09/2003",
            "weight": 70,
            "height": 170,
            "active": "Sometimes"
        },
    ]

if "family_verify" not in st.session_state:
    st.session_state.family_verify = [
        {
            "name": "Phạm Anh Tuấn",
            "dob": "08/09/2005",
            "weight": 65,
            "height": 180,
            "active": "Sometimes"
        },
        {
            "name": "Trịnh Trần Phương Tuấn",
            "dob": "12/04/1997",
            "weight": 60,
            "height": 170,
            "active": "Sometimes"
        },
    ]

@st.dialog("Chỉnh sửa thông tin cá nhân", width="large")
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
                image = Image.open(uploaded_image)
        
                # Define the full save path
                image_path = os.path.join(save_path + '/' + st.session_state.username, "macdinh.jpg")
                
                # Save the image
                image.save(image_path)
            st.rerun()

@st.dialog("Vào gia đình", width="large")
def joinFamily():
    st.subheader("Search", divider='gray')
    col1, col2, col3 = st.columns([70, 15, 15])
    with col1:
        search_food_name = st.text_input("Searching family name", label_visibility="collapsed")
    with col2:
        search = st.button("Tìm kiếm", use_container_width=True)
        if search:
            st.session_state.isSearch = True
            st.session_state.inputSearch = search_food_name
    with col3:
        if st.button("Reset", use_container_width=True):
            st.session_state.isSearch = False
            st.session_state.inputSearch = ""

    st.text('')
    st.subheader("Gia đình", divider='gray')

    with st.container(border=True):
         col1, col2 = st.columns([20, 80])
         with col1:
              st.image("family_images/nutrihome_avatar.jpg", use_column_width=True)
         with col2:
                st.write("**Tên gia đình:** Nutrihome")
                with st.expander("**Mô tả**"):
                    st.write("Những người bạn siêu chất của tôi!")
         if(st.button("Gửi yêu cầu", use_container_width=True, type='primary', key="family_1")):
              st.rerun()

    with st.container(border=True):
         col1, col2 = st.columns([20, 80])
         with col1:
              st.image("family_images/phongbat_avatar.jpeg", use_column_width=True)
         with col2:
                st.write("**Tên gia đình:** Hội phông bạt đánh bay bão Yagi")
                with st.expander("**Mô tả**"):
                    st.write("Bọn tao quyên góp 10 tỷ cho mặt trận tổ quốc!")
         if(st.button("Gửi yêu cầu", use_container_width=True, type='primary', key="family_2")):
              st.rerun()

@st.dialog("Tạo gia đình", width="large")
def createFamily():
    col1, col2 = st.columns([45, 55], gap='medium')

    with col1:
        uploaded_image = st.file_uploader("Ảnh gia đình", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, use_column_width=True)

    with col2:
        family_name = st.text_input("Tên gia đình")
        family_description = st.text_area("Mô tả", placeholder="Write your family's description here...")

    if st.button("Tạo gia đình", use_container_width=True, type='primary'):
         st.session_state.inFamily = True
         st.session_state.family_image = uploaded_image
         st.session_state.family_name = family_name
         st.session_state.family_description = family_description
         st.rerun()

st.title("Profile")

st.subheader("Thông tin cá nhân", divider='gray')

col1, col2 = st.columns([31, 69])

with col1:
    st.image(f"images/avatar/{st.session_state.username}/macdinh.jpg", width=300, use_column_width=True)

    st.write(f"**{st.session_state.fullname}**")

with col2:
    with st.container(border=True):
        st.write("- " + "**Ngày sinh**" + f":  {str(st.session_state.dob)}")
        st.write("- " + "**Cân nặng**" + f":  {str(st.session_state.weight)} kg")
        st.write("- " + "**Chiều cao**" + f":  {str(st.session_state.height)} cm")
        st.write("- " + "**Tần số hoạt động**" + f":  {str(st.session_state.activity_level)}")

    if st.button("Chỉnh sửa thông tin cá nhân", type="primary", use_container_width=True):
         editPersonal()

st.text('')
st.subheader("Gia đình của bạn", divider='gray')
if (st.session_state.inFamily):
     col1, col2 = st.columns([31, 69])
     with col1:
        st.image(st.session_state.family_image, use_column_width=True)

        st.write(f"**{st.session_state.family_name}**")

     with col2:
        with st.container(border=True):
            st.write("**Mô tả:**")
            st.write(st.session_state.family_description)
else:
     st.warning("**Bạn chưa ở trong gia đình! Vào một gia đình ngay:**")
     col1, col2 = st.columns([1, 1])
     with col1:
          if(st.button("Vào gia đình", type='primary', use_container_width=True)):
               joinFamily()
     with col2:
          if(st.button("Tạo gia đình", use_container_width=True)):
               createFamily()