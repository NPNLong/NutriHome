import streamlit as st
import plotly.express as px

if st.session_state.logged_in:
    st.title(f"Chào mừng {st.session_state.fullname}! Hôm nay bạn muốn ăn gì?")
    st.text("")

    labels = ['A', 'B']
    sizes = [75, 25]
    colors = ['#3366CC', '#C0C0C0']

    fig = px.pie(names=labels, values=sizes, title="Lượng calories đã hấp thụ", color_discrete_sequence=colors, hole = 0.70)
    fig.update_traces(textinfo='none')

    currentCalories = 1500
    goalCalories = 2000

    fig.update_layout(annotations=[dict(text=str(currentCalories) + '/' + str(goalCalories) + '<br>calories', x=0.5, y=0.5, font_size=25, showarrow=False)],
                        showlegend=False, width = 380, height = 380)

    with st.container(border=True, height=400):
        col1, col2, col3 = st.columns([1, 8, 1])
        with col2:
            st.plotly_chart(fig, use_container_width=True)

    st.text("")
    st.text("")
    st.subheader("**📄 Thực đơn bữa ăn tiếp theo:**")
    st.text("")

    with st.container(border=True):
        col1, col2 = st.columns([0.3, 0.7], vertical_alignment="center")
        with col1: 
            st.image("food_images/com.jpg", width = 100)
        with col2:
            st.write("Cơm")

    with st.container(border=True):
        col1, col2 = st.columns([0.3, 0.7], vertical_alignment="center")
        with col1: 
            st.image("food_images/thitKhoTau.jpg", width = 100)
        with col2:
            st.write("Thịt Kho Tàu")

    with st.container(border=True):
        col1, col2 = st.columns([0.3, 0.7], vertical_alignment="center")
        with col1: 
            st.image("food_images/rauMuongXaoToi.jpg", width = 100)
        with col2:
            st.write("Rau Muống Xào Tỏi")

    with st.container(border=True):
                col1, col2 = st.columns([0.3, 0.7], vertical_alignment="center")
                with col1: 
                    st.image("food_images/canhRauMuongSau.jpg", width = 100)
                with col2:
                    st.write("Canh Rau Muống Sấu")

    st.text("")
    thuc_don = st.button("Theo dõi thực đơn của bạn", use_container_width=True, type="primary")
    if thuc_don:
                st.switch_page("pages/features/weeklyMenu.py")
    muc_tieu = st.button("Theo dõi mục tiêu của bạn", use_container_width=True)
    if muc_tieu:
                st.switch_page("pages/personal/profile.py")

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

    st.text("")
    st.text("")
    st.subheader("Có gì mới", divider="gray")
    st.text("")

    col1, col2, col3 = st.columns([1, 1, 1], gap = "small", vertical_alignment="top")

    with col1:
        with st.form("com1"):
            st.image("features_images/ex.jpg")
            st.write("**Công thức nấu ngon tuyệt**")
            st.write("Công thức nấu ngon tuyệt được phát hiện bởi NPNLong")
            switch_page = st.form_submit_button("Xem ngay", use_container_width=True)
            if switch_page:
                 st.switch_page("pages/features/community.py")

    with col2:
        with st.form("com2"):
            st.image("features_images/ex.jpg")
            st.write("**Công thức nấu tuyệt ngon**")
            st.write("Công thức nấu ngon tuyệt được phát hiện bởi LongNPN")
            switch_page = st.form_submit_button("Xem ngay", use_container_width=True)
            if switch_page:
                 st.switch_page("pages/features/community.py")

    with col3:
        with st.form("com3"):
            st.image("features_images/ex.jpg")
            st.write("**Công thức nấu độc lạ Bình Dương**")
            st.write("Công thức nấu ngon tuyệt được phát hiện bởi kemngott")
            switch_page = st.form_submit_button("Xem ngay", use_container_width=True)
            if switch_page:
                 st.switch_page("pages/features/community.py")

else:
    st.title("Chào mừng!")
    st.text("")
    st.write("NutriHome là ứng dụng tư vấn dinh dưỡng thông minh, sử dụng AI để tính toán chính xác nhu cầu dinh dưỡng cá nhân. Ứng dụng tạo thực đơn tùy chỉnh theo sở thích và theo dõi lịch sử ăn uống của người dùng, giúp duy trì thói quen ăn uống lành mạnh.")
    
    st.text("")
    st.text("")

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