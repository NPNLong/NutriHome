import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Khởi tạo trạng thái của nút yêu thích
if 'favorite' not in st.session_state:
    st.session_state.favorite = False

if "isSearch" not in st.session_state:
    st.session_state.isSearch = False

if "inputSearch" not in st.session_state:
    st.session_state.inputSearch = ""

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
            st.session_state.inputSearch = search_food_name
            st.rerun()
    with col3:
        if st.button("Reset", use_container_width=True):
            st.session_state.isSearch = False
            st.session_state.inputSearch = ""
            st.rerun()

st.subheader("List of foods", divider="grey")

if st.session_state.isSearch and st.session_state.inputSearch.lower() in ["cơm"]:
    st.write("**You are searching**")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        with st.container(border=True):
            st.image("food_images/com.jpg")
            st.write("**Cơm**")
            st.write(" - **Thời gian nấu**" + ": 40 phút")
            st.write(" - **Độ khó**" + ": ⭐")
            st.write(" - **Rating**" + ": ⭐⭐⭐⭐ ")
            getDetails = st.button("Chi tiết", use_container_width=True)
            if getDetails:
                details("Cơm", "food_images/com.jpg")

else:
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        with st.container(border=True):
            st.image("food_images/com.jpg")
            st.write("**Cơm**")
            st.write(" - **Thời gian nấu**" + ": 40 phút")
            st.write(" - **Độ khó**" + ": ⭐")
            st.write(" - **Rating**" + ": ⭐⭐⭐⭐ ")
            getDetails = st.button("Chi tiết", use_container_width=True, key = 1)
            if getDetails:
                details("Cơm", "food_images/com.jpg")

        with st.container(border=True):
            st.image("food_images/canhRauMuongSau.jpg")
            st.write("**Canh rau muống sấu**")
            st.write(" - **Thời gian nấu**" + ": 15 phút")
            st.write(" - **Độ khó**" + ": ⭐")
            st.write(" - **Rating**" + ": ⭐⭐⭐⭐ ")
            getDetails = st.button("Chi tiết", use_container_width=True, key = 4)
            if getDetails:
                details("Canh rau muống sấu", "food_images/ccanhRauMuongSau.jpg")

    with col2:
        with st.container(border=True):
            st.image("food_images/thitKhoTau.jpg")
            st.write("**Thịt kho tàu**")
            st.write(" - **Thời gian nấu**" + ": 45 phút")
            st.write(" - **Độ khó**" + ": ⭐")
            st.write(" - **Rating**" + ": ⭐⭐⭐⭐⭐ ")
            getDetails = st.button("Chi tiết", use_container_width=True, key = 2)
            if getDetails:
                details("Thịt kho tàu", "food_images/thitKhoTau.jpg")

    with col3:
        with st.container(border=True):
            st.image("food_images/rauMuongXaoToi.jpg")
            st.write("**Rau muống xào tỏi**")
            st.write(" - **Thời gian nấu**" + ": 15 phút")
            st.write(" - **Độ khó**" + ": ⭐")
            st.write(" - **Rating**" + ": ⭐⭐ ")
            getDetails = st.button("Chi tiết", use_container_width=True, key = 3)
            if getDetails:
                details("Rau muống xào tỏi", "food_images/rauMuongXaoToi.jpg")