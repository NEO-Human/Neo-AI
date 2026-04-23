import streamlit as st

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Vatshunya Official Store", page_icon="🌿", layout="centered")

# --- 2. SESSION STATE (Data Safety) ---
if "is_dev" not in st.session_state: st.session_state.is_dev = False
if "orders" not in st.session_state: st.session_state.orders = []
if "reviews" not in st.session_state:
    st.session_state.reviews = [
        {"name": "Rahul S.", "stars": 5, "comment": "Best pain relief gel!", "file": None, "type": None}
    ]

# Default Product Data
if "p_name" not in st.session_state: st.session_state.p_name = "Vatshunya Care Gel"
if "p_price" not in st.session_state: st.session_state.p_price = "150"
if "p_img" not in st.session_state: st.session_state.p_img = "https://www.dropbox.com/scl/fi/p6yfa547mvi76he78rypp/20260423_054138.jpg?rlkey=p4g9z5qox1lt77kxwo6s90s4a&st=fagfav9i&dl=1"

# --- 3. UI STYLING ---
st.markdown("""
    <style>
    .block-container { max-width: 450px; background: #fff; padding-top: 1rem; }
    .stApp { background-color: #f8f9fa; }
    .review-card { background: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #eee; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .stButton>button { width: 100%; border-radius: 25px; font-weight: bold; height: 3.2em; background: #1b5e20; color: white; border: none; }
    .order-box { background: #e8f5e9; padding: 15px; border-radius: 10px; border-left: 5px solid #2e7d32; margin-bottom: 10px; color: #1b5e20; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: ADMIN DASHBOARD (Order Management) ---
with st.sidebar:
    st.title("Admin Panel ⚙️")
    if not st.session_state.is_dev:
        dev_pass = st.text_input("Enter Admin Password", type="password")
        if st.button("Login"):
            if dev_pass == "NEO_DEV_2026": 
                st.session_state.is_dev = True
                st.rerun()
            else: st.error("Access Denied!")
    else:
        st.success("Admin Access: ON")
        st.subheader("📦 Order History")
        if st.session_state.orders:
            for i, o in enumerate(st.session_state.orders):
                with st.expander(f"Order #{i+1} - {o['name']}"):
                    st.write(f"**Phone:** {o['phone']}")
                    st.write(f"**Address:** {o['addr']}")
                    st.write(f"**App:** {o['pay_app']}")
        else:
            st.info("No orders yet.")
            
        if st.button("Logout Admin"):
            st.session_state.is_dev = False
            st.rerun()

# --- 5. MAIN STORE UI ---
st.markdown(f"<h2 style='text-align: center; color: #1b5e20;'>🌿 {st.session_state.p_name}</h2>", unsafe_allow_html=True)
st.image(st.session_state.p_img, use_container_width=True)

st.markdown(f"<h3 style='text-align:center; margin:0;'>Price: ₹{st.session_state.p_price}</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:red; font-size:12px; font-weight:bold;'>🚚 Free Shipping | Safe Checkout</p>", unsafe_allow_html=True)

# --- 6. BUY NOW & DATA CAPTURE ---
with st.expander("🛒 Fill Delivery Details", expanded=True):
    name = st.text_input("Full Name")
    phone = st.text_input("WhatsApp No")
    pincode = st.text_input("Pincode", max_chars=6)
    address = st.text_area("Complete Address")
    pay_app = st.selectbox("Choose Payment App", ["PhonePe", "Google Pay", "Paytm"])
    
    if st.button("Confirm Order & Pay"):
        if name and phone and pincode and address:
            # 1. Save locally for Admin Panel
            st.session_state.orders.insert(0, {"name": name, "phone": phone, "addr": f"{address}, Pin: {pincode}", "pay_app": pay_app})
            
            # 2. UPI Deep Link
            upi_id = "9665145228-2@axl"
            note = f"Order_For_{phone}"
            upi_url = f"upi://pay?pa={upi_id}&pn=VatshunyaCare&am={st.session_state.p_price}&cu=INR&tn={note}"
            
            # 3. WhatsApp Redirect (For Extra Confirmation)
            wa_num = "9665145228" # Aapka WhatsApp Number
            wa_msg = f"Naya Order Aaya Hai!%0A*Name:* {name}%0A*Phone:* {phone}%0A*Address:* {address}, {pincode}%0A*Price:* ₹{st.session_state.p_price}%0A*Status:* Payment Initiated via {pay_app}"
            wa_url = f"https://wa.me/{wa_num}?text={wa_msg}"
            
            st.success("Success! Order details captured.")
            
            st.markdown(f"""
                <div style="text-align: center; margin-top: 10px;">
                    <a href="{upi_url}" target="_blank" style="text-decoration:none;">
                        <div style="background:#2e7d32; color:white; padding:15px; border-radius:10px; font-weight:bold; margin-bottom:10px;">STEP 1: PAY ₹{st.session_state.p_price}</div>
                    </a>
                    <a href="{wa_url}" target="_blank" style="text-decoration:none;">
                        <div style="background:#25d366; color:white; padding:15px; border-radius:10px; font-weight:bold;">STEP 2: SEND ADDRESS TO WHATSAPP</div>
                    </a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Please fill all details correctly.")

st.divider()

# --- 7. REVIEWS & GALLERY ---
st.header("⭐ Customer Reviews")
with st.expander("✍️ Write a Review (Pick from Gallery)"):
    rev_n = st.text_input("Name", key="rev_n")
    rev_s = st.slider("Rating", 1, 5, 5)
    rev_c = st.text_area("Experience")
    up_f = st.file_uploader("Upload Photo/Video", type=['jpg','png','mp4','mov'])
    
    if st.button("Submit Review"):
        if rev_n and rev_c:
            f_t = "video" if up_f and up_f.name.lower().endswith(('mp4','mov')) else "image"
            st.session_state.reviews.insert(0, {"name": rev_n, "stars": rev_s, "comment": rev_c, "file": up_f, "type": f_t})
            st.success("Review Submitted!")
            st.rerun()

# Review Display Loop
for r in st.session_state.reviews:
    st.markdown(f"""
    <div class="review-card">
        <strong>{r.get('name', 'User')}</strong> <span style='color:#FFD700;'>{'★' * r.get('stars', 5)}</span>
        <p style='font-size:14px; margin-top:5px;'>{r.get('comment', '')}</p>
    </div>
    """, unsafe_allow_html=True)
    if r.get('file'):
        if r.get('type') == "image": st.image(r['file'], width=250)
        else: st.video(r['file'])

st.caption("© 2026 Vatshunya Ayurvedic Store - Secure Payments")

