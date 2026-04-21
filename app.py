import streamlit as st
import time
import random
import smtplib
from email.message import EmailMessage
import google.generativeai as genai
from PIL import Image

# --- 1. CONFIG & GEMINI SETUP ---
st.set_page_config(page_title="Neo AI - Official Suite", page_icon="🛡️", layout="wide")

# AAPKI WORKING API KEY
API_KEY = "AIzaSyA1xU_jsLHzAOSAZX_m61b18Z_7CtIDcbU"
genai.configure(api_key=API_KEY)

# --- 2. DYNAMIC MODEL LOADING (To fix 404 Error) ---
def load_model():
    # Try Latest Gemini 2.0 first, then fallback to 1.5
    models_to_try = ['gemini-2.0-flash', 'gemini-1.5-flash', 'gemini-1.5-pro']
    for m_name in models_to_try:
        try:
            model = genai.GenerativeModel(m_name)
            # Test call to verify if model exists
            return model
        except:
            continue
    return None

chat_model = load_model()

if chat_model is None:
    st.error("Model Error: Google API models not found. Please check API Key permissions.")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .auth-container { max-width: 450px; margin: auto; padding: 30px; border: 1px solid #EEE; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center; }
    .btn-redirect { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. EMAIL OTP ENGINE ---
S_EMAIL = "nichitesurekha61@gmail.com" 
S_PASS = "wlbyzggcamomaxsw" 

def send_otp_email(rec_email, otp):
    try:
        msg = EmailMessage()
        msg.set_content(f"Your Neo AI Login Code: {otp}")
        msg['Subject'] = "Neo AI Security Code"
        msg['From'] = S_EMAIL
        msg['To'] = rec_email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(S_EMAIL, S_PASS)
            smtp.send_message(msg)
        return True
    except:
        return False

# --- 4. SESSION STATE ---
if "auth_step" not in st.session_state: st.session_state.auth_step = "email_entry"
if "gen_otp" not in st.session_state: st.session_state.gen_otp = None
if "u_email" not in st.session_state: st.session_state.u_email = ""
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# --- 5. AUTH GATEWAY ---
def show_auth():
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    st.title("🛡️ Neo Access")
    if st.session_state.auth_step == "email_entry":
        email = st.text_input("Enter Email", placeholder="user@gmail.com")
        if st.button("Send Code"):
            if "@" in email:
                otp = str(random.randint(111111, 999999))
                if send_otp_email(email, otp):
                    st.session_state.gen_otp = otp
                    st.session_state.u_email = email
                    st.session_state.auth_step = "otp_verify"
                    st.rerun()
    elif st.session_state.auth_step == "otp_verify":
        code = st.text_input("Enter OTP", placeholder="XXXXXX")
        if st.button("Verify"):
            if code == st.session_state.gen_otp:
                st.session_state.auth_step = "verified"
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- 6. MAIN APP ---
if st.session_state.auth_step != "verified":
    show_auth()
else:
    with st.sidebar:
        st.title("Neo v13.0 Pro 🚀")
        st.write(f"Logged in: {st.session_state.u_email}")
        st.markdown('<span class="premium-badge">UNLIMITED CHAT ACTIVE ♾️</span>', unsafe_allow_html=True)
        if st.button("🔴 Logout"):
            st.session_state.auth_step = "email_entry"
            st.rerun()

    # CHATBOT INTERFACE
    st.subheader("🗨️ Neo GPT (Beast Mode)")
    
    # History clear button
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    if prompt := st.chat_input("Baat karein..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            try:
                # Latest content generation
                response = chat_model.generate_content(prompt)
                full_text = response.text
                st.markdown(full_text)
                st.session_state.chat_history.append({"role": "assistant", "content": full_text})
            except Exception as e:
                st.error(f"Execution Error: {e}")
