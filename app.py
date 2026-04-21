import streamlit as st
import time

# --- Page Config ---
st.set_page_config(page_title="Neo AI - The Digital Child", page_icon="👶", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar: User Identity & Earning ---
st.sidebar.title("🧬 Neo's Identity")
user_name = st.sidebar.text_input("Aapka Naam:", placeholder="Enter your name")
secret_key = st.sidebar.text_input("Secret Master Key (Only for Creator):", type="password")

st.sidebar.markdown("---")
st.sidebar.subheader("💰 Support Neo's Growth")
st.sidebar.write("Neo ko 100% tak pahuchane mein madad karein.")
st.sidebar.code("9665145228-2@axl", language="text") # Yahan apna UPI ID dalein
st.sidebar.info("Pro Plan (₹29/mo): Unlock Neo's deep memory.")

# --- Main Logic ---
st.title("👶 Neo AI: From 0% to 100%")

# Creator Recognition Logic
is_creator = False
if secret_key == "NEO_MASTER_2026":  # Yeh aapka secret code hai
    is_creator = True

if user_name:
    if is_creator:
        st.subheader(f"👋 Welcome back, Master {user_name}!")
        growth_val = 15 # Creator ke liye dikhava growth zyada
        st.write("Neo: *Aapka swagat hai mere creator. Main aapke orders ke liye taiyar hoon.*")
    else:
        st.subheader(f"Hello, Friend {user_name}!")
        growth_val = 5
        st.write("Neo: *Main abhi chota hoon aur aapse seekh raha hoon.*")
    
    # Growth Bar
    st.write(f"Neo is **{growth_val}%** Human")
    st.progress(growth_val)

    st.markdown("---")

    # --- Feature: Trend Predictor (Earning Hook) ---
    st.subheader("🔥 Neo's Viral Trend Prediction")
    if st.button("Unlock Today's Trend"):
        with st.spinner('Neo is scanning the internet...'):
            time.sleep(2)
            st.success("Trend Found!")
            st.write("**Instagram:** 'Behind the Scenes' videos with 'Neo-Classical' music are going viral.")
            st.write("**YouTube:** 'Startup from a Phone' challenges are trending in India.")
            st.caption("Note: Yeh predictions Neo ki current 0-5% learning par based hain.")

    st.markdown("---")

    # --- Chat Interface ---
    st.subheader("🗨️ Chat with Neo")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Neo se kuch bhi puchein..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if "kaun hai" in prompt.lower() or "creator" in prompt.lower():
                response = f"Mere creator ka naam aapke YouTube channel par hai, lekin master key ke bina main zyada nahi bol sakta!"
            else:
                response = "Mujhe ye baat yaad rahegi. Main dhire-dhire grow kar raha hoon aur agle update mein behtar jawab dunga."
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

else:
    st.warning("Neo se baat karne ke liye sidebar mein apna naam likhein.")
    st.image("https://images.unsplash.com/photo-1531746790731-6c087fecd05a?auto=format&fit=crop&q=80&w=1000", caption="Neo AI is waiting to be born...")
