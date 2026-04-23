import streamlit as st

# --- 1. PAGE SETUP (Mobile Layout) ---
st.set_page_config(page_title="Vatshunya Official", page_icon="🌿", layout="centered")

# --- 2. SESSION STATE (Crash-Proof Logic) ---
if "is_dev" not in st.session_state: 
    st.session_state.is_dev = False

# Default Reviews Setup (Safe for data)
if "reviews" not in st.session_state:
    st.session_state.reviews = [
        {"name": "Rahul S.", "stars": 5, "comment": "Best pain relief gel!", "file": None, "type": None}
    ]

# Default Product Data
if "prod_name" not in st.session_state: st.session_state.prod_name = "Vatshunya Care"
if "prod_price" not in st.session_state: st.session_state.prod_price = "150"
if "prod_img" not in st.session_state: st.session_state.prod_img = "https://www.dropbox.com/scl/fi/p6yfa547mvi76he78rypp/20260423_054138.jpg?rlkey=p4g9z5qox1lt77kxwo6s90s4a&st=fagfav9i&dl=1"

# --- 3. UI STYLING (Modern App Look) ---
st.markdown("""
    <style>
    .block-container { max-width: 450px; background: #fff; padding-top: 1rem; }
    .stApp { background-color: #f8f9fa; }
    .review-card { background: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #eee; margin-bottom: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .star-gold { color: #FFD700; font-size: 16px; }
    .stButton>button { width: 100%; border-radius: 25px; font-weight: bold; height: 3.2em; background: #1b5e20; color: white; border: none; }
    .pay-btn { background: #2e7d32; color: white; text-align: center; padding: 15px; border-radius: 10px; font-weight: bold; text-decoration: none; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: ADMIN PANEL ---
with st.sidebar:
    st.title("Admin Panel ⚙️")
    if not st.session_state.is_dev:
        dev_pass = st.text_input("Admin Password", type="password")
        if st.button("Login"):
            if dev_pass == "NEO_DEV_2026": 
                st.session_state.is_dev = True
                st.rerun()
            else: st.error("Wrong Password!")
    else:
        st.success("✅ Admin Access On")
        st.subheader("📝 Edit Store Details")
        st.session_state.prod_name = st.text_input("Product Name", st.session_state.prod_name)
        st.session_state.prod_price = st.text_input("Price (₹)", st.session_state.prod_price)
        st.session_state.prod_img = st.text_input("Image URL", st.session_state.prod_img)
        
        if st.button("Logout Admin"):
            st.session_state.is_dev = False
            st.rerun()

# --- 5. MAIN STORE UI ---
st.markdown(f"<h2 style='text-align: center; color: #1b5e20;'>🌿 {st.session_state.prod_name}</h2>", unsafe_allow_html=True)

# Main Image
st.image(st.session_state.prod_img, use_container_width=True)

st.markdown(f"<h3 style='text-align:center; margin:0;'>Price: ₹{st.session_state.prod_price}</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:red; font-size:12px; font-weight:bold;'>🚚 FREE Delivery in 10-15 Days</p>", unsafe_allow_html=True)

# --- 6. ORDER & DIRECT PAYMENT ---
with st.expander("🛒 Order Details & Payment", expanded=True):
    u_name = st.text_input("Full Name")
    u_phone = st.text_input("WhatsApp No")
    u_addr = st.text_area("Delivery Address")
    pay_app = st.radio("Choose Payment App:", ["PhonePe", "Google Pay", "Paytm"])
    
    if st.button("Confirm & Pay Now"):
        if u_name and u_phone and u_addr:
            # Direct UPI Deep Link
            upi_id = "9665145228-2@axl"
            note = f"Order_{u_phone}"
            upi_url = f"upi://pay?pa={upi_id}&pn=VatshunyaCare&am={st.session_state.prod_price}&cu=INR&tn={note}"
            
            st.success("Details Saved! Click the button below to complete payment.")
            st.markdown(f'<a href="{upi_url}" class="pay-btn">PAY ₹{st.session_state.prod_price} via {pay_app}</a>', unsafe_allow_html=True)
        else:
            st.error("Bhai, saari details bharna zaroori hai!")

st.divider()

# --- 7. BUYER REVIEWS (With Gallery Access) ---
st.header("⭐ Customer Feedback")

with st.expander("✍️ Rate & Upload Photo/Video"):
    r_name = st.text_input("Your Name", key="r_name")
    r_stars = st.slider("Rating", 1, 5, 5)
    r_comment = st.text_area("Your Review")
    
    # Direct Gallery Access
    up_file = st.file_uploader("Upload Image/Video from Gallery", type=['jpg', 'png', 'mp4', 'mov'])
    
    if st.button("Submit Review"):
        if r_name and r_comment:
            f_type = None
            if up_file:
                f_type = "video" if up_file.name.lower().endswith(('mp4', 'mov')) else "image"
            
            # Key safety ensured
            st.session_state.reviews.insert(0, {
                "name": r_name, 
                "stars": r_stars, 
                "comment": r_comment, 
                "file": up_file,
                "type": f_type
            })
            st.success("Review Added!")
            st.rerun()

# --- 8. DISPLAY REVIEWS (Smooth & Crash-Free) ---
for r in st.session_state.reviews:
    st.markdown(f"""
    <div class="review-card">
        <strong>{r.get('name', 'Buyer')}</strong> <span class="star-gold">{'★' * r.get('stars', 5)}</span>
        <p style="font-size: 14px; margin-top:5px; color: #444;">{r.get('comment', '')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Safe media loading
    if r.get('file'):
        try:
            if r.get('type') == "image":
                st.image(r['file'], width=250)
            elif r.get('type') == "video":
                st.video(r['file'])
        except:
            st.info("Loading media...")

st.caption("© 2026 Vatshunya Store | Trusted by 5000+ Customers")
