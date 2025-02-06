# 🍽️ **NutriHome: Ứng Dụng Gợi Ý Thực Đơn Gia Đình**

---

## 📖 **Mục Lục**  
1. [Giới thiệu](#gioi-thieu)  
2. [Cài đặt và Cách sử dụng](#cai-dat-va-cach-su-dung)  
3. [Tính năng](#tinh-nang)  
4. [Hình ảnh giao diện](#hinh-anh-giao-dien)  
5. [Hướng phát triển](#huong-phat-trien)
6. [Thành viên nhóm](#member-list)

---
<a id="gioi-thieu"></a>
## 🌟 **Giới thiệu**
**NutriHome** là ứng dụng web giúp gợi ý thực đơn gia đình dựa trên lịch sử bữa ăn, nhu cầu dinh dưỡng cá nhân và hóa đơn mua sắm. Ứng dụng hỗ trợ người dùng xây dựng chế độ ăn uống phù hợp với sức khỏe và thói quen sinh hoạt của gia đình.
Ứng dụng giúp bạn theo dõi và tổ chức thông tin sách dễ dàng, tiện lợi với giao diện thân thiện.

🎯 **Lợi ích của NutriHome**

  🥗 Gợi ý thực đơn cá nhân hóa theo nhu cầu dinh dưỡng.
  
  📊 Theo dõi lượng dinh dưỡng tiêu thụ thông qua lịch sử ăn uống.
  
  🏡 Xây dựng thực đơn cho cả gia đình.
  
  📷 Lưu lịch sử món ăn bằng xử lý hình ảnh hóa đơn.
  
  🍽️ Diễn đàn chia sẻ công thức nấu ăn.

---
<a id="cai-dat-va-cach-su-dung"></a>
## 🚀 **Cài đặt và Cách sử dụng**  
### 💻 **Yêu cầu hệ thống**  
- Python 3.x
- Flask
- Streamlit
- SQLite
- Gemini API

### 🔧 **Hướng dẫn cài đặt**
**Clone ứng dụng về máy**
```bash
git clone https://github.com/Akapi895/NutriHome.git
cd NutriHome
```
**Cài đặt môi trường ảo và dependencies**
```bash
python -m venv venv
source venv/bin/activate  # Trên macOS/Linux
venv\Scripts\activate  # Trên Windows
pip install -r requirements.txt
```
**Chạy ứng dụng**
```bash
cd frontend
streamlit run app.py
```
```bash
cd backend
python app.py
```
```bash
cd menu_service
python app.py
```

---
<a id="tinh-nang"></a>
## ⚙️ **Tính năng**  

### 🥗 **1. Gợi ý thực đơn cá nhân hóa**  
- Người dùng nhập **cân nặng, chiều cao, mức độ vận động** để tính toán nhu cầu dinh dưỡng.
- Hệ thống gợi ý món ăn phù hợp với từng thành viên trong gia đình.

### 🏡 **2. Xây dựng thực đơn theo nhóm (gia đình)**  
- Tạo nhóm gia đình để lập thực đơn theo tuần.
- Đảm bảo các thành viên có chế độ ăn uống phù hợp.

### 🧾 **3. Lưu lịch sử ăn uống**  
- Lưu thông tin món ăn từ hóa đơn bằng xử lý hình ảnh.
- Ghi nhận lịch sử ăn uống bên ngoài để theo dõi lượng dưỡng chất đã tiêu thụ.

### 🍳 **4. Hướng dẫn cách nấu**  
- Đề xuất công thức món ăn phù hợp với thực đơn.
- Hướng dẫn chi tiết cách chế biến từng món.

### 📚 **5. Diễn đàn chia sẻ công thức**  
- Người dùng có thể chia sẻ công thức nấu ăn.
- Lưu công thức yêu thích và tính toán giá trị dinh dưỡng.

---
<a id="member-list"></a>
## 👥 **Thành viên nhóm**
- Nguyễn Phước Ngưỡng Long: Frontend Developer
- Hoàng Khánh Chi: Backend Developer
- Vũ Mạnh Cường: Backend Developer
- Phạm Anh Tuấn: AI Engineer

---

Cảm ơn bạn đã sử dụng **NutriHome**! 🚀
