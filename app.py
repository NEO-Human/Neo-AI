import streamlit as st

# --- Page Config & White Beast Theme ---
st.set_page_config(page_title="Neo AI - Store", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #1A1A1B; }
    .stChatMessage { background-color: #F3F4F6; border-radius: 10px; border: none; }
    .product-card { border: 1px solid #E5E7EB; padding: 15px; border-radius: 10px; background: #F9FAFB; margin-bottom: 10px; }
    .price-tag { color: #10a37f; font-weight: bold; font-size: 20px; }
    .stButton>button { background-color: #000000; color: white; border-radius: 6px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: User Profile & UPI ---
with st.sidebar:
    st.title("Neo v2.5")
    user_name = st.text_input("Name", placeholder="Enter your name")
    master_key = st.text_input("Master Key", type="password")
    
    st.markdown("---")
    st.subheader("💳 Subscription Status")
    if master_key == "NEO_MASTER_2026":
        st.success("Level: OWNER (Master)")
    else:
        st.warning("Level: FREE USER")
        if st.button("🚀 Upgrade to Pro (₹29)"):
            st.info("Pay to: `9665145228-2@axl` and send screenshot.")
    
    st.markdown("---")
    st.write("💰 **UPI ID:** `9665145228-2@axl`")

# --- Main App Logic ---
if not user_name:
    st.title("Neo AI")
    st.write("Welcome to the Future. Identify yourself to access the AI Store.")
else:
    # --- Store Section ---
    st.title(f"Hello, {user_name}!")
    
    tab1, tab2, tab3 = st.tabs(["🗨️ Neo Chat", "🛍️ AI Tool Store", "📊 Trends"])

    with tab1:
        st.subheader("Chat with Neo Intelligence")
        if "messages" not in st.session_state: st.session_state.messages = []
        for message in st.session_state.messages:
            with st.chat_message(message["role"]): st.markdown(message["content"])
        
        if prompt := st.chat_input("Neo se puchiye..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("assistant"):
                response = "Neo is processing your request using global databases..."
                st.markdown(response)

    with tab2:
        st.subheader("🔥 Premium AI Tools (Low Price Access)")
        st.write("Neo provides shared access to top AI tools at 90% discount.")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""<div class="product-card">
                <h3>ChatGPT Plus (Shared)</h3>
                <p>Access GPT-4, DALL-E 3, and more.</p>
                <p class="price-tag">₹49 / Month</p>
                </div>""", unsafe_allow_html=True)
            if st.button("Buy ChatGPT Access"):
                st.success("UPI ID: 9665145228-2@axl pe ₹49 pay karein.")

        with col2:
            st.markdown("""<div class="product-card">
                <h3>Canva Pro (Full)</h3>
                <p>Premium templates and AI design tools.</p>
                <p class="price-tag">₹29 / Month</p>
                </div>""", unsafe_allow_html=True)
            if st.button("Buy Canva Access"):
                st.success("UPI ID: 9665145228-2@axl pe ₹29 pay karein.")

    with tab3:
        st.subheader("📈 7-Day Future Trends")
        st.info("Locked: Buy 'Neo Pro' Subscription to see future viral data.")
        if st.button("Unlock Now"):
            st.write("Please complete the payment to `9665145228-2@axl`.")

