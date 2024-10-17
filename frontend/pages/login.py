import streamlit as st
from datetime import datetime

USERNAME = "nutrimate"
PASSWORD = "abc123"
FULLNAME = "Nguyễn Phước Ngưỡng Long"
DOB = datetime(2005, 10, 18)
FIX_DOB = DOB.strftime("%d-%m-%Y")
WEIGHT = 62
HEIGHT = 175
ACTIVITY_LEVEL = "Sometimes"

if "register" not in st.session_state:
    st.session_state.register = False

if st.session_state.register:
    st.title("Đăng ký")

    with st.form("login_form"):
        new_fullname = st.text_input("Họ và Tên")
        new_dob = st.date_input("Ngày sinh")
        new_weight = st.text_input("Cân nặng (kg)")
        new_height = st.text_input("Chiều cao (cm)")
        new_activity_level = st.selectbox("Tần suất hoạt động", ["Active", "Sometimes", "Inactive"])

        new_username = st.text_input("Tên đăng nhập", max_chars=14)

        if new_username == USERNAME:
            st.warning("Đã có người sử dụng tên đăng nhập này!")

        password = st.text_input("Mật khẩu")
        again_password = st.text_input("Nhập lại mật khẩu", max_chars=14)

        if password != again_password:
            st.warning("Mật khẩu không trùng!")

        register_button = st.form_submit_button("Đăng ký", type="primary", use_container_width=True)

        if register_button:
            st.session_state.logged_in = True
            st.session_state.username = new_username
            st.session_state.fullname = new_fullname
            st.session_state.dob = new_dob.strftime("%d-%m-%Y")
            st.session_state.weight = new_weight
            st.session_state.height = new_height
            st.session_state.activity_level = new_activity_level
            st.success(f"Chào mừng {st.session_state.fullname}!")
            st.rerun() 

else:
    def check_login(username, password):
        return username == USERNAME and password == PASSWORD

    st.title("Đăng nhập")

    with st.form("login_form"):
        username = st.text_input("Tên đăng nhập")
        password = st.text_input("Mật khẩu", type="password")
        login_button = st.form_submit_button("Đăng nhập", type="primary", use_container_width=True)
        register_button = st.form_submit_button("Đăng ký", use_container_width=True)

    if login_button:
        if check_login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = USERNAME
            st.session_state.fullname = FULLNAME
            st.session_state.dob = FIX_DOB
            st.session_state.weight = WEIGHT
            st.session_state.height = HEIGHT
            st.session_state.activity_level = ACTIVITY_LEVEL
            st.rerun() 

        else:
            st.error("Thông tin đăng nhập không chính xác, vui lòng thử lại.")

    if register_button:
        st.session_state.register = True
        st.rerun()
