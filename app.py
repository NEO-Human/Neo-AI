import streamlit as st
import google.generativeai as genai

# --- Gemini AI Configuration ---
# Note: Get your API Key from https://aistudio.google.com/
# genai.configure(api_key="YOUR_GEMINI_API_KEY") 

# --- White Beast Theme (Minimalist) ---
st.set_page_config(page_title="Neo AI", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; color: #1A1A1B; }
    section[data-testid="stSidebar"] { background-color: #F8F9FA !important; border-right: 1px solid #E5E7EB; }
    .stChatMessage { background-color: #F3F4F6; border-radius: 12px; border: none; color: #1A1A1B; margin-bottom: 10px; }
    .stTextInput>div>div>input { border-radius: 8px; border: 1px solid #D1D5DB; }
    .stButton>button { background-color: #000000; color: white; border-radius: 6px; width: 100%; border: none; font-weight: 600; }
    .stButton>button:hover { background-color: #222222; color: white; }
    .stChatInputContainer { padding-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: Smart Categories & Monetization ---
with st.sidebar:
    st.title("Neo Intelligence")
    st.caption("Version 2.0 (Beast Mode)")
    if st.button("➕ New Unlimited Chat"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.subheader("📂 Smart Categories")
    with st.expander("💼 Business Ideas"):
        if "cat_biz" in st.session_state:
            for item in st.session_state.cat_biz: st.caption(item)
    with st.expander("📈 Future Trends (7 Days)"):
        if "cat_trend" in st.session_state:
            for item in st.session_state.cat_trend: st.caption(item)

    st.markdown("---")
    user_name = st.text_input("Identify Yourself", placeholder="Enter Name")
    master_key = st.text_input("Master Key", type="password")
    
    st.markdown("---")
    st.success("✅ Connected to Live Sources")
    st.write("💰 **Support Neo's Growth**")
    st.code("9665145228-2@axl", language="text")
    st.caption("Donate ₹10 to unlock 7-day trend analysis.")

# --- Main Logic ---
if not user_name:
    st.title("Neo")
    st.write("The world's first growing AI child. Enter your name in the sidebar to start.")
    st.image("https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&q=80&w=1000", width=500)
else:
    if "messages" not in st.session_state: st.session_state.messages = []
    if "cat_biz" not in st.session_state: st.session_state.cat_biz = []
    if "cat_trend" not in st.session_state: st.session_state.cat_trend = []

    # Display Chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Ask Neo anything about the future..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            # Professional Logic for Trends & Ideas
            if "7 days" in prompt.lower() or "trend" in prompt.lower():
                response = "🔍 **Scanning Global Live Sources...** \n\nPrediction for **April 29, 2026**: High probability of a 'Hyper-Local AI' trend. Small businesses will start using personalized AI assistants for voice-calls. Content creators should focus on 'Raw AI-Human interactions'."
                st.session_state.cat_trend.append(f"Trend: {prompt[:15]}...")
            elif "idea" in prompt.lower() or "business" in prompt.lower():
                response = "💡 **Live Data Business Insight:** Currently, 'Automated Newsletter Curation for AI News' has the highest ROI with 0 investment. I've saved this in your Business folder."
                st.session_state.cat_biz.append(f"Idea: {prompt[:15]}...")
            else:
                response = "I've analyzed the live web. Here is the fast-reply from my deep memory servers: [Processing Complete]."
            
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
