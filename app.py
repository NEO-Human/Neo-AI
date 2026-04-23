import streamlit as st

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Vatshunya - Instant Pain Relief", page_icon="🌿", layout="centered")

# Custom CSS for a clean, high-conversion look
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    .stButton>button { width: 100%; background-color: #1b5e20; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none; font-size: 18px; transition: 0.3s; }
    .stButton>button:hover { background-color: #2e7d32; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
    .price-text { font-size: 40px; color: #1b5e20; font-weight: bold; margin-bottom: 0px; }
    .delivery-tag { background-color: #fff4f4; color: #d32f2f; padding: 6px 12px; border-radius: 8px; font-weight: bold; font-size: 14px; display: inline-block; margin-bottom: 10px; }
    .product-container { text-align: center; padding: 20px; border-radius: 20px; background: #fafafa; border: 1px solid #f0f0f0; }
    .form-box { background: #ffffff; padding: 25px; border-radius: 15px; border: 1px solid #eee; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("<h1 style='text-align: center; color: #1b5e20;'>🌿 Vatshunya Care</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666; font-size: 18px;'>Ayurvedic Roll-on for Instant Pain Relief</p>", unsafe_allow_html=True)
st.divider()

# --- 3. PRODUCT PHOTO SECTION (No Video) ---
# Image Center Alignment
col_left, col_mid, col_right = st.columns([0.2, 1.6, 0.2])

with col_mid:
    st.markdown("<div class='product-container'>", unsafe_allow_html=True)
    # Aapka Dropbox Photo Link (dl=1 for direct view)
    photo_url = "https://www.dropbox.com/scl/fi/p6yfa547mvi76he78rypp/20260423_054138.jpg?rlkey=p4g9z5qox1lt77kxwo6s90s4a&st=fagfav9i&dl=1"
    st.image(photo_url, use_container_width=True)
    
    st.markdown("<p class='price-text'>Price: ₹150</p>", unsafe_allow_html=True)
    st.markdown("<div class='delivery-tag'>🚚 FREE Home Delivery (10-15 Days)</div>", unsafe_allow_html=True)
    
    st.write("""
    **Fayde:**
    Joint aur Muscle Pain mein turant aaram | 100% Ayurvedic | Easy Roll-on
    """)
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# --- 4. ORDER FORM ---
st.markdown("<h2 style='text-align: center;'>📦 Order Details</h2>", unsafe_allow_html=True)

_, form_col, _ = st.columns([0.1, 1, 0.1])

with form_col:
    with st.form("order_form"):
        st.markdown("### Shipping Information")
        name = st.text_input("Aapka Full Name*")
        phone = st.text_input("WhatsApp Number*", help="Order update isi par aayenge")
        pincode = st.text_input("Area Pincode*", max_chars=6)
        address = st.text_area("Pura Address (House No, Colony, City)*")
        
        st.write("---")
        st.info("💡 Note: Proceed karne ke baad UPI payment button dikhega.")
        
        submit_btn = st.form_submit_button("Proceed to Pay ₹150")

# --- 5. PAYMENT REDIRECTION LOGIC ---
if submit_btn:
    if not (name and phone and pincode and address):
        st.error("Bhai, saari details bharna zaroori hai!")
    elif len(phone) < 10:
        st.error("Mobile number galat hai.")
    else:
        st.success(f"Dhanyawad {name}! Aapka order process ho raha hai.")
        
        # UPI Details
        upi_id = "9665145228-2@axl" 
        note = f"VatshunyaOrder_{phone}"
        upi_url = f"upi://pay?pa={upi_id}&pn=VatshunyaCare&am=150&cu=INR&tn={note}"
        
        # Big Payment Button
        st.markdown(f"""
            <div style="text-align: center; margin-top: 20px; padding: 20px; border: 2px dashed #1b5e20; border-radius: 15px;">
                <h4>Last Step: Complete Payment</h4>
                <a href="{upi_url}">
                    <button style="background-color: #6200ee; color: white; padding: 18px 40px; border: none; border-radius: 10px; font-size: 22px; cursor: pointer; font-weight: bold; width: 100%;">
                        Pay ₹150 via UPI
                    </button>
                </a>
                <p style="margin-top: 15px; font-size: 13px; color: #555;">(PhonePe, GPay, Paytm support)</p>
            </div>
            """, unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888; font-size: 12px;'>
        <p>© 2026 Vatshunya Ayurvedic Care | Trusted by Thousands</p>
        <p>Pure Natural Ingredients | No Chemicals | For External Use Only</p>
    </div>
    """, unsafe_allow_html=True)
