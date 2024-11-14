import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import os
import pytz
import json
import requests

BACKEND_API = "http://127.0.0.1:5000"
timezone = pytz.timezone("Asia/Bangkok")

if "register" not in st.session_state:
    st.session_state.register = False

if st.session_state.register:
    st.title("Đăng ký")

    with st.form("login_form"):
        new_fullname = st.text_input("Họ và Tên")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            new_gender = st.selectbox("Giới tính", ["male", "female"])
        with col2:
            date = st.text_input("Ngày sinh")
        with col3:
            month = st.text_input("Tháng sinh")
        with col4:
            year = st.text_input("Năm sinh")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            new_weight = st.text_input("Cân nặng (kg)")
        with col2:
            new_height = st.text_input("Chiều cao (cm)")
        with col3:
            new_activity_level = st.selectbox("Tần suất hoạt động", ["high", "medium", "low"])

        new_disease = st.text_input("Bệnh lý")
        new_allergen = st.text_input("Dị ứng")

        new_username = st.text_input("Tên đăng nhập")

        password = st.text_input("Mật khẩu")
        again_password = st.text_input("Nhập lại mật khẩu")
        if password != again_password:
            st.warning("Mật khẩu không trùng!")

        col1, col2 = st.columns([1, 1])
        with col1:
            cancel_button = st.form_submit_button("Quay lại", use_container_width=True)
            if cancel_button:
                st.session_state.register = False
                st.rerun()
        with col2:
            register_button = st.form_submit_button("Đăng ký", type="primary", use_container_width=True)
            if register_button:
                if all([
                    new_fullname, new_gender, date, month, year,
                    new_weight, new_height, new_activity_level, new_username,
                    password, again_password, password == again_password, new_disease, new_allergen
                ]):
                    new_dob = datetime(int(year), int(month), int(date))
                    get_all_api = BACKEND_API + "/api/credentials/register"
                    response = requests.post(
                        get_all_api,
                        data=json.dumps(
                            {
                                "fullname": new_fullname,
                                "dob": new_dob.strftime("%Y-%m-%d"),
                                "username" : new_username,
                                "password": password,
                                "confirm_password": again_password,
                                "height": int(new_height),
                                "weight": int(new_weight),
                                "activity_level": new_activity_level,
                                "avatar": "images/avatar/macdinh.jpg",
                                "gender": new_gender
                            }
                        ),
                        headers = {'Content-Type': 'application/json',}
                    )
                    print(response.status_code)

                    if response.status_code == 201:
                        st.session_state.logged_in = True
                        st.session_state.user =  {
                            "id": response.json()["data"]["user"]["user_id"],
                            "fullname": response.json()["data"]["user"]["fullname"],
                            "age": response.json()["data"]["user"]["age"]
                        }
                        user_dir = os.path.join("images/avatar", new_username)
                        os.makedirs(user_dir, exist_ok=True)  # Creates folder if it doesn't exist
                        # Save avatar in the user directory
                        avatar_path = os.path.join(user_dir, "macdinh.jpg")
                        avatar_image = Image.open("images/avatar/macdinh.jpg")
                        avatar_image.convert("RGB").save(avatar_path, "JPEG")
                        st.session_state.user["avatar"] = avatar_path
             
                        st.rerun() 

                else:
                    st.error("Vui lòng điền đầy đủ thông tin trước khi đăng ký.")
            
else:
    st.title("Đăng nhập")

    with st.form("login_form"):
        username = st.text_input("Tên đăng nhập")
        password = st.text_input("Mật khẩu", type="password")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            login_button = st.form_submit_button("Đăng nhập", type="primary", use_container_width=True)
        with col2:
            register_button = st.form_submit_button("Đăng ký", use_container_width=True)
        with col3:
            back_button = st.form_submit_button("Quay lại", use_container_width=True)

        if login_button:
            get_all_api = BACKEND_API + "/api/credentials/login"
            response = requests.post(get_all_api,
                                        data=json.dumps({"username": username,
                                                        "password": password
                                                        }), headers = {
                    'Content-Type': 'application/json',
            })
            print(response.status_code)

            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.user =  {
                    "id": response.json()["data"]["user"]["user_id"],
                    "fullname": response.json()["data"]["user"]["fullname"],
                    "username": response.json()["data"]["user"]["username"],
                    "family_id": response.json()["data"]["user"]["family_id"]
                }
                st.session_state.posts = [
                {
                    "post_id": 1,
                    "author_id": 10,
                    "author": "Hoàng Khánh Chi",
                    "author_username": "kachi1401",
                    "title": "Cách nấu cơm siêu ngon!",
                    "content": "Nấu ngon thì cơm sẽ siêu ngon!",
                    "image": "food_images/com.jpg",
                    "created_at": datetime(2024, 1, 1, 12, 30, 45).strftime("%Y-%m-%d %H:%M:%S"),
                    "react": False,
                    "total_reacts": 20,
                    "comments": ["Hoàng Khánh Chi: Top 1 công thức tôi luôn tin tưởng", "Phạm Anh Tuấn: Cho thêm giấm ngon x100"]
                },
                {
                    "post_id": 2,
                    "author_id": 20,
                    "author": "Nguyễn Huy Thái",
                    "author_username": "bochungmay",
                    "title": "SGUET",
                    "content": "Đỉnh mãi SG!",
                    "image": "features_images/sg.jpg",
                    "created_at": datetime(2012, 11, 14, 12, 30, 45).strftime("%Y-%m-%d %H:%M:%S"),
                    "react": True,
                    "total_reacts": 1000,
                    "comments": ["Nguyễn Huy Thái: Ảnh xấu vcl"]
                },
            ]

                
                st.rerun() 

            else:
                st.error("Thông tin đăng nhập không chính xác, vui lòng thử lại.")

    if register_button:
        st.session_state.register = True
        st.rerun()

    if back_button:
        st.session_state.login_page = False
        st.rerun()
