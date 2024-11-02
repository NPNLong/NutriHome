import streamlit as st
from PIL import Image

# Initialize favorite status
if 'favorite' not in st.session_state:
    st.session_state.favorite = False

# Initialize session for comments and posts
if "posts" not in st.session_state:
    st.session_state.posts = [
        {
            "title": "Cách nấu cơm siêu ngon!",
            "author": "Nguyễn Văn A",
            "description": "Nấu ngon thì cơm sẽ siêu ngon!",
            "image": "food_images/com.jpg",
            "comments": ["Vũ Mạnh Cường: Bịp vcl", "Hoàng Khánh Chi: Top 1 công thức tôi luôn tin tưởng", "Phạm Anh Tuấn: Cho thêm giấm ngon x100"]
        },
        {
            "title": "SGUET",
            "author": "Lê Thị B",
            "description": "Đỉnh mãi SG!",
            "image": "features_images/sg.jpg",
            "comments": ["Nguyễn Huy Thái: Ảnh xấu vcl"]
        }
    ]

@st.dialog("Bài viết", width="large")
def addNewPost():
    col1, col2 = st.columns([1, 1], gap='medium')

    with col1:
        uploaded_image = st.file_uploader("Ảnh bài viết", type=["jpg", "jpeg", "png"])
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, use_column_width=True)

    with col2:
        title = st.text_input("Tiêu đề bài viết")
        description = st.text_area("Mô tả", placeholder="Write your post's description here...")

    if st.button("Chia sẻ bài viết"):
        st.session_state.posts.append({
            "title": title,
            "author": f"{st.session_state.fullname}",  # Update author dynamically if needed
            "description": description,
            "image": image,
            "comments": []
        })
        st.rerun()
    

def toggle_favorite():
    st.session_state.favorite = not st.session_state.favorite

st.title("Community")
st.write("NutriHome cung cấp diễn đàn, giúp những người có cùng đam mê ẩm thực có thể chia sẻ những cách chế biến thực phẩm sáng tạo và độc đáo của riêng mình.")

st.header("**What's new?**", divider='gray')
st.text('')

col1, col2 = st.columns([42, 38], vertical_alignment='center')
with col1:
    st.write("**Bạn muốn chia sẻ 'bí kíp nấu ăn' nào không?**")
with col2:
    add_new_post = st.button("Add new post", use_container_width=True, type='primary')
    if(add_new_post):
        addNewPost()

for i, post in enumerate(st.session_state.posts):
    st.text('')
    with st.container(border=True):
        st.subheader(post["title"], divider='gray')
        col1, col2 = st.columns([35,65])

        with col1:
            st.image(post["image"])

            c1, c2 = st.columns([4, 6])

            with c1:
                # Hiển thị nút yêu thích
                if st.session_state.favorite:
                    if st.button("❤️", on_click=toggle_favorite, key=f"favorite_{i}", use_container_width=True):
                        st.write("Bạn đã thích món ăn này!")
                else:
                    if st.button("♡", on_click=toggle_favorite, key=f"favorite_{i}", use_container_width=True):
                        st.write("Hãy yêu thích món ăn này!")

            user_comment = st.text_area("**Bình luận**", placeholder="Write your comment here...", key=f"comment_input_{i}")
            commentary = st.button("Bình luận", use_container_width=True, type='primary', key=f"comment_button_{i}")

            if (commentary) and user_comment:
                post["comments"].append(f"{st.session_state.fullname}: {user_comment}")
                st.rerun()
            

        with col2:
            with st.container(border=True):
                st.write(f"**Author:** {post['author']}")
            with st.container(border=True):
                st.write("**Mô tả**")
                st.write(post["description"])

            with st.container(border=True):
                st.write("**Bình luận**")

                for comment in post["comments"]:
                    with st.container(border=True):
                        st.write("*" + comment + "*")