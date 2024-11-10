import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Khởi tạo trạng thái của nút yêu thích
if 'favorite' not in st.session_state:
    st.session_state.favorite = False

if "isSearch" not in st.session_state:
    st.session_state.isSearch = False

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

def food_brief():
    for idx in range(0, len(st.session_state.searchingList), 3):
        c1, c2, c3 = st.columns(3)
        
        # Column 1
        if idx < len(st.session_state.searchingList):
            with c1:
                with st.container(border=True):
                    food = st.session_state.searchingList[idx]
                    with st.container(height=150, border=False):
                        st.image(food["image"], use_container_width=True)
                    with st.container(height=50, border=False):
                        st.write(f"**{food['name']}**")
                    st.write(f"**Thời gian nấu**: {food['cooking_time']} phút")
                    display_rating(food["rating"])
                    if st.button("Chi tiết", use_container_width=True, key=f"{food['id']}_details"):
                        details()

        # Column 2
        if idx + 1 < len(st.session_state.searchingList):
            with c2:
                with st.container(border=True):
                    food = st.session_state.searchingList[idx + 1]
                    with st.container(height=150, border=False):
                        st.image(food["image"], use_container_width=True)
                    with st.container(height=50, border=False):
                        st.write(f"**{food['name']}**")
                    st.write(f"**Thời gian nấu**: {food['cooking_time']} phút")
                    display_rating(food["rating"])
                    if st.button("Chi tiết", use_container_width=True, key=f"{food['id']}_details"):
                        details()

        # Column 3
        if idx + 2 < len(st.session_state.searchingList):
            with c3:
                with st.container(border=True):
                    food = st.session_state.searchingList[idx + 2]
                    with st.container(height=150, border=False):
                        st.image(food["image"], use_container_width=True)
                    with st.container(height=50, border=False):
                        st.write(f"**{food['name']}**")
                    st.write(f"**Thời gian nấu**: {food['cooking_time']} phút")
                    display_rating(food["rating"])
                    if st.button("Chi tiết", use_container_width=True, key=f"{food['id']}_details"):
                        details()

def display_rating(rating):
    # Display rating with stars based on rating value
    stars = "⭐" * int(rating)
    half_star = "⭐" if rating % 1 >= 0.5 else ""
    st.write(f"**Đánh giá:**")
    st.write(f"{stars}{half_star} ({rating} / 5.0)")

st.title("Recipes")
st.write("NutriHome đồng hành với người dùng như một người bạn cùng nhau chia sẻ những “bí kíp” nấu ăn đảm bảo sức khỏe nhưng không kém phần hấp dẫn. Các công thức chế biến món ăn được lựa chọn từ những nguồn uy tín như Kitchen Stories, Tasty, All recipes, Cookyvn sẽ được NutriHome trình bày dưới dạng hình ảnh bắt mắt cùng với những tóm tắt ngắn gọn, xúc tích nhằm đảm bảo bất kỳ người dùng nào cũng có thể trở thành những “bậc thầy làng bếp” xuất sắc.")

with st.container(border=True):
    st.subheader("Search")
    col1, col2, col3 = st.columns([70, 15, 15])
    with col1:
        search_food_name = st.text_input("Searching bar", label_visibility="collapsed")
    with col2:
        search = st.button("Tìm kiếm", use_container_width=True)
        if search:
            st.session_state.isSearch = True
            st.rerun()
    with col3:
        if st.button("Reset", use_container_width=True):
            st.session_state.isSearch = False
            st.rerun()

st.subheader("List of foods", divider="grey")

if st.session_state.isSearch:
    st.write("**You are searching**")
    st.session_state.searchingList = []
    st.session_state.searchingList = [
                {
                    "id": 8,
                    "name": "Latte Art Chuẩn Barista",
                    "image": "food_images/latteBarista.jpg",
                    "cooking_time": 10,
                    "rating": 4.6
                },
            ]
    food_brief()

else:
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
    food_brief()