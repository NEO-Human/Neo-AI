import streamlit as st
import time

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Vatshunya - Official Store", page_icon="🌿", layout="centered")

# --- 2. SESSION STATE (Management) ---
if "is_dev" not in st.session_state: st.session_state.is_dev = False
if "reviews" not in st.session_state:
    st.session_state.reviews = [
        {"name": "Rahul S.", "stars": 5, "comment": "Best pain relief gel!", "media": None},
        {"name": "Anjali K.", "stars": 4, "comment": "Kaafi asardar hai, delivery fast thi.", "media": None}
    ]

# --- 3. UI STYLING ---
st.markdown("""
    <style>
    .block-container { max-width: 450px; background: #fff; padding-top: 1rem; }
    .stApp { background-color: #f4f7f6; }
    .dev-badge { background: #ff4b4b; color: white; padding: 5px 10px; border-radius: 5px; font-size: 10px; font-weight: bold; }
    .review-card { background: #f9f9f9; padding: 15px; border-radius: 12px; border: 1px solid #eee; margin-bottom: 10px; }
    .star-gold { color: #FFD700; font-size: 18px; }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR: DEVELOPER ACCESS ---
with st.sidebar:
    st.title("Settings ⚙️")
    if not st.session_state.is_dev:
        dev_pass = st.text_input("Enter Developer Password", type="password")
        if st.button("Unlock Developer Mode"):
            if dev_pass == "NEO_DEV_2026": # Aapka strong password
                st.session_state.is_dev = True
                st.rerun()
            else: st.error("Wrong Password!")
    else:
        st.markdown('<span class="dev-badge">DEVELOPER MODE ACTIVE</span>', unsafe_allow_html=True)
        if st.button("Logout Dev Mode"):
            st.session_state.is_dev = False
            st.rerun()

# --- 5. DEVELOPER DASHBOARD (Only visible when logged in) ---
if st.session_state.is_dev:
    st.header("🛠️ Admin Dashboard")
    with st.expander("➕ Add New Product"):
        new_name = st.text_input("Product Name")
        new_price = st.number_input("Price", min_value=0)
        new_img = st.text_input("Image URL (Dropbox)")
        if st.button("Publish Product"):
            st.success(f"Product '{new_name}' Live ho gaya!")
    
    with st.expander("📝 Edit Dev Details"):
        st.text_input("Developer Name", value="Neo Developer")
        st.text_input("Contact Email", value="dev@neo.com")
    st.divider()

# --- 6. MAIN STORE UI ---
st.markdown("<h2 style='text-align: center; color: #1b5e20;'>🌿 Vatshunya Care</h2>", unsafe_allow_html=True)

# Main Product Photo
photo_url = "https://www.dropbox.com/scl/fi/p6yfa547mvi76he78rypp/20260423_054138.jpg?rlkey=p4g9z5qox1lt77kxwo6s90s4a&st=fagfav9i&dl=1"
st.image(photo_url, use_container_width=True)

st.markdown("<h3 style='text-align:center;'>Price: ₹150</h3>", unsafe_allow_html=True)

# Order Form
with st.expander("📦 Order & Payment Details", expanded=True):
    name = st.text_input("Your Name")
    phone = st.text_input("WhatsApp No")
    addr = st.text_area("Full Address")
    pay_app = st.selectbox("Select Payment App", ["PhonePe", "GPay", "Paytm"])
    
    if st.button(f"Pay ₹150 via {pay_app}"):
        if name and phone and addr:
            upi_url = f"upi://pay?pa=9665145228-2@axl&pn=Vatshunya&am=150&cu=INR&tn=Order_{phone}"
            st.markdown(f'<a href="{upi_url}" target="_blank"><button style="width:100%; padding:10px; background:#2e7d32; color:white; border:none; border-radius:10px;">PROCEED TO PAYMENT</button></a>', unsafe_allow_html=True)
        else: st.warning("Details bharein!")

st.divider()

# --- 7. BUYER RATINGS & REVIEWS ---
st.header("⭐ Customer Reviews")

# Review Submission Form
with st.expander("✍️ Write a Review"):
    rev_name = st.text_input("Your Name", key="rev_n")
    rev_stars = st.slider("Rating", 1, 5, 5)
    rev_text = st.text_area("Share your experience")
    rev_media = st.text_input("Photo/Video Link (Dropbox/Drive)")
    
    if st.button("Submit Review"):
        if rev_name and rev_text:
            new_rev = {"name": rev_name, "stars": rev_stars, "comment": rev_text, "media": rev_media}
            st.session_state.reviews.insert(0, new_rev)
            st.success("Review submitted!")
            st.rerun()

# Display Reviews
for r in st.session_state.reviews:
    st.markdown(f"""
    <div class="review-card">
        <strong>{r['name']}</strong> <span class="star-gold">{'★' * r['stars']}</span>
        <p style="font-size: 14px; color: #555; margin-top:5px;">{r['comment']}</p>
    </div>
    """, unsafe_allow_html=True)
    if r['media']:
        if ".mp4" in r['media'] or "youtube" in r['media']:
            st.video(r['media'])
        else:
            st.image(r['media'], width=150)

# --- FOOTER ---
st.caption("© 2026 Vatshunya Official - Secure & Trusted")
