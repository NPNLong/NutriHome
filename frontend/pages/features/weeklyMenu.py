import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Khởi tạo trạng thái của nút yêu thích
if 'favorite' not in st.session_state:
    st.session_state.favorite = False

# Đổi trạng thái khi nhấn nút
def toggle_favorite():
    st.session_state.favorite = not st.session_state.favorite

# Hàm tạo các mục trong bữa ăn
@st.dialog("Chi tiết món ăn", width="large")
def details(food_name, image_path):
    st.header(food_name, divider="grey")

    col1, col2 = st.columns([35,65])

    with col1:
        st.image(image_path)
        # Hiển thị nút yêu thích
        if st.session_state.favorite:
            if st.button("❤️", on_click=toggle_favorite):
                st.write("Bạn đã thích món ăn này!")
        else:
            if st.button("♡", on_click=toggle_favorite):
                st.write("Hãy yêu thích món ăn này!")

        # Dữ liệu cho biểu đồ tròn
        labels = ['Carbs', 'Fats', 'Protein']
        values = [70, 10, 20]

        st.subheader("", divider="grey")

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
                st.write("1000cals")
                st.write("210g")
                st.write("30g")
                st.write("60g")

        if st.button("Rating", use_container_width=True):
            with st.form("Rating"):
                sentiment_mapping = ["one", "two", "three", "four", "five"]
                selected = st.feedback("stars")
                st.form_submit_button('Submit')

    with col2:
        with st.container(border=True):
            st.write("**Thời gian nấu**" + ": 40 phút")
            st.write("**Độ khó**" + ": ⭐")
            st.write("**Đánh giá**" + ": ⭐⭐⭐⭐ " + "(4.3 / 5.0)")

            st.text("")

            st.subheader("Nguyên liệu")
            st.write("   - Gạo: 160gr (1 cốc)")
            st.write("   - Nước: 280 ml")
            st.write("   - Muối: 1 muỗng cà phê")
            st.write("   - Giấm ăn: 1/2 muỗng cà phê")
            
            st.text("")
            
            st.subheader("Cách làm")
            st.write("   - Đong gạo: Bạn dùng cốc đi kèm nồi cơm điện đong gạo, đong 1 cốc gạo khoảng 160gr cho 2 chén cơm.")
            st.write("   - Vo gạo: Cho nước vào nồi cơm đã có gạo, dùng tay nhẹ nhàng vo gạo rồi khuấy đều để cát bụi, vỏ trấu, sạn còn bám trên hạt gạo, chắt nước ra rồi tiếp tục chế nước sạch vào.")
            st.write("   - Đong nước: Tùy loại gạo bạn nấu, và tùy bạn muốn ăn cơm nhão, khô hay vừa mà thêm nước sao cho phù hợp. Trong nồi cơm thường có nấc chia độ, cho thấy nên cho thêm bao nhiêu nước và gạo.")
            st.write("   - Thêm vài nguyên liệu để nấu cơm ngon hơn: Để cơm được ngon hơn bạn nên cho gia vị vào nước trước khi bạn bắt đầu nấu cơm, như vậy, gạo mới hấp thu được gia vị trong quá trình nấu. Bạn thêm 1 muỗng cà phê muối, 1/2 muỗng cà phê giấm vào nồi cơm hoặc nhỏ 2 - 3 giọt dầu oliu hay dầu mè vào gạo trước khi nấu.")
            st.write("   - Nấu cơm: Lau bên ngoài lòng nồi bằng khăn khô, đảm bảo bề mặt nồi khô ráo, đặt lòng nồi vào trong thân nồi, xoay nhẹ sao cho đáy nồi tiếp xúc trực tiếp với mâm nhiệt. Đóng nắp lại, cắm điện và bật công tắc.")
            st.write("   - Ủ cơm: Khi cơm chín, công tắc sẽ chuyển sang chế độ giữ ấm. Lúc này, bạn nên để nồi nấu thêm khoảng 10 - 15 phút nữa, việc này sẽ giúp cơm khô bề mặt, chín đều và hạt cơm không bị dính vào thân nồi. Sau đó dùng muỗng hay đũa cả xới cơm lên sẽ giúp cơm tơi và cho ra bát để thưởng thức.")
            st.markdown("[Xem hướng dẫn chi tiết qua video](https://youtu.be/QJZUwiJhKZ0?si=IO1AvQjjiCk6GzLO)")

def display_meal(food_items, meal_name):
    for idx, (food_name, image_path) in enumerate(food_items):
        with st.container(border=True):
            col1, col2, col3 = st.columns([0.3, 0.5, 0.2], vertical_alignment="center")
            with col1:
                st.image(image_path, width=100)
            with col2:
                st.write(food_name)
            with col3:
                # Thêm meal_name vào key để mỗi nút là duy nhất cho từng bữa
                if st.button("Chi tiết", key=f"{meal_name}_{food_name}_{idx}"):
                    details(food_name, image_path)

# Dữ liệu mẫu cho từng bữa ăn
breakfast_items = [
    ("Cơm", "food_images/com.jpg"),
    ("Thịt Kho Tàu", "food_images/thitKhoTau.jpg"),
    ("Rau Muống Xào Tỏi", "food_images/rauMuongXaoToi.jpg"),
    ("Canh Rau Muống Sấu", "food_images/canhRauMuongSau.jpg")
]

lunch_items = [
    ("Cơm", "food_images/com.jpg"),
    ("Thịt Kho Tàu", "food_images/thitKhoTau.jpg"),
    ("Rau Muống Xào Tỏi", "food_images/rauMuongXaoToi.jpg"),
    ("Canh Rau Muống Sấu", "food_images/canhRauMuongSau.jpg")
]

dinner_items = [
    ("Cơm", "food_images/com.jpg"),
    ("Thịt Kho Tàu", "food_images/thitKhoTau.jpg"),
    ("Rau Muống Xào Tỏi", "food_images/rauMuongXaoToi.jpg"),
    ("Canh Rau Muống Sấu", "food_images/canhRauMuongSau.jpg")
]

st.title("Weekly Menu")
st.write("NutriHome cung cấp tính năng xây dựng thực đơn cá nhân hóa hàng tuần dựa trên dữ liệu như chiều cao, cân nặng, và tình trạng sức khỏe của cá nhân. Hệ thống sử dụng dữ liệu dinh dưỡng đáng tin cậy từ USDA Food Data Central, giúp đảm bảo sự chính xác về hàm lượng dinh dưỡng trong các món ăn.")

# Tabs cho các ngày trong tuần
tabs = st.tabs(["**Thứ Hai**", "**Thứ Ba**", "**Thứ Tư**", "**Thứ Năm**", "**Thứ Sáu**", "**Thứ Bảy**", "**Chủ Nhật**"])

# Nội dung cho từng ngày
with tabs[0]:  # Thứ Hai
    with st.expander("**Tổng lượng dưỡng chất từ bữa ăn**"):
        st.header("**Tổng lượng dưỡng chất từ bữa ăn**", divider="grey")
        # Dữ liệu cho biểu đồ tròn
        labels = ['Carbs', 'Fats', 'Protein']
        values = [70, 10, 20]

        # Tạo biểu đồ tròn với plotly
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

        # Tùy chỉnh biểu đồ tròn
        fig.update_traces(
            hoverinfo='label+percent',
            textinfo='label+percent',  # Chỉ hiển thị tên thành phần
            textfont=dict(size=15, color='white', family='Arial Black'),
            marker=dict(colors=['#FFCC00', '#66b3ff', '#9933CC']),  # Màu sắc cho các thành phần
            showlegend=False
        )
        
        fig.update_layout(
            margin=dict(t=10, b=10, l=10, r=10),
            width=700,  # Độ rộng biểu đồ
            height=300  # Độ cao biểu đồ
        )

        # Hiển thị biểu đồ trong Streamlit
        st.plotly_chart(fig)

        st.write("**Chi tiết**")

        table = """
                <style>
                    table {
                        width: 100%;
                    }
                    th, td {
                        text-align: middle;
                        padding: 8px;
                    }
                </style>

                <table>
                    <tr>
                        <th>Hạng mục</th>
                        <th>Giá trị</th>
                    </tr>
                    <tr>
                        <td>Total calories</td>
                        <td>1000cal</td>
                    </tr>
                    <tr>
                        <td>Carbohydrates</td>
                        <td>210g</td>
                    </tr>
                    <tr>
                        <td>Fat</td>
                        <td>30g</td>
                    </tr>
                    <tr>
                        <td>Protein</td>
                        <td>60g</td>
                    </tr>
                </table>
                """

                # Hiển thị bảng trong Streamlit
        st.markdown(table, unsafe_allow_html=True)

    st.header("Hôm nay là Thứ Hai, thực đơn của gia đình bạn là:")

    breakFast, lunch, dinner = st.tabs(["Bữa sáng", "Bữa trưa", "Bữa tối"])

    with breakFast:
        st.subheader("Bữa sáng:")
        display_meal(breakfast_items, meal_name="breakfast")

    with lunch:
        st.subheader("Bữa trưa:")
        display_meal(lunch_items, meal_name="lunch")

    with dinner:
        st.subheader("Bữa tối:")
        display_meal(dinner_items, meal_name="dinner")