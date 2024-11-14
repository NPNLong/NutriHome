import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import json
import requests

BACKEND_API = "http://127.0.0.1:5000"

# Đổi trạng thái khi nhấn nút
def toggle_favorite():
    st.session_state.favorite = not st.session_state.favorite

# Hàm tạo các mục trong bữa ăn
@st.dialog("Chi tiết món ăn", width="large")
def details(id):
    get_all_api = BACKEND_API + "/api/recipes/detail"
    response = requests.get(get_all_api, data=json.dumps({"recipe_id": id}), headers = {
        'Content-Type': 'application/json',
    })
    print(response.status_code)
    print(response.json())

    st.session_state.food_details =  response.json()["data"]

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
            for idx, ingredients in enumerate(st.session_state.food_details["ingredients"]):
                st.write(f" - {ingredients["name"]} {ingredients["quantity"]} {ingredients["unit"]}")
            
            st.text("")
            
            st.subheader("Cách làm")
            for idx, steps in enumerate(st.session_state.food_details["steps"]):
                st.write(f" - {steps}")
            # Video
            # st.markdown("[Xem hướng dẫn chi tiết qua video](https://youtu.be/QJZUwiJhKZ0?si=IO1AvQjjiCk6GzLO)")

# Hàm hiển thị từng món ăn trong bữa
def display_meal(meal, day):
    for idx in range(0, len(st.session_state.weekly_menu[day][meal]["listOfFoods"]), 2):
        c1, c2 = st.columns(2)

        # First food item in the current pair (idx)
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
                        details(food1["recipe_id"])

        # Second food item in the current pair (idx + 1), if it exists
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
                            details(food2["recipe_id"])

if st.session_state.logged_in:

    #Chart
    get_all_api = BACKEND_API + "/api/home/chart"
    response = requests.get(
        get_all_api,
        data=json.dumps(
            {
                "user_id": st.session_state.user["id"]
            }
        ),
        headers = {'Content-Type': 'application/json',}
    )
    print(response.status_code)
    if response.status_code == 200:
        st.session_state.user["absorbed_carbs"] = response.json()["data"]["chart"]["absorbedCarbs"]
        st.session_state.user["absorbed_protein"] = response.json()["data"]["chart"]["absorbedProtein"]
        st.session_state.user["absorbed_fat"] = response.json()["data"]["chart"]["absorbedFat"]
        st.session_state.user["absorbed_calories"] = response.json()["data"]["chart"]["absorbedCalories"]
        st.session_state.user["target_carbs"] = response.json()["data"]["chart"]["goalCarbs"]
        st.session_state.user["target_protein"] = response.json()["data"]["chart"]["goalProtein"]
        st.session_state.user["target_fat"] = response.json()["data"]["chart"]["goalFat"]
        st.session_state.user["target_calories"] = response.json()["data"]["chart"]["goalCalories"]

    #Weekly menu:
    get_all_api = BACKEND_API + "/api/weekly_menu"
    response = requests.get(
        get_all_api,
        data=json.dumps(
            {
                "user_id": st.session_state.user["id"]
            }
        ),
        headers = {'Content-Type': 'application/json',}
    )
    print(response.status_code)
    if response.status_code == 200:
        date1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        date2 = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        meal = ["Breakfast", "Lunch", "Dinner"]
        for i, day in enumerate(date1):
            for j, meal_type in enumerate(meal):
                st.session_state.weekly_menu[day][meal_type]["listOfFoods"] = response.json()["data"]["menu"][date2[i]][meal_type.lower()]

        

    st.title(f"Chào mừng {st.session_state.user["fullname"]}! Hôm nay bạn muốn ăn gì?")
    st.text("")
    st.subheader("**📈 Chỉ số dinh dưỡng của bạn:**")

    def create_pie_chart(current, goal, label, color):
        labels = ['done', 'notDone']
        sizes = [current/goal, 1 - current/goal]
        pie_chart = px.pie(names=labels, values=sizes, color_discrete_sequence=[color, '#C0C0C0'], hole=0.7)
        pie_chart.update_layout(
            annotations=[dict(text=f"{current}/{goal}<br>{label}", x=0.5, y=0.5, font_size=22, showarrow=False)],
            showlegend=False,
            width=180,
            height=180,
            margin=dict(t=0, b=0, l=0, r=0)
        )
        pie_chart.update_traces(textinfo='none', sort=False)
        return pie_chart

    # Generate charts
    pie_calories = create_pie_chart(st.session_state.user["absorbed_calories"], st.session_state.user["target_calories"], 'calories', '#DC143C')
    pie_carbs = create_pie_chart(st.session_state.user["absorbed_carbs"], st.session_state.user["target_carbs"], 'carbs', '#FA8072')
    pie_fat = create_pie_chart(st.session_state.user["absorbed_fat"], st.session_state.user["target_fat"], 'fat', '#66b3ff')
    pie_protein = create_pie_chart(st.session_state.user["absorbed_protein"], st.session_state.user["target_protein"], 'protein', '#9933CC')

    # Display in a grid
    with st.container(border=True):
        col1, col2, col3, col4 = st.columns(4)
        col1.plotly_chart(pie_calories, use_container_width=True)
        col2.plotly_chart(pie_carbs, use_container_width=True)
        col3.plotly_chart(pie_fat, use_container_width=True)
        col4.plotly_chart(pie_protein, use_container_width=True)

    st.text("")
    st.text("")
    st.subheader("**📄 Thực đơn bữa ăn tiếp theo:**")

    display_meal(st.session_state.meal, st.session_state.day_of_week)

    thuc_don = st.button("Theo dõi thực đơn của bạn", use_container_width=True, type="primary")
    if thuc_don:
                st.switch_page("pages/features/weeklyMenu.py")

    st.text("")
    st.text("")
    st.subheader("Hãy cùng nhau nấu một bữa thật ngon nào!")
    st.text("")

    with st.container(border=True):
        col1, col2 = st.columns([0.4, 0.6], vertical_alignment="center")

        with col1:
            st.image("features_images/weeklyMenu.jpg")

        with col2:
            st.write("**Weekly Menu**")
            st.write("Bạn chưa biết hôm nay mình sẽ ăn gì, ngày mai mình sẽ ăn gì? Bạn không biết làm cách nào để có một bữa ăn thật Healthy? Chỉ cần nhấp chuột một lần, bạn đã có thể nhận được một thực đơn Healthy như bạn mong muốn mà không cần phải suy nghĩ đắn đo.")
        
        weeklyMenu_button = st.button("Tạo một thực đơn thật Healthy!", use_container_width=True)
        if weeklyMenu_button:
            st.switch_page("pages/features/weeklyMenu.py")

    st.text("")

    with st.container(border=True):
        col1, col2 = st.columns([0.6, 0.4], vertical_alignment="center")

        with col2:
            st.image("features_images/recipes.jpg")

        with col1:
            st.write("**Recipes**")
            st.write("Nơi đây là một bách khoa toàn thư về các món ăn, các bạn có thể tìm kiếm những món ăn mình yêu thích, tham khảo chi tiết hàm lượng dinh dưỡng của món ăn đó. Đặc biệt, NutriHome hướng dẫn các bạn nấu ăn một cách tỉ mỉ và chi tiết thông quá từng bước.")
        
        recipes_button = st.button("Đến xem những công thức nấu ăn tuyệt đỉnh nào!", use_container_width=True)
        if recipes_button:
            st.switch_page("pages/features/recipes.py")

    st.text("")
    
    with st.container(border=True):
        col1, col2 = st.columns([0.4, 0.6], vertical_alignment="center")

        with col1:
            st.image("features_images/history.jpg")

        with col2:
            st.write("**History**")
            st.write("Bạn có thể xem lại lịch sử ăn uống của bản thân trong 3 ngày vừa qua. Tại đây NutriHome sẽ tính toán chi tiết hàm lượng mà các bạn đã hấp thụ, đưa ra những thông số cụ thể để các bạn có thể tham khảo một cách trực quan nhất.")
        
        history_button = st.button("Đến xem hôm nay bạn đã ăn những gì nào!", use_container_width=True)
        if history_button:
            st.switch_page("pages/features/history.py")

    st.text("")
    
    with st.container(border=True):
        col1, col2 = st.columns([0.6, 0.4], vertical_alignment="center")

        with col2:
            st.image("features_images/community.jpg")

        with col1:
            st.write("**Community**")
            st.write("Đây là một cộng đồng, nơi các bạn có thể chia sẻ cho nhau những món ăn và công thức nấu ăn độc đáo mà các bạn khám phá ra. Đồng thời, các bạn có thể lưu lại những công thức mà các bạn yêu thích hoặc tâm đắc.")
        
        community_button = st.button("Hãy cùng chia sẻ những công thức nấu ăn mà bạn đã khám phá ra nhé!", use_container_width=True)
        if community_button:
            st.switch_page("pages/features/community.py")

    # What's new (later)
    # st.text("")
    # st.text("")
    # st.subheader("Có gì mới", divider="gray")
    # st.text("")
    # col1, col2, col3 = st.columns([1, 1, 1], gap = "small", vertical_alignment="top")

    # with col1:
    #     with st.form("com1"):
    #         st.image("features_images/ex.jpg")
    #         st.write("**Công thức nấu ngon tuyệt**")
    #         st.write("Công thức nấu ngon tuyệt được phát hiện bởi NPNLong")
    #         switch_page = st.form_submit_button("Xem ngay", use_container_width=True)
    #         if switch_page:
    #              st.switch_page("pages/features/community.py")

    # with col2:
    #     with st.form("com2"):
    #         st.image("features_images/ex.jpg")
    #         st.write("**Công thức nấu tuyệt ngon**")
    #         st.write("Công thức nấu ngon tuyệt được phát hiện bởi LongNPN")
    #         switch_page = st.form_submit_button("Xem ngay", use_container_width=True)
    #         if switch_page:
    #              st.switch_page("pages/features/community.py")

    # with col3:
    #     with st.form("com3"):
    #         st.image("features_images/ex.jpg")
    #         st.write("**Công thức nấu độc lạ Bình Dương**")
    #         st.write("Công thức nấu ngon tuyệt được phát hiện bởi kemngott")
    #         switch_page = st.form_submit_button("Xem ngay", use_container_width=True)
    #         if switch_page:
    #              st.switch_page("pages/features/community.py")

else:
    st.title("Chào mừng!")
    st.text("")
    st.write("NutriHome là ứng dụng tư vấn dinh dưỡng thông minh, sử dụng AI để tính toán chính xác nhu cầu dinh dưỡng cá nhân. Ứng dụng tạo thực đơn tùy chỉnh theo sở thích và theo dõi lịch sử ăn uống của người dùng, giúp duy trì thói quen ăn uống lành mạnh.")
    
    st.text("")
    st.text("")

    with st.container(border=True):
        st.subheader("Bạn chưa biết hôm nay sẽ ăn gì? Bạn muốn tạo một thực đơn thật Healthy? Hãy cùng bắt đầu với chúng tôi!")
        st.text("")
        login = st.button("Tạo thực đơn ngay!", type="primary", use_container_width = True)

        if login:
            st.session_state.login_page = True
            st.rerun()

    st.text("")
    st.text("")
    st.subheader("NutriHome sẽ đem lại cho bạn những gì?")
    st.text("")

    with st.container(border=True):
        col1, col2 = st.columns([0.4, 0.6], vertical_alignment="center")

        with col1:
            st.image("features_images/weeklyMenu.jpg")

        with col2:
            st.write("**Weekly Menu**")
            st.write("Bạn chưa biết hôm nay mình sẽ ăn gì, ngày mai mình sẽ ăn gì? Bạn không biết làm cách nào để có một bữa ăn thật Healthy? Chỉ cần nhấp chuột một lần, bạn đã có thể nhận được một thực đơn Healthy như bạn mong muốn mà không cần phải suy nghĩ đắn đo.")

    st.text("")

    with st.container(border=True):
        col1, col2 = st.columns([0.6, 0.4], vertical_alignment="center")

        with col2:
            st.image("features_images/recipes.jpg")

        with col1:
            st.write("**Recipes**")
            st.write("Nơi đây là một bách khoa toàn thư về các món ăn, các bạn có thể tìm kiếm những món ăn mình yêu thích, tham khảo chi tiết hàm lượng dinh dưỡng của món ăn đó. Đặc biệt, NutriHome hướng dẫn các bạn nấu ăn một cách tỉ mỉ và chi tiết thông quá từng bước.")

    st.text("")
    
    with st.container(border=True):
        col1, col2 = st.columns([0.4, 0.6], vertical_alignment="center")

        with col1:
            st.image("features_images/history.jpg")

        with col2:
            st.write("**History**")
            st.write("Bạn có thể xem lại lịch sử ăn uống của bản thân trong 3 ngày vừa qua. Tại đây NutriHome sẽ tính toán chi tiết hàm lượng mà các bạn đã hấp thụ, đưa ra những thông số cụ thể để các bạn có thể tham khảo một cách trực quan nhất.")

    st.text("")
    
    with st.container(border=True):
        col1, col2 = st.columns([0.6, 0.4], vertical_alignment="center")

        with col2:
            st.image("features_images/community.jpg")

        with col1:
            st.write("**Community**")
            st.write("Đây là một cộng đồng, nơi các bạn có thể chia sẻ cho nhau những món ăn và công thức nấu ăn độc đáo mà các bạn khám phá ra. Đồng thời, các bạn có thể lưu lại những công thức mà các bạn yêu thích hoặc tâm đắc.")