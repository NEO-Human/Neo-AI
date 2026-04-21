import streamlit as st
import time
import random
import smtplib
from email.message import EmailMessage
import google.generativeai as genai
from PIL import Image
import io

# --- 1. CONFIG & GEMINI SETUP ---
st.set_page_config(page_title="Neo AI - Professional Suite", page_icon="🚀", layout="wide")

# AAPKI WORKING API KEY
API_KEY = "AIzaSyA1xU_jsLHzAOSAZX_m61b18Z_7CtIDcbU"
genai.configure(api_key=API_KEY)

# Models Initializing - FIXED NAMES
try:
    # 'gemini-1.5-flash' sabse stable naam hai 404 error se bachne ke liye
    chat_model = genai.GenerativeModel('gemini-1.5-flash')
    # Image ke liye 'gemini-1.5-flash' ya direct 'imagen' model use hota hai
    # Filhal chat ko check karne ke liye dono ko isi par set kar dete hain
    img_model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Model Configuration Error: {e}")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .auth-container { max-width: 450px; margin: auto; padding: 30px; border: 1px solid #EEE; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center; }
    .btn-redirect { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    .design-box { border: 2px dashed #10a37f; padding: 20px; border-radius: 10px; text-align: center; background: #f0fff4; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. EMAIL OTP ENGINE ---
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

# --- 3. SESSION STATE ---
if "auth_step" not in st.session_state: st.session_state.auth_step = "email_entry"
if "gen_otp" not in st.session_state: st.session_state.gen_otp = None
if "u_email" not in st.session_state: st.session_state.u_email = ""
if "credits" not in st.session_state: st.session_state.credits = 3
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "master" not in st.session_state: st.session_state.master = False

# --- 4. AUTHENTICATION ---
def show_auth():
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    st.title("🛡️ Neo Access")
    if st.session_state.auth_step == "email_entry":
        email = st.text_input("Enter Email", placeholder="user@gmail.com")
        if st.button("Get Security Code"):
            if "@" in email and "." in email:
                otp = str(random.randint(111111, 999999))
                if send_otp_email(email, otp):
                    st.session_state.gen_otp = otp
                    st.session_state.u_email = email
                    st.session_state.auth_step = "otp_verify"
                    st.rerun()
                else: st.error("Email delivery failed.")
            else: st.error("Please enter a valid email.")
    elif st.session_state.auth_step == "otp_verify":
        st.info(f"Code sent to {st.session_state.u_email}")
        code = st.text_input("Enter OTP", placeholder="XXXXXX")
        if st.button("Log In"):
            if code == st.session_state.gen_otp:
                st.session_state.auth_step = "verified"
                st.rerun()
            else: st.error("Incorrect code.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. MAIN APPLICATION ---
if st.session_state.auth_step != "verified":
    show_auth()
else:
    with st.sidebar:
        st.title("Neo v12.1 Stable 🚀")
        st.write(f"Account: {st.session_state.u_email}")
        m_key = st.text_input("Master Key", type="password")
        if m_key == "NEO_MASTER_2026":
            st.session_state.master = True
            st.success("MASTER ACTIVE")
        
        c_val = "∞" if st.session_state.master else st.session_state.credits
        st.markdown(f'<span class="premium-badge">IMAGE CREDITS: {c_val}</span>', unsafe_allow_html=True)
        st.markdown(f'<span class="premium-badge" style="color:#000;">CHAT: UNLIMITED ♾️</span>', unsafe_allow_html=True)
        
        if st.button("🔴 Logout"):
            st.session_state.auth_step = "email_entry"
            st.rerun()

    t1, t2, t3 = st.tabs(["🗨️ Neo Chat", "🖼️ Sketch to Realistic", "💎 Pro Upgrade"])

    # --- TAB 1: CHAT ---
    with t1:
        st.subheader("Neo GPT Chat")
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
        
        if prompt := st.chat_input("Ask Neo anything..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            with st.chat_message("assistant"):
                try:
                    # Model calling logic
                    response = chat_model.generate_content(prompt)
                    st.markdown(response.text)
                    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Chat Error: {e}")

    # --- TAB 2: SKETCH TO PHOTO ---
    with t2:
        st.subheader("🖼️ Realistic Transformation")
        st.markdown('<div class="design-box">Upload a sketch and describe the final look!</div>', unsafe_allow_html=True)
        up_img = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
        details = st.text_area("Style/Details", "Make it a 4K photorealistic cinematic image.")
        
        if st.button("Transform Sketch"):
            if (st.session_state.credits > 0 or st.session_state.master) and up_img:
                with st.spinner("🤖 AI Reimagining..."):
                    try:
                        img = Image.open(up_img)
                        # Fixed model call for image reasoning
                        res = img_model.generate_content([img, f"Transform this sketch: {details}"])
                        if res:
                            if not st.session_state.master: st.session_state.credits -= 1
                            col1, col2 = st.columns(2)
                            with col1: st.image(img, caption="Original", use_container_width=True)
                            with col2: st.image(res.text, caption="AI Analysis (Note: Image output depends on specific model capability)")
                    except Exception as e:
                        st.error(f"Image Generation Error: {e}")
            elif not up_img: st.error("Please upload a sketch image first.")
            else: st.error("No credits remaining.")

    with t3:
        st.markdown("Upgrade section here...")
