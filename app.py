import streamlit as st
import time

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Vatshunya - Official Store", page_icon="🌿", layout="centered")

# --- 2. SESSION STATE (Data Persistence) ---
if "is_dev" not in st.session_state: st.session_state.is_dev = False
if "reviews" not in st.session_state:
    st.session_state.reviews = [
        {"name": "Rahul S.", "stars": 5, "comment": "Best pain relief gel!", "file": None, "type": None}
    ]

# --- 3. UI STYLING ---
st.markdown("""
    <style>
    .block-container { max-width: 450px; background: #fff; padding-top: 1rem; }
    .stApp { background-color: #f4f7f6; }
    .dev-badge { background: #ff4b4b; color: white; padding: 5px 10px; border-radius: 5px; font-size: 10px; font-weight: bold; }
    .review-card { background: #ffffff; padding: 15px; border-radius: 12px; border: 1px solid #ddd; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); }
    .star-gold { color: #FFD700; font-size: 18px; }
    .stButton>button { width: 100%; border-radius: 25px; font-weight: bold; height: 3em; background: #1b5e20; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: DEVELOPER PANEL ---
with st.sidebar:
    st.title("Admin Settings ⚙️")
    if not st.session_state.is_dev:
        dev_pass = st.text_input("Admin Password", type="password")
        if st.button("Login"):
            if dev_pass == "NEO_DEV_2026": 
                st.session_state.is_dev = True
                st.rerun()
            else: st.error("Wrong Password!")
    else:
        st.markdown('<span class="dev-badge">ADMIN ACCESS ACTIVE</span>', unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.is_dev = False
            st.rerun()

# --- 5. ADMIN DASHBOARD ---
if st.session_state.is_dev:
    st.header("🛠️ Product Management")
    with st.expander("➕ Add New Product"):
        p_name = st.text_input("Product Name")
        p_price = st.text_input("Price (e.g. 150)")
        p_file = st.file_uploader("Upload Product Image", type=['jpg', 'png', 'jpeg'], key="admin_up")
        if st.button("Add to Store"):
            st.success("Product Added Successfully!")
    st.divider()

# --- 6. MAIN STORE UI ---
st.markdown("<h2 style='text-align: center; color: #1b5e20;'>🌿 Vatshunya Care</h2>", unsafe_allow_html=True)

# Main Product Display
main_img = "https://www.dropbox.com/scl/fi/p6yfa547mvi76he78rypp/20260423_054138.jpg?rlkey=p4g9z5qox1lt77kxwo6s90s4a&st=fagfav9i&dl=1"
st.image(main_img, use_container_width=True)

st.markdown("<h3 style='text-align:center; margin:0;'>Price: ₹150</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:red; font-weight:bold;'>🚚 FREE Delivery in 10-15 Days</p>", unsafe_allow_html=True)

# Order Form
with st.expander("🛒 Buy Now", expanded=True):
    name = st.text_input("Full Name")
    phone = st.text_input("WhatsApp No")
    addr = st.text_area("Address")
    method = st.radio("Pay with:", ["PhonePe", "GPay", "Paytm"])
    
    if st.button("Confirm Order & Pay"):
        if name and phone and addr:
            upi_url = f"upi://pay?pa=9665145228-2@axl&pn=Vatshunya&am=150&cu=INR&tn=Order_{phone}"
            st.markdown(f'<a href="{upi_url}" style="text-decoration:none;"><div style="background:#2e7d32; color:white; text-align:center; padding:15px; border-radius:10px; font-weight:bold;">CLICK TO PAY ₹150</div></a>', unsafe_allow_html=True)
        else: st.warning("Please fill all details")

st.divider()

# --- 7. REVIEWS & GALLERY UPLOAD ---
st.header("⭐ Customer Feedback")

with st.expander("✍️ Rate & Upload Photo/Video"):
    r_name = st.text_input("Your Name")
    r_stars = st.slider("Rating", 1, 5, 5)
    r_comment = st.text_area("How was the product?")
    
    # DIRECT GALLERY ACCESS: User can pick photo/video from phone
    uploaded_file = st.file_uploader("Upload Photo/Video from Gallery", type=['jpg', 'png', 'mp4', 'mov'])
    
    if st.button("Submit Review"):
        if r_name and r_comment:
            file_type = None
            if uploaded_file:
                file_type = "video" if uploaded_file.name.endswith(('mp4', 'mov')) else "image"
            
            st.session_state.reviews.insert(0, {
                "name": r_name, 
                "stars": r_stars, 
                "comment": r_comment, 
                "file": uploaded_file,
                "type": file_type
            })
            st.success("Thank you for your review!")
            st.rerun()

# Displaying Reviews
for r in st.session_state.reviews:
    st.markdown(f"""
    <div class="review-card">
        <strong>{r['name']}</strong> <span class="star-gold">{'★' * r['stars']}</span>
        <p style="font-size: 14px; margin-top:5px;">{r['comment']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Review Media Display
    if r['file']:
        if r['type'] == "image":
            st.image(r['file'], width=250)
        elif r['type'] == "video":
            st.video(r['file'])

# --- FOOTER ---
st.markdown("<p style='text-align:center; color:gray; font-size:10px;'>Vatshunya Official Store © 2026</p>", unsafe_allow_html=True)

