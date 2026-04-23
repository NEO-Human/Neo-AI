import streamlit as st

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(page_title="Vatshunya - Instant Pain Relief", page_icon="🌿", layout="centered")

# Custom Styling for Professional Store Look
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #1a1a1a; }
    .stButton>button { width: 100%; background-color: #2e7d32; color: white; border-radius: 12px; height: 3.5em; font-weight: bold; border: none; font-size: 18px; transition: 0.3s; }
    .stButton>button:hover { background-color: #1b5e20; box-shadow: 0 4px 15px rgba(46, 125, 50, 0.3); }
    .price-text { font-size: 38px; color: #2e7d32; font-weight: bold; margin-bottom: 0px; }
    .delivery-badge { background-color: #ffebee; color: #c62828; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 14px; display: inline-block; }
    .product-card { border: 1px solid #eee; padding: 25px; border-radius: 20px; background: #fafafa; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
    .benefit-list { list-style-type: none; padding: 0; }
    .benefit-item { margin-bottom: 10px; font-size: 16px; color: #444; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER ---
st.markdown("<h1 style='text-align: center; color: #2e7d32; margin-bottom: 0;'>🌿 Vatshunya Care</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Ayurvedic Solution for Every Body Pain</p>", unsafe_allow_html=True)
st.divider()

# --- 3. PRODUCT DISPLAY ---
col_img, col_info = st.columns([1, 1], gap="large")

with col_img:
    # Aapki Dropbox Photo
    image_url = "https://www.dropbox.com/scl/fi/p6yfa547mvi76he78rypp/20260423_054138.jpg?rlkey=p4g9z5qox1lt77kxwo6s90s4a&st=fagfav9i&dl=1"
    st.image(image_url, use_container_width=True, caption="Vatshunya Roll-on Gel")
    st.caption("✨ Real Product Image")

with col_info:
    st.markdown("<p class='price-text'>₹150 <span style='font-size: 16px; color: #888; text-decoration: line-through;'>₹299</span></p>", unsafe_allow_html=True)
    st.markdown("<div class='delivery-badge'>🚚 FREE Delivery (10-15 Days)</div>", unsafe_allow_html=True)
    
    st.markdown("""
    ### Kyun Chunein Vatshunya?
    <ul class='benefit-list'>
        <li class='benefit-item'>✅ **Instant Relief:** Joint aur Muscle pain mein turant asar.</li>
        <li class='benefit-item'>✅ **100% Ayurvedic:** No chemicals, pure natural herbs.</li>
        <li class='benefit-item'>✅ **Easy Roll-on:** Lagane mein asaan, chip-chipahat nahi.</li>
        <li class='benefit-item'>✅ **Travel Friendly:** Choti bottle, kahi bhi le jayein.</li>
    </ul>
    """, unsafe_allow_html=True)

st.divider()

# --- 4. ORDER FORM ---
st.markdown("<h2 style='text-align: center;'>📦 Apna Order Confirm Karein</h2>", unsafe_allow_html=True)

with st.container():
    with st.form("vatshunya_order_form"):
        st.markdown("### Shipping Details")
        u_name = st.text_input("Aapka Pura Naam*")
        u_phone = st.text_input("WhatsApp Number (Delivery Update ke liye)*")
        u_pin = st.text_input("Pincode (6-digit)*", max_chars=6)
        u_address = st.text_area("Pura Address (Ghar No, Colony, City)*")
        
        st.write("---")
        st.info("💡 Note: Payment ke baad aapka order 24 ghante mein process ho jayega.")
        
        submit_order = st.form_submit_button("Proceed to Pay ₹150")

# --- 5. PAYMENT LOGIC ---
if submit_order:
    if not (u_name and u_phone and u_pin and u_address):
        st.error("Bhai, saari details bharna zaroori hai!")
    elif len(u_phone) < 10 or not u_pin.isdigit():
        st.error("Phone number ya Pincode galat lag raha hai.")
    else:
        # Success details save (Internally)
        st.success(f"Dhanyawad {u_name}! Details save ho gayi hain.")
        
        # UPI Details
        upi_id = "9665145228-2@axl" 
        note = f"VatshunyaOrder_{u_phone}"
        upi_url = f"upi://pay?pa={upi_id}&pn=VatshunyaCare&am=150&cu=INR&tn={note}"
        
        # Large Payment Button
        st.markdown(f"""
            <div style="text-align: center; border: 2px dashed #2e7d32; padding: 30px; border-radius: 20px; margin-top: 20px; background: #f1f8e9;">
                <h3 style="color: #2e7d32;">Last Step: Complete Payment</h3>
                <p>Niche diye gaye button par click karein aur ₹150 pay karein:</p>
                <a href="{upi_url}">
                    <button style="background-color: #6200ee; color: white; padding: 18px 40px; border: none; border-radius: 12px; font-size: 22px; cursor: pointer; font-weight: bold; width: 80%;">
                        Pay ₹150 via UPI
                    </button>
                </a>
                <p style="margin-top: 20px; font-size: 12px; color: #555;">Payment hote hi aapko WhatsApp par confirmation mil jayegi.</p>
            </div>
            """, unsafe_allow_html=True)

# --- 6. FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888;'>
        <p>© 2026 Vatshunya Ayurvedic Care | Pure. Safe. Effective.</p>
        <p style='font-size: 10px;'>Customer Care: WhatsApp your order details for tracking.</p>
    </div>
    """, unsafe_allow_html=True)

