import streamlit as st
import plotly.graph_objects as go

st.title("History")
st.write("NutriHome cung cấp tính năng ghi lại mọi món ăn trong ngày, bao gồm bữa chính tại nhà, bữa ăn ngoài và món ăn vặt. Người dùng có thể dễ dàng theo dõi chế độ ăn uống của mình bằng cách nhập dữ liệu hoặc chụp hóa đơn, giúp người dùng nắm bắt tình trạng dinh dưỡng và điều chỉnh thói quen ăn uống cho phù hợp với sức khỏe của từng thành viên trong gia đình.")

st.text('')
st.subheader("Thống kê hàm lượng dinh dưỡng", divider="gray")
# Tên các cột
categories = ['Hôm nay', 'Hôm qua', 'Hôm kia']
# Dữ liệu cho 3 thành phần
component1 = [60, 75, 30]
component2 = [30, 50, 60]
component3 = [100, 135, 70]

# Tạo biểu đồ cột chồng
fig = go.Figure(data=[
    go.Bar(name='Carbs', x=categories, y=component1, text=component1, texttemplate='%{text:.2f}', textposition='inside', marker_color='#FFCC00', textfont=dict(color='white', size=14)),
    go.Bar(name='Fat', x=categories, y=component2, text=component2, texttemplate='%{text:.2f}', textposition='inside', marker_color='#66b3ff', textfont=dict(color='white', size=14)),
    go.Bar(name='Protein', x=categories, y=component3, text=component3, texttemplate='%{text:.2f}', textposition='inside', marker_color='#9933CC', textfont=dict(color='white', size=14))
])

# Đặt chế độ hiển thị thành cột chồng
fig.update_layout(barmode='stack')

# Hiển thị biểu đồ trên Streamlit
st.plotly_chart(fig)

st.text('')
st.subheader("Lịch sử ăn uống", divider="gray")