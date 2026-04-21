import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(page_title="Neo AI", page_icon="🤖", layout="wide")

# --- GPT Style Dark Theme CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #343541; color: #ECECF1; }
    section[data-testid="stSidebar"] { background-color: #202123 !important; border-right: 1px solid #4d4d4f; }
    .stChatMessage { border-radius: 12px; padding: 15px; margin-bottom: 10px; }
    .stTextInput>div>div>input { background-color: #40414f; color: white; border: 1px solid #565869; border-radius: 5px; }
    .stButton>button { border-radius: 5px; background-color: #10a37f; color: white; border: none; transition: 0.3s; }
    .stButton>button:hover { background-color: #1a7f64; }
    </style>
    """, unsafe_allow_html=True)

# --- Initializing State for Chat & Categories ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "cat_business" not in st.session_state: st.session_state.cat_business = []
if "cat_trends" not in st.session_state: st.session_state.cat_trends = []
if "cat_growth" not in st.session_state: st.session_state.cat_growth = []

# --- SIDEBAR: Organized Memories ---
with st.sidebar:
    st.title("➕ New Chat")
    st.markdown("---")
    
    st.subheader("📁 Smart Categories")
    
    # Category Folders using Expanders
    with st.expander("💼 Business & Startup"):
        if st.session_state.cat_business:
            for item in st.session_state.cat_business: st.caption(f"• {item}")
        else: st.caption("No history yet.")

    with st.expander("🔥 Viral Trends"):
        if st.session_state.cat_trends:
            for item in st.session_state.cat_trends: st.caption(f"• {item}")
        else: st.caption("No history yet.")

    with st.expander("🧠 Growth & Personal"):
        if st.session_state.cat_growth:
            for item in st.session_state.cat_growth: st.caption(f"• {item}")
        else: st.caption("No history yet.")

    st.markdown("---")
    user_name = st.text_input("User Name", placeholder="Type your name...")
    master_key = st.text_input("Master Key", type="password", placeholder="Enter Secret Key")
    
    st.markdown("---")
    st.write("💎 **Neo Pro**")
    st.write("Support Neo's Learning via UPI:")
    st.code("9665145228-2@axl", language="text") # Apna UPI yahan badlein
    st.progress(5)
    st.caption("Neo Growth: 5% (Infant)")

# --- MAIN CHAT AREA ---
if not user_name:
    st.title("Neo AI")
    st.write("Welcome! Please identify yourself in the sidebar to start a secure conversation.")
    
    # Professional Preview Grid
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Analyze Trends**\n\nNeo scans YouTube/Insta for you.")
    with col2:
        st.info("**Startup Blueprint**\n\nConvert ideas into business.")
else:
    st.subheader(f"Neo v1.0 Chat - {user_name}")
    
    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    if prompt := st.chat_input("Ask Neo about your next move..."):
        # Add User Message to UI
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # --- Simple Auto-Categorization Logic ---
        p_lower = prompt.lower()
        if any(word in p_lower for word in ["paisa", "business", "startup", "money", "sell"]):
            st.session_state.cat_business.append(prompt[:20] + "...")
        elif any(word in p_lower for word in ["trend", "viral", "insta", "youtube", "reels"]):
            st.session_state.cat_trends.append(prompt[:20] + "...")
        else:
            st.session_state.cat_growth.append(prompt[:20] + "...")

        # Neo's Response Logic
        with st.chat_message("assistant"):
            if master_key == "NEO_MASTER_2026": # Secret Creator Key
                response = f"Master {user_name}, I've analyzed your input and categorized it for our records. How should we proceed?"
            else:
                response = f"Thanks for sharing, {user_name}. I'm saving this in my growth logs to serve you better."
            
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
