import streamlit as st
import google.generativeai as genai

# --- 1. SETTINGS & THEME ---
st.set_page_config(page_title="Neo AI - Master Access", page_icon="🧠", layout="wide")

# White Minimalist Beast Theme
st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #1A1A1B; }
    section[data-testid="stSidebar"] { background-color: #F8F9FA !important; border-right: 1px solid #E5E7EB; }
    .stChatMessage { background-color: #F3F4F6; border-radius: 12px; border: none; color: #1A1A1B; margin-bottom: 15px; }
    .stTextInput>div>div>input { border-radius: 8px; border: 1px solid #D1D5DB; }
    
    /* Button & Card Styling */
    .stButton>button { background-color: #000000; color: white; border-radius: 8px; width: 100%; border: none; height: 3em; font-weight: 600; }
    .product-card { border: 1px solid #E5E7EB; padding: 20px; border-radius: 12px; background: #FFFFFF; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 20px; }
    .price-tag { color: #10a37f; font-weight: bold; font-size: 22px; margin: 10px 0; }
    .master-unlock { color: #10a37f; font-weight: bold; border: 2px solid #10a37f; padding: 10px; border-radius: 8px; text-align: center; margin-bottom: 10px; }
    
    /* Redirect Styling */
    .btn-redirect { display: block; text-decoration: none; background-color: #000000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; font-weight: bold; margin-top: 10px; }
    .btn-whatsapp { background-color: #25D366 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR & MASTER LOGIC ---
with st.sidebar:
    st.title("Neo v2.8 🚀")
    st.caption("Master-Beast Intelligence")
    
    user_name = st.text_input("Name", placeholder="Identify yourself")
    master_key = st.text_input("Secret Master Key", type="password", placeholder="Enter Key")
    
    # Master Bypass Check
    is_master = False
    if master_key == "NEO_MASTER_2026":
        is_master = True
        st.markdown('<div class="master-unlock">🔓 MASTER ACCESS ACTIVE</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    if st.button("➕ New Chat Session"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.subheader("📁 Smart Folders")
    with st.expander("💼 Business Ideas"):
        if "cat_biz" in st.session_state:
            for item in st.session_state.cat_biz: st.caption(item)
    with st.expander("📈 7-Day Trends"):
        if "cat_trend" in st.session_state:
            for item in st.session_state.cat_trend: st.caption(item)

    st.markdown("---")
    st.write("💰 **UPI ID:** `9665145228-2@axl`")
    st.markdown(f'<a href="tel:9665145228" target="_self" class="btn-redirect">📞 Direct Call Creator</a>', unsafe_allow_html=True)

# --- 3. MAIN APP LOGIC ---
if not user_name:
    st.title("Neo AI")
    st.subheader("The World's Cleanest AI Beast.")
    st.write("Enter your name and key in the sidebar to proceed.")
    st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=1000", width=600)
else:
    # Initialize States
    if "messages" not in st.session_state: st.session_state.messages = []
    if "cat_biz" not in st.session_state: st.session_state.cat_biz = []
    if "cat_trend" not in st.session_state: st.session_state.cat_trend = []
    
    tab1, tab2, tab3 = st.tabs(["🗨️ Unlimited Chat", "🛍️ AI Tool Store", "📊 7-Day Trends"])

    # --- TAB 1: CHAT ---
    with tab1:
        st.markdown(f"### Neo Chat | User: {user_name}")
        for message in st.session_state.messages:
            with st.chat_message(message["role"]): st.markdown(message["content"])
        
        if prompt := st.chat_input("Ask Neo Anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)

            with st.chat_message("assistant"):
                p_low = prompt.lower()
                if is_master:
                    response = "Greetings, Master. Deep search enabled. Processing your request through all restricted databases..."
                elif "trend" in p_low or "7 days" in p_low:
                    response = "🔍 **Trend Insight:** To see future 7-day viral projections, please upgrade to Neo Pro in the sidebar."
                else:
                    response = "I am processing your query using live web sources. Reach out to the creator for faster API access."
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    # --- TAB 2: AI STORE ---
    with tab2:
        st.subheader("🛍️ AI Tool Store")
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown('<div class="product-card"><h3>ChatGPT Plus</h3><p class="price-tag">₹49 / Month</p></div>', unsafe_allow_html=True)
            if is_master:
                st.success("✅ Master Access: Free Link Unlocked")
            else:
                wa_chatgpt = "https://wa.me/919665145228?text=I%20want%20to%20buy%20ChatGPT%20Plus"
                st.markdown(f'<a href="{wa_chatgpt}" target="_blank" class="btn-redirect btn-whatsapp">💬 Buy via WhatsApp</a>', unsafe_allow_html=True)

        with c2:
            st.markdown('<div class="product-card"><h3>Canva Pro</h3><p class="price-tag">₹29 / Month</p></div>', unsafe_allow_html=True)
            if is_master:
                st.success("✅ Master Access: Free License Active")
            else:
                wa_canva = "https://wa.me/919665145228?text=I%20want%20to%20buy%20Canva%20Pro"
                st.markdown(f'<a href="{wa_canva}" target="_blank" class="btn-redirect btn-whatsapp">💬 Buy via WhatsApp</a>', unsafe_allow_html=True)

    # --- TAB 3: TRENDS ---
    with tab3:
        st.subheader("📊 Intelligence & Future Data")
        if is_master:
            st.info("📈 **Live Analysis for Master:**\n\n1. AI-Driven Vlogging is peaking.\n2. Viral Hook: 'Why I left my job for Neo AI'.\n3. ROI Niche: Micro-AI Consulting.")
        else:
            st.warning("🔒 7-Day Trend Analysis is locked for normal users.")
            st.markdown(f'<a href="tel:9665145228" target="_self" class="btn-redirect">📞 Call to Unlock Pro Trends</a>', unsafe_allow_html=True)
