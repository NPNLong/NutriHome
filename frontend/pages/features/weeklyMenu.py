import streamlit as st
import plotly.graph_objects as go
from PIL import Image
import os

# Khởi tạo trạng thái của nút yêu thích
if 'favorite' not in st.session_state:
    st.session_state.favorite = False

# Đổi trạng thái khi nhấn nút
def toggle_favorite():
    st.session_state.favorite = not st.session_state.favorite

# Hàm tạo các mục trong bữa ăn
@st.dialog("Chi tiết món ăn", width="large")
def details():
    st.session_state.food_details = {
        "id": 1,
        "name": "Cơm",
        "image": "food_images/com.jpg",
        "rating" : 4.2,
        "cooking_time" : 40,
        "calories" : 2000,
        "protein" : 150,
        "carbs" : 200,
        "fat" : 60,
        "step" : """
        - **Đong gạo**: Bạn dùng cốc đi kèm nồi cơm điện đong gạo, đong 1 cốc gạo khoảng 160gr cho 2 chén cơm.

        - **Vo gạo**: Cho nước vào nồi cơm đã có gạo, dùng tay nhẹ nhàng vo gạo rồi khuấy đều để cát bụi, vỏ trấu, sạn còn bám trên hạt gạo, chắt nước ra rồi tiếp tục chế nước sạch vào.

        - **Đong nước**: Tùy loại gạo bạn nấu, và tùy bạn muốn ăn cơm nhão, khô hay vừa mà thêm nước sao cho phù hợp. Trong nồi cơm thường có nấc chia độ, cho thấy nên cho thêm bao nhiêu nước và gạo.

        - **Thêm gia vị**: Để cơm được ngon hơn, thêm gia vị vào nước trước khi nấu, như 1 muỗng cà phê muối, 1/2 muỗng cà phê giấm hoặc 2 - 3 giọt dầu oliu.
        """,
        "ingredients" : """
        - Gạo: 160gr (1 cốc)

        - Nước: 280 ml

        - Muối: 1 muỗng cà phê

        - Giấm ăn: 1/2 muỗng cà phê
        """
    }

    st.header(st.session_state.food_details["name"], divider="grey")

    col1, col2 = st.columns([35,65])

    with col1:
        st.image(st.session_state.food_details["image"], use_container_width=True)

        rating = st.session_state.food_details["rating"]
        if rating < 1.5:
            with st.container(border=True):
                st.write("**Đánh giá**" + ": ⭐ ")
                st.write(f"({rating} / 5.0)")
        elif rating >= 1.5 and rating < 2.5:
            with st.container(border=True):
                st.write("**Đánh giá**" + ": ⭐⭐ ")
                st.write(f"({rating} / 5.0)")
        elif rating >= 2.5 and rating < 3.5:
            with st.container(border=True):
                st.write("**Đánh giá**" + ": ⭐⭐⭐ ")
                st.write(f"({rating} / 5.0)")
        elif rating >= 3.5 and rating < 4.5:
            with st.container(border=True):
                st.write("**Đánh giá**" + ": ⭐⭐⭐⭐ ")
                st.write(f"({rating} / 5.0)")
        elif rating > 4.5:
            with st.container(border=True):
                st.write("**Đánh giá**" + ": ⭐⭐⭐⭐⭐ ")
                st.write(f"({rating} / 5.0)")

        c1, c2 = st.columns([1, 1])
        with c1:
            # Hiển thị nút yêu thích
            if st.session_state.favorite:
                if st.button("Yêu thích", on_click=toggle_favorite, type='primary', use_container_width=True):
                    st.write("Bạn đã thích món ăn này!")
            else:
                if st.button("Đã yêu thích", on_click=toggle_favorite, use_container_width=True):
                    st.write("Hãy yêu thích món ăn này!")
        with c2:
            rating =  st.button("Rating", use_container_width=True)
        if rating:
            with st.form("Rating"):
                sentiment_mapping = ["one", "two", "three", "four", "five"]
                selected = st.feedback("stars")
                st.form_submit_button('Submit', type='primary')

        # Dữ liệu cho biểu đồ tròn
        labels = ['Carbs', 'Fats', 'Protein']
        values = [st.session_state.food_details["carbs"], st.session_state.food_details["fat"], st.session_state.food_details["protein"]]

        st.write("**Chi tiết dinh dưỡng**")
        # Tạo biểu đồ tròn với plotly
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        # Tùy chỉnh biểu đồ tròn
        fig.update_traces(
            hoverinfo='label+percent',
            textinfo='label+percent',  # Chỉ hiển thị tên thành phần
            textfont=dict(size=10, color='white', family='Arial Black'),
            marker=dict(colors=['#FFCC00', '#66b3ff', '#9933CC']),  # Màu sắc cho các thành phần
            showlegend=False
        )
        fig.update_layout(
            margin=dict(t=10, b=10, l=10, r=10),
            width=300,  # Độ rộng biểu đồ
            height=300  # Độ cao biểu đồ
        )
        # Hiển thị biểu đồ trong Streamlit
        st.plotly_chart(fig)

        with st.container(border=True):
            c1, c2 = st.columns([6, 4])

            with c1:
                st.write("Total calories")
                st.write("Carbs")
                st.write("Fat")
                st.write("Protein")

            with c2:
                st.write(f"{st.session_state.food_details["calories"]} cals")
                st.write(f"{st.session_state.food_details["carbs"]} g")
                st.write(f"{st.session_state.food_details["fat"]} g")
                st.write(f"{st.session_state.food_details["protein"]} g")

    with col2:
        with st.container(border=True):
            st.write("**Thời gian nấu**" + f": {st.session_state.food_details["cooking_time"]} phút")

            st.text("")

            st.subheader("Nguyên liệu")
            st.write(st.session_state.food_details["ingredients"])
            
            st.text("")
            
            st.subheader("Cách làm")
            st.write(st.session_state.food_details["step"])
            # Video
            # st.markdown("[Xem hướng dẫn chi tiết qua video](https://youtu.be/QJZUwiJhKZ0?si=IO1AvQjjiCk6GzLO)")

@st.dialog("Quét hóa đơn")
def billScanning():
    uploaded_image = st.file_uploader("Hóa đơn", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image).convert("RGB")
        st.image(image, use_container_width=True)
    if st.button("Quét hóa đơn", type='primary', use_container_width=True):
        bill_dir = os.path.join("images/bills", st.session_state.user["username"])
        os.makedirs(bill_dir, exist_ok=True)  # Creates folder if it doesn't exist
                    
        # Save avatar in the user directory
        avatar_path = os.path.join(bill_dir, "bill.jpg")
        avatar_image = Image.open(uploaded_image)
        avatar_image.convert("RGB").save(avatar_path, "JPEG")
        st.session_state.user["avatar"] = avatar_path
        st.rerun()

# Hàm để hiển thị biểu đồ tròn và chi tiết dinh dưỡng
def display_nutrition_chart(day):
    col1, col2 = st.columns([1, 1], vertical_alignment='center')
    with col1:
        labels = ['Carbs', 'Fats', 'Protein']
        values = [st.session_state.weekly_menu[day]["Carbs"], st.session_state.weekly_menu[day]["Fat"], st.session_state.weekly_menu[day]["Protein"]]
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_traces(
            hoverinfo='label+percent',
            textinfo='label+percent',
            textfont=dict(size=15, color='white', family='Arial Black'),
            marker=dict(colors=['#FFCC00', '#66b3ff', '#9933CC']),
            showlegend=False
        )
        fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), width=700, height=280)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.write("**Chi tiết**")
        with st.container(border=True):
            c1, c2 = st.columns([6, 4])
            with c1:
                st.write("Total calories")
                st.write("Carbs")
                st.write("Fat")
                st.write("Protein")
            with c2:
                st.write(f"{st.session_state.weekly_menu[day]["Calories"]} calories")
                st.write(f"{st.session_state.weekly_menu[day]["Carbs"]} g")
                st.write(f"{st.session_state.weekly_menu[day]["Protein"]} g")
                st.write(f"{st.session_state.weekly_menu[day]["Fat"]} g")

# Hàm hiển thị từng món ăn trong bữa
def display_meal(meal, day):
        for idx in range(0, len(st.session_state.weekly_menu[day][meal]["listOfFoods"]), 2):
            c1, c2 = st.columns(2)
            food1 = st.session_state.weekly_menu[day][meal]["listOfFoods"][idx]
            with c1:
                with st.container(border=True):
                    col1, col2, col3 = st.columns([20, 45, 25], vertical_alignment="center")
                    with col1:
                        with st.container(height=50, border=False):
                            st.image(food1["image"], use_container_width=True)
                    with col2:
                        st.write(f"**{food1["name"]}**")
                    with col3:
                        # Using an f-string for the key with escaped quotes
                        if st.button("Chi tiết", key=f"{day}_{meal}_{food1['name']}_{idx}"):
                            details()

            if idx + 1 < len(st.session_state.weekly_menu[day][meal]["listOfFoods"]):
                food2 = st.session_state.weekly_menu[day][meal]["listOfFoods"][idx + 1]
                with c2:
                    with st.container(border=True):
                        col1, col2, col3 = st.columns([20, 45, 25], vertical_alignment="center")
                        with col1:
                            with st.container(height=50, border=False):
                                st.image(food2["image"], use_container_width=True)
                        with col2:
                            st.write(f"**{food2["name"]}**")
                        with col3:
                            # Using an f-string for the key with escaped quotes
                            if st.button("Chi tiết", key=f"{day}_{meal}_{food2['name']}_{idx + 1}"):
                                details()

st.title("Weekly Menu")
st.write("NutriHome cung cấp tính năng xây dựng thực đơn cá nhân hóa hàng tuần dựa trên dữ liệu như chiều cao, cân nặng, và tình trạng sức khỏe của cá nhân. Hệ thống sử dụng dữ liệu dinh dưỡng đáng tin cậy từ USDA Food Data Central, giúp đảm bảo sự chính xác về hàm lượng dinh dưỡng trong các món ăn.")

# Tên các ngày trong tuần
days_of_week = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]

# Tạo các tab cho mỗi ngày
tabs = st.tabs([f"**{day}**" for day in days_of_week])

# Vòng lặp qua từng tab với từng ngày
for day, day_tab in zip(days_of_week, tabs):
    if day == "Thứ Hai":
        day = "Monday"
    elif day == "Thứ Ba":
        day = "Tuesday"
    elif day == "Thứ Tư":
        day = "Wednesday"
    elif day == "Thứ Năm":
        day = "Thursday"
    elif day == "Thứ Sáu":
        day = "Friday"
    elif day == "Thứ Bảy":
        day = "Saturday"
    elif day == "Chủ Nhật":
        day = "Sunday"
    with day_tab:
        with st.expander("**Tổng lượng dưỡng chất từ bữa ăn**"):
            display_nutrition_chart(day)
        
        st.header("Thực đơn của gia đình bạn là:")
        breakFast, lunch, dinner = st.tabs(["Bữa sáng", "Bữa trưa", "Bữa tối"])

        with breakFast:
            st.subheader("Bữa sáng:")
            display_meal("Breakfast", day)
            col1, col2, col3 = st.columns([25, 25, 50])
            with col1:
                if st.session_state.weekly_menu[day]["Breakfast"]["eaten"] == False:
                    if st.button("Đã ăn", key=f"Breakfast_{day}", type='primary', use_container_width=True):
                        st.session_state.weekly_menu[day]["Breakfast"]["eaten"] = True
                        st.rerun()
                else:
                    if st.button("Đã ăn", key=f"Breakfast_{day}", use_container_width=True):
                        st.session_state.weekly_menu[day]["Breakfast"]["eaten"] = False
                        st.rerun()
            with col2:
                if st.button("Quét hóa đơn", key=f"Scan_Breakfast_{day}", use_container_width=True):
                    billScanning()
                        
        with lunch:
            st.subheader("Bữa trưa:")
            display_meal("Lunch", day)
            col1, col2, col3 = st.columns([25, 25, 50])
            with col1:
                if st.session_state.weekly_menu[day]["Lunch"]["eaten"] == False:
                    if st.button("Đã ăn", key=f"Lunch_{day}", type='primary', use_container_width=True):
                        st.session_state.weekly_menu[day]["Lunch"]["eaten"] = True
                        st.rerun()
                else:
                    if st.button("Đã ăn", key=f"Lunch_{day}", use_container_width=True):
                        st.session_state.weekly_menu[day]["Lunch"]["eaten"] = False
                        st.rerun()
            with col2:
                if st.button("Quét hóa đơn", key=f"Scan_Lunch_{day}", use_container_width=True):
                    billScanning()

        with dinner:
            st.subheader("Bữa tối:")
            display_meal("Dinner", day)
            col1, col2, col3 = st.columns([25, 25, 50])
            with col1:
                if st.session_state.weekly_menu[day]["Dinner"]["eaten"] == False:
                    if st.button("Đã ăn", key=f"Dinner_{day}", type='primary', use_container_width=True):
                        st.session_state.weekly_menu[day]["Dinner"]["eaten"] = True
                        st.rerun()
                else:
                    if st.button("Đã ăn", key=f"Breakfast_{day}", use_container_width=True):
                        st.session_state.weekly_menu[day]["Dinner"]["eaten"] = False
                        st.rerun()
            with col2:
                if st.button("Quét hóa đơn", key=f"Scan_Dinner_{day}", use_container_width=True):
                    billScanning()