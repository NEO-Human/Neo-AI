import streamlit as st

# Page Configuration
st.set_page_config(page_title="Vatshunya Roll on Gel", page_icon="🌿")

# Custom CSS for styling
st.markdown("""
    <style>
    .price-tag { font-size: 24px; color: #2E7D32; font-weight: bold; }
    .delivery-info { color: #555; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

## Product Section
st.title("Vatshunya Roll on Gel")
col1, col2 = st.columns([1, 1])

with col1:
    # Yahan apni image file ka path dein
    st.image("vatshunya_bottle.jpg", caption="Fast Relief of all Body Pain")

with col2:
    st.markdown("### Ayurvedic Pain Relief")
    st.markdown("<p class='price-tag'>Price: ₹150</p>", unsafe_allow_html=True)
    st.write("✅ 100% Natural")
    st.write("✅ Fast Action Formula")
    st.markdown("<p class='delivery-info'>🚚 Free Home Delivery in 15 Days</p>", unsafe_allow_html=True)

st.divider()

## Order Form
st.header("Delivery Details")
with st.form("order_form"):
    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number (WhatsApp)")
    address = st.text_area("Full Delivery Address")
    pincode = st.text_input("Pincode", max_chars=6)
    
    st.info("Payment Options: UPI, PhonePe, Google Pay, Credit/Debit Card")
    
    submit = st.form_submit_button("Proceed to Payment & Buy Now")

    if submit:
        if len(phone) < 10 or len(pincode) < 6:
            st.error("Please enter valid Phone Number and Pincode.")
        elif name and address:
            # Payment Gateway Integration logic
            # ₹150 amount set karne ke liye 'amount': 15000 (paise mein)
            st.success(f"Processing Order for {name}...")
            
            # Note: Real payment ke liye Razorpay ya Instamojo ki API key lagegi
            # Yeh link user ko payment apps par redirect karega
            payment_url = "https://razorpay.me/@vatshunya" # Example link
            
            st.markdown(f"""
                <a href="{payment_url}" target="_blank">
                    <button style="background-color: #6200ee; color: white; padding: 15px 32px; border: none; border-radius: 8px; cursor: pointer; font-size: 18px;">
                        Pay ₹150 Now
                    </button>
                </a>
                """, unsafe_allow_html=True)
            st.warning("Note: Payment hone ke baad 15 din mein product aapke address par deliver ho jayega.")
        else:
            st.error("Saari details bharna anivarya hai.")

# Footer
st.markdown("---")
st.caption("Vatshunya Ayurvedic Proprietary Medicine | 100% Satisfaction Guaranteed")
