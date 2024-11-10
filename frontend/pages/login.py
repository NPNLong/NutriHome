import streamlit as st
from datetime import datetime, timedelta
from PIL import Image
import os
import pytz

timezone = pytz.timezone("Asia/Bangkok")

ID = 1
USERNAME = "nutrimate"
PASSWORD = "abc123"
FULLNAME = "Nguyễn Phước Ngưỡng Long"
DOB = datetime(2005, 10, 18)
FIX_DOB = DOB.strftime("%d-%m-%Y") #Định dạng ngày
GENDER = "Male"
WEIGHT = 62
HEIGHT = 175
BMI = 20.2
ACTIVITY_LEVEL = "Sometimes"

if "register" not in st.session_state:
    st.session_state.register = False

if st.session_state.register:
    st.title("Đăng ký")

    with st.form("login_form"):
        new_fullname = st.text_input("Họ và Tên")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            new_gender = st.selectbox("Giới tính", ["Nam", "Nữ"])
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
            new_activity_level = st.selectbox("Tần suất hoạt động", ["Active", "Sometimes", "Inactive"])

        new_username = st.text_input("Tên đăng nhập", max_chars=14)
        if new_username == USERNAME: #Check trùng tên đăng nhập
            st.warning("Đã có người sử dụng tên đăng nhập này!")

        password = st.text_input("Mật khẩu")
        again_password = st.text_input("Nhập lại mật khẩu", max_chars=14)
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
                    password, again_password, password == again_password
                ]):
                    new_dob = datetime(int(year), int(month), int(date))
                    st.session_state.logged_in = True
                    st.session_state.user = {
                        "id": 10,
                        "fullname": new_fullname,
                        "username": new_username,
                        "avatar": "",  # Path to user avatar image
                        "dob": new_dob.strftime("%d-%m-%Y"),  # Date of birth
                        "gender": new_gender,  # User's gender
                        "height": new_height,  # Height in cm
                        "weight": new_weight,  # Weight in kg
                        "bmi": 0,  # Body Mass Index, initially set to 0
                        "activity_level": new_activity_level,  # Activity level of the user
                        "absorbed_carbs": 0,
                        "absorbed_protein": 0,
                        "absorbed_fat": 0,
                        "absorbed_calories": 0,
                        "target_carbs": 0,  # Daily target carbohydrates in grams
                        "target_protein": 0,  # Daily target protein in grams
                        "target_fat": 0,  # Daily target fat in grams
                        "target_calories": 0,  # Daily calorie target
                        "family_id": 0,  # Identifier for the family group
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
    def check_login(username, password): #Check thông tin đăng nhập
        return username == USERNAME and password == PASSWORD

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
        if check_login(username, password):
            st.session_state.logged_in = True
            st.session_state.user = {
                "id": 1,
                "fullname": FULLNAME,
                "username": USERNAME,
                "avatar": f"images/avatar/{USERNAME}/macdinh.jpg",  # Path to user avatar image
                "dob": FIX_DOB,  # Date of birth
                "gender": GENDER,  # User's gender
                "height": HEIGHT,  # Height in cm
                "weight": WEIGHT,  # Weight in kg
                "bmi": BMI,  # Body Mass Index, initially set to 0
                "activity_level": ACTIVITY_LEVEL,  # Activity level of the user
                "absorbed_carbs": 150,
                "absorbed_protein": 15,
                "absorbed_fat": 10,
                "absorbed_calories": 1500,
                "target_carbs": 210,  # Daily target carbohydrates in grams
                "target_protein": 60,  # Daily target protein in grams
                "target_fat": 30,  # Daily target fat in grams
                "target_calories": 2000,  # Daily calorie target
                "family_id": 0,  # Identifier for the family group
            }

            st.session_state.weekly_menu = {
                "Monday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 1,
                                "name": "Cơm",
                                "image": "food_images/com.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 2,
                                "name": "Thịt Kho Tàu",
                                "image": "food_images/thitKhoTau.jpg"
                            },
                            { 
                                "id": 3,
                                "name": "Rau Muống Xào Tỏi",
                                "image": "food_images/rauMuongXaoToi.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 4,
                                "name": "Canh Rau Muong Sau",
                                "image": "food_images/canhRauMuongSau.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Carbs": 200,
                    "Protein": 100,
                    "Fat": 50,
                    "Calories": 2000
                },
                "Tuesday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 5,
                                "name": "Chả Ram Tôm Đất",
                                "image": "food_images/chaRamTomDat.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 6,
                                "name": "Salad trái cây trộn chua ngọt",
                                "image": "food_images/saladTraiCay.jpg"
                            },
                            { 
                                "id": 7,
                                "name": "Cá basa kho tộ",
                                "image": "food_images/caBasaKhoTo.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 8,
                                "name": "Latte Art Chuẩn Barista",
                                "image": "food_images/latteBarista.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Carbs": 300,
                    "Protein": 48,
                    "Fat": 50,
                    "Calories": 1876
                },
                "Wednesday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 9,
                                "name": "Quýt ngâm đường phèn",
                                "image": "food_images/quytNgam.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 10,
                                "name": "Ức gà sốt cam",
                                "image": "food_images/ucGaSotCam.jpg"
                            },
                            { 
                                "id": 11,
                                "name": "Canh chua cá lóc nấu khế",
                                "image": "food_images/canhChuaCaLoc.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 12,
                                "name": "Sữa Chua Đào Vải Thạch Lá Dứa",
                                "image": "food_images/suaChuaDaoVaiThach.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Carbs": 500,
                    "Protein": 400,
                    "Fat": 350,
                    "Calories": 4000
                },
                "Thursday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 11,
                                "name": "Canh chua cá lóc nấu khế",
                                "image": "food_images/canhChuaCaLoc.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 1,
                                "name": "Cơm",
                                "image": "food_images/com.jpg"
                            },
                            { 
                                "id": 2,
                                "name": "Thịt Kho Tàu",
                                "image": "food_images/thitKhoTau.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 6,
                                "name": "Salad trái cây trộn chua ngọt",
                                "image": "food_images/saladTraiCay.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Carbs": 300,
                    "Protein": 230,
                    "Fat": 130,
                    "Calories": 2300
                },
                "Friday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 3,
                                "name": "Rau Muống Xào Tỏi",
                                "image": "food_images/rauMuongXaoToi.jpg"
                            },
                            { 
                                "id": 4,
                                "name": "Canh Rau Muong Sau",
                                "image": "food_images/canhRauMuongSau.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 7,
                                "name": "Cá basa kho tộ",
                                "image": "food_images/caBasaKhoTo.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 5,
                                "name": "Chả Ram Tôm Đất",
                                "image": "food_images/chaRamTomDat.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Carbs": 200,
                    "Protein": 30,
                    "Fat": 10,
                    "Calories": 1000
                },
                "Saturday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 8,
                                "name": "Latte Art Chuẩn Barista",
                                "image": "food_images/latteBarista.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 11,
                                "name": "Canh chua cá lóc nấu khế",
                                "image": "food_images/canhChuaCaLoc.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 2,
                                "name": "Thịt Kho Tàu",
                                "image": "food_images/thitKhoTau.jpg"
                            },
                            { 
                                "id": 12,
                                "name": "Sữa Chua Đào Vải Thạch Lá Dứa",
                                "image": "food_images/suaChuaDaoVaiThach.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Carbs": 400,
                    "Protein": 40,
                    "Fat": 200,
                    "Calories": 2224
                },
                "Sunday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 4,
                                "name": "Canh Rau Muong Sau",
                                "image": "food_images/canhRauMuongSau.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 5,
                                "name": "Chả Ram Tôm Đất",
                                "image": "food_images/chaRamTomDat.jpg"
                            },
                            { 
                                "id": 1,
                                "name": "Cơm",
                                "image": "food_images/com.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 9,
                                "name": "Quýt ngâm đường phèn",
                                "image": "food_images/quytNgam.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Carbs": 123,
                    "Protein": 32,
                    "Fat": 43,
                    "Calories": 2134
                }
            }

            st.session_state.history = {
                "Today": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 8,
                                "name": "Latte Art Chuẩn Barista",
                                "image": "food_images/latteBarista.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 11,
                                "name": "Canh chua cá lóc nấu khế",
                                "image": "food_images/canhChuaCaLoc.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 2,
                                "name": "Thịt Kho Tàu",
                                "image": "food_images/thitKhoTau.jpg"
                            },
                            { 
                                "id": 12,
                                "name": "Sữa Chua Đào Vải Thạch Lá Dứa",
                                "image": "food_images/suaChuaDaoVaiThach.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Date": datetime.now(timezone),
                    "Carbs": 400,
                    "Protein": 40,
                    "Fat": 200,
                    "Calories": 2224
                },
                "Yesterday": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 5,
                                "name": "Chả Ram Tôm Đất",
                                "image": "food_images/chaRamTomDat.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 6,
                                "name": "Salad trái cây trộn chua ngọt",
                                "image": "food_images/saladTraiCay.jpg"
                            },
                            { 
                                "id": 7,
                                "name": "Cá basa kho tộ",
                                "image": "food_images/caBasaKhoTo.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 8,
                                "name": "Latte Art Chuẩn Barista",
                                "image": "food_images/latteBarista.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Date": datetime.now(timezone) - timedelta(days=1),
                    "Carbs": 300,
                    "Protein": 48,
                    "Fat": 50,
                    "Calories": 1876
                },
                "theDayBefore": {
                    "Breakfast": {
                        "listOfFoods": [
                            { 
                                "id": 1,
                                "name": "Cơm",
                                "image": "food_images/com.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Lunch": {
                        "listOfFoods": [
                            { 
                                "id": 2,
                                "name": "Thịt Kho Tàu",
                                "image": "food_images/thitKhoTau.jpg"
                            },
                            { 
                                "id": 3,
                                "name": "Rau Muống Xào Tỏi",
                                "image": "food_images/rauMuongXaoToi.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Dinner": {
                        "listOfFoods": [
                            { 
                                "id": 4,
                                "name": "Canh Rau Muong Sau",
                                "image": "food_images/canhRauMuongSau.jpg"
                            },
                        ],
                        "eaten": False,
                    },
                    "Date": datetime.now(timezone) - timedelta(days=2),
                    "Carbs": 200,
                    "Protein": 100,
                    "Fat": 50,
                    "Calories": 2000
                }
            }

            st.session_state.searchingList = [
                {
                    "id": 1,
                    "name": "Cơm",
                    "image": "food_images/com.jpg",
                    "cooking_time": 45,
                    "rating": 4.5
                },
                {
                    "id": 2,
                    "name": "Thịt Kho Tàu",
                    "image": "food_images/thitKhoTau.jpg",
                    "cooking_time": 60,
                    "rating": 4.8
                },
                {
                    "id": 3,
                    "name": "Rau Muống Xào Tỏi",
                    "image": "food_images/rauMuongXaoToi.jpg",
                    "cooking_time": 20,
                    "rating": 1.6
                },
                {
                    "id": 4,
                    "name": "Canh Rau Muong Sau",
                    "image": "food_images/canhRauMuongSau.jpg",
                    "cooking_time": 10,
                    "rating": 4.3
                },
                {
                    "id": 5,
                    "name": "Chả Ram Tôm Đất",
                    "image": "food_images/chaRamTomDat.jpg",
                    "cooking_time": 45,
                    "rating": 4.4
                },
                {
                    "id": 6,
                    "name": "Salad trái cây trộn chua ngọt",
                    "image": "food_images/saladTraiCay.jpg",
                    "cooking_time": 5,
                    "rating": 0.5
                },
                {
                    "id": 7,
                    "name": "Cá basa kho tộ",
                    "image": "food_images/caBasaKhoTo.jpg",
                    "cooking_time": 45,
                    "rating": 3.8
                },
                {
                    "id": 8,
                    "name": "Latte Art Chuẩn Barista",
                    "image": "food_images/latteBarista.jpg",
                    "cooking_time": 10,
                    "rating": 4.6
                },
                {
                    "id": 9,
                    "name": "Quýt ngâm đường phèn",
                    "image": "food_images/quytNgam.jpg",
                    "cooking_time": 5,
                    "rating": 3.4
                },
                {
                    "id": 10,
                    "name": "Ức gà sốt cam",
                    "image": "food_images/ucGaSotCam.jpg",
                    "cooking_time": 35,
                    "rating": 4.9
                },
                {
                    "id": 11,
                    "name": "Canh chua cá lóc nấu khế",
                    "image": "food_images/canhChuaCaLoc.jpg",
                    "cooking_time": 30,
                    "rating": 4.2
                },
                {
                    "id": 12,
                    "name": "Sữa Chua Đào Vải Thạch Lá Dứa",
                    "image": "food_images/suaChuaDaoVaiThach.jpg",
                    "cooking_time": 3,
                    "rating": 4.2
                },
            ]

            st.session_state.addMember = [
                {
                    "id": 0,
                    "username": "",
                    "fullname": "",
                    "avatar": "",  # Path to user avatar image
                },
            ]

            st.session_state.family = {
                "id": 1,
                "name": "SGUET",
                "avatar": "",
                "description": "A Support Group of UET (University of Engineering and Technology) typically refers to a community or organization within or associated with a university that provides assistance, guidance, and resources to students, faculty, or staff. In the case of UET (whether referring to UET Lahore or other branches of the University of Engineering and Technology), a support group can take various forms depending on the purpose and audience",
                "memberCount": 5,
                "member": [
                    {
                        "id": 1,
                        "username": USERNAME,
                        "fullname": FULLNAME,
                        "avatar": "",  # Path to user avatar image
                        "absorbed_carbs": 150,
                        "absorbed_protein": 15,
                        "absorbed_fat": 10,
                        "absorbed_calories": 1500,
                        "target_carbs": 210,  # Daily target carbohydrates in grams
                        "target_protein": 60,  # Daily target protein in grams
                        "target_fat": 30,  # Daily target fat in grams
                        "target_calories": 2000,  # Daily calorie target
                    },
                    {
                        "id": 2,
                        "username": "kachi1401",
                        "fullname": "Hoàng Khánh Chi",
                        "avatar": "",  # Path to user avatar image
                        "absorbed_carbs": 149,
                        "absorbed_protein": 16,
                        "absorbed_fat": 11,
                        "absorbed_calories": 1510,
                        "target_carbs": 216,  # Daily target carbohydrates in grams
                        "target_protein": 63,  # Daily target protein in grams
                        "target_fat": 33,  # Daily target fat in grams
                        "target_calories": 2005,  # Daily calorie target
                    },
                    {
                        "id": 3,
                        "username": "top1manager",
                        "fullname": "Phạm Anh Tuấn",
                        "avatar": "",  # Path to user avatar image
                        "absorbed_carbs": 156,
                        "absorbed_protein": 12,
                        "absorbed_fat": 14,
                        "absorbed_calories": 1509,
                        "target_carbs": 212,  # Daily target carbohydrates in grams
                        "target_protein": 65,  # Daily target protein in grams
                        "target_fat": 34,  # Daily target fat in grams
                        "target_calories": 2004,  # Daily calorie target
                    },
                    {
                        "id": 4,
                        "username": "cuongdeptrai",
                        "fullname": "Vũ Mạnh Cường",
                        "avatar": "",  # Path to user avatar image
                        "absorbed_carbs": 155,
                        "absorbed_protein": 11,
                        "absorbed_fat": 19,
                        "absorbed_calories": 1590,
                        "target_carbs": 260,  # Daily target carbohydrates in grams
                        "target_protein": 70,  # Daily target protein in grams
                        "target_fat": 90,  # Daily target fat in grams
                        "target_calories": 2100,  # Daily calorie target
                    },
                    {
                        "id": 5,
                        "username": "bochungmay",
                        "fullname": "Nguyễn Huy Thái",
                        "avatar": "",  # Path to user avatar image
                        "absorbed_carbs": 200,
                        "absorbed_protein": 30,
                        "absorbed_fat": 33,
                        "absorbed_calories": 1800,
                        "target_carbs": 300,  # Daily target carbohydrates in grams
                        "target_protein": 90,  # Daily target protein in grams
                        "target_fat": 60,  # Daily target fat in grams
                        "target_calories": 2300,  # Daily calorie target
                    },
                ]
            }

            st.session_state.shoppingList = ["Thịt bò Wagyu 2g", "Giấm 10ml", "Gạo 100g",]

            st.session_state.posts = [
                {
                    "post_id": 1,
                    "author_id": 10,
                    "author": "Hoàng Khánh Chi",
                    "author_username": "kachi1401",
                    "title": "Cách nấu cơm siêu ngon!",
                    "content": "Nấu ngon thì cơm sẽ siêu ngon!",
                    "image": "food_images/com.jpg",
                    "created_at": datetime(2024, 1, 1, 12, 30, 45).strftime("%d-%m-%Y %H:%M:%S"),
                    "react": False,
                    "total_reacts": 20,
                    "comments": ["Vũ Mạnh Cường: Bịp vcl", "Hoàng Khánh Chi: Top 1 công thức tôi luôn tin tưởng", "Phạm Anh Tuấn: Cho thêm giấm ngon x100"]
                },
                {
                    "post_id": 2,
                    "author_id": 20,
                    "author": "Nguyễn Huy Thái",
                    "author_username": "bochungmay",
                    "title": "SGUET",
                    "content": "Đỉnh mãi SG!",
                    "image": "features_images/sg.jpg",
                    "created_at": datetime(2012, 11, 14, 12, 30, 45).strftime("%d-%m-%Y %H:%M:%S"),
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
