import streamlit as st
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="Vatshunya - Instant Pain Relief", page_icon="🌿", layout="centered")

# Custom CSS for a professional look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 10px; height: 3em; font-weight: bold; }
    .price-text { font-size: 30px; color: #1b5e20; font-weight: bold; margin-bottom: 0px; }
    .delivery-tag { color: #d32f2f; font-weight: bold; font-size: 14px; }
    .product-box { border: 1px solid #ddd; padding: 15px; border-radius: 15px; background: white; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🌿 Vatshunya Ayurvedic Care")
st.subheader("Fast Relief from Joint & Muscle Pain")

# --- PRODUCT & VIDEO SECTION ---
col1, col2 = st.columns([1, 1])

with col1:
    # IMAGE OR VIDEO DEMO
    # Agar aap product ka demo video dikhana chahte hain (Google Drive Direct Link):
    # Format: https://drive.google.com/uc?export=download&id=YOUR_FILE_ID
    demo_video = "https://www.w3schools.com/html/mov_bbb.mp4" # Dummy link, apni replace karein
    st.video(demo_video)
    st.caption("📽️ Watch how it works!")

with col2:
    st.markdown("<div class='product-box'>", unsafe_allow_html=True)
    st.markdown("<p class='price-text'>Price: ₹150</p>", unsafe_allow_html=True)
    st.markdown("<p class='delivery-tag'>🚚 FREE Delivery in 15 Days</p>", unsafe_allow_html=True)
    
    st.write("""
    **Main Fayde:**
    * ✅ Joint aur Muscle Pain mein turant aaram.
    * ✅ Roll-on design (Hath gande nahi honge).
    * ✅ 100% Ayurvedic & No Side Effects.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- ORDER FORM ---
st.header("📦 Order Details")
with st.form("order_details"):
    name = st.text_input("Aapka Full Name*")
    phone = st.text_input("WhatsApp Number*", help="Order update isi number par aayenge")
    pincode = st.text_input("Area Pincode*", max_chars=6)
    address = st.text_area("Pura Address (House No, Colony, City)*")
    
    st.write("---")
    st.info("💡 Payment ke baad Screenshot WhatsApp zaroori hai.")
    
    submit_btn = st.form_submit_button("Proceed to Pay ₹150")

# --- PAYMENT REDIRECTION LOGIC ---
if submit_btn:
    if not (name and phone and pincode and address):
        st.error("Bhai, saari details bharna zaroori hai!")
    elif len(phone) < 10:
        st.error("Phone number sahi nahi hai.")
    else:
        # Success Message
        st.success(f"Dhanyawad {name}! Details save ho gayi hain.")
        
        # YOUR ACTUAL UPI ID (Change this)
        upi_id = "9665145228-2@axl" 
        note = f"VatshunyaOrder_{phone}"
        
        # UPI Deep Link
        upi_url = f"upi://pay?pa={upi_id}&pn=Vatshunya%20Care&am=150&cu=INR&tn={note}"
        
        st.markdown(f"""
            <div style="text-align: center; border: 2px dashed #2e7d32; padding: 20px; border-radius: 15px;">
                <h4>Final Step: Complete Payment</h4>
                <a href="{upi_url}">
                    <button style="background-color: #2e7d32; color: white; padding: 15px 30px; border: none; border-radius: 10px; font-size: 20px; cursor: pointer; font-weight: bold;">
                        Pay ₹150 via UPI
                    </button>
                </a>
                <p style="margin-top: 15px; font-size: 14px;">Pay karne ke baad isi number par <b>{phone}</b> tracking link mil jayega.</p>
            </div>
            """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style='text-align: center;'>
        <p>© 2026 Vatshunya | Trusted Ayurvedic Pain Relief</p>
        <p style='font-size: 10px;'>Safe & Natural Ingredients | For External Use Only</p>
    </div>
    """, unsafe_allow_html=True)
