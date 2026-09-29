import streamlit as st
import pandas as pd

# 1. CẤU HÌNH TRANG
st.set_page_config(page_title="Pizza & Relax - Mercure Vibe", layout="centered", initial_sidebar_state="collapsed")

# 2. GIAO DIỆN & VIBE (Sử dụng CSS tối ưu, hạn chế xung đột Dark/Light mode)
st.markdown("""
<style>
    /* Bỏ ép màu nền cứng để tôn trọng Light/Dark mode của thiết bị */
    h1, h2, h3 {
        color: #00509E !important; /* Xanh đại dương sáng hơn để nổi trên nền tối */
        font-family: 'Georgia', serif; 
        font-weight: 400;
    }
    /* Chỉnh màu chữ bình thường */
    .stMarkdown p {
        font-size: 16px;
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
    }
</style>
""", unsafe_allow_html=True)

# 3. TIÊU ĐỀ
st.markdown("<h1 style='text-align: center;'>🍕 La Pizza de Mercure</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; font-size: 16px; font-style: italic;'>Hương vị tinh tế bên tiếng sóng vỗ rì rào...</h3>", unsafe_allow_html=True)
st.write("---")

# 4. TỪ ĐIỂN DỮ LIỆU
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

# Hiển thị danh sách món ăn - Sửa lại cách hiển thị để không bị ẩn
for pizza, price in PIZZA_MENU.items():
    st.markdown(f"**{pizza}** - *{price:,} VNĐ*") # Dùng st.markdown thay vì st.write trong cột
    qty = st.number_input(f"Số lượng {pizza}", min_value=0, max_value=20, value=0, key=pizza, label_visibility="collapsed")
    if qty > 0:
        order[pizza] = qty
    st.write("") # Tạo khoảng trống mỏng giữa các món

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
    
    df_bill = pd.DataFrame(bill_data)
    st.table(df_bill)
    
    st.metric(label="Tổng Chi Phí", value=f"{total_price:,} VNĐ")
    
    if st.button("Xác nhận & Chờ phục vụ"):
        st.success("Cảm ơn bạn! Bếp đang chuẩn bị món ăn với tất cả sự nâng niu. Hãy nhâm nhi chút đồ uống và tận hưởng không gian nhé.")
else:
    st.info("Chiếc bàn vẫn đang trống, hãy chọn cho mình một hương vị yêu thích nhé!")
