import streamlit as st
import pandas as pd

# 1. CẤU HÌNH TRANG
st.set_page_config(page_title="Pizza & Relax - Mercure Vibe", layout="centered")

# 2. GIAO DIỆN & VIBE (Sử dụng CSS tùy chỉnh)
# Màu xanh đại dương (#003366), font chữ thanh lịch, nút bấm bo góc mềm mại
st.markdown("""
<style>
    .stApp {
        background-color: #F9FAFB; /* Màu nền trắng xám như cát mịn */
    }
    h1, h2, h3 {
        color: #003366 !important; /* Xanh đại dương thẫm */
        font-family: 'Georgia', serif; 
        font-weight: 400;
    }
    .stButton>button {
        background-color: #003366;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00509E;
        color: white;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    div[data-testid="stMetricValue"] {
        color: #C19A6B; /* Màu vàng cát hoàng hôn cho phần giá tiền */
    }
</style>
""", unsafe_allow_html=True)

# 3. TIÊU ĐỀ
st.markdown("<h1 style='text-align: center;'>🍕 La Pizza de Mercure</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666; font-size: 16px; font-style: italic;'>Hương vị tinh tế bên tiếng sóng vỗ rì rào...</h3>", unsafe_allow_html=True)
st.write("---")

# 4. GIẢI QUYẾT RÀO CẢN: TỪ ĐIỂN DỮ LIỆU
# Bạn chỉ cần thay đổi tên món và giá tiền ở cục dữ liệu này cho khớp 100% với app cũ.
PIZZA_MENU = {
    "Pizza Margherita (Phô mai & Cà chua)": 150000,
    "Pizza Pepperoni (Xúc xích Ý)": 180000,
    "Pizza Hawaiian (Dăm bông & Dứa)": 170000,
    "Pizza Seafood (Hải sản thanh mát)": 250000,
    "Pizza Chicken BBQ (Gà nướng)": 190000
}

st.subheader("Thực Đơn Chạm Đến Cảm Xúc")

# Bộ lưu trữ món ăn khách chọn
order = {}

# Hiển thị danh sách món ăn
for pizza, price in PIZZA_MENU.items():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"**{pizza}**")
        st.write(f"*{price:,} VNĐ*")
    with col2:
        # Nút chọn số lượng bo góc gọn gàng
        qty = st.number_input(f"Số lượng {pizza}", min_value=0, max_value=20, value=0, key=pizza, label_visibility="collapsed")
        if qty > 0:
            order[pizza] = qty

st.write("---")

# 5. KHU VỰC HÓA ĐƠN & THANH TOÁN
st.subheader("🧾 Hóa Đơn Trải Nghiệm")

if order:
    total_price = 0
    bill_data = []
    
    for pz, q in order.items():
        cost = q * PIZZA_MENU[pz]
        total_price += cost
        bill_data.append({"Món ăn": pz, "Số lượng": q, "Thành tiền (VNĐ)": f"{cost:,}"})
    
    # Hiển thị bảng
    df_bill = pd.DataFrame(bill_data)
    st.table(df_bill)
    
    # Hiển thị tổng tiền với màu sắc ấm áp
    st.metric(label="Tổng Chi Phí", value=f"{total_price:,} VNĐ")
    
    # Nút xác nhận
    if st.button("Xác nhận & Chờ phục vụ"):
        st.success("Cảm ơn bạn! Bếp đang chuẩn bị món ăn với tất cả sự nâng niu. Hãy nhâm nhi chút đồ uống và tận hưởng không gian nhé.")
else:
    st.info("Chiếc bàn vẫn đang trống, hãy chọn cho mình một hương vị yêu thích nhé!")
