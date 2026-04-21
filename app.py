import streamlit as st
import time
import random
import smtplib
from email.message import EmailMessage
import google.generativeai as genai
from PIL import Image
import io

# --- 1. CONFIG & GEMINI SETUP ---
st.set_page_config(page_title="Neo AI - Professional Suite", page_icon="🛡️", layout="wide")

# API Key Configuration
API_KEY = "AIzaSyDQQ7KRmtuJNQbTKHP4qZ6MitGeM01-Pg0AIzaSyCCSYeirnZTfl4AlwdO8HUwg9t805VOkeQ"
genai.configure(api_key=API_KEY)

# Models Initialization
# gemini-3.1-pro-preview for UNLIMITED CHAT
# gemini-2.5-flash-image (Nano Banana) for IMAGES
chat_model = genai.GenerativeModel('gemini-3.1-pro-preview')
img_model = genai.GenerativeModel('gemini-2.5-flash-image')

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .auth-container { max-width: 450px; margin: auto; padding: 30px; border: 1px solid #EEE; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center; }
    .btn-redirect { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    .design-box { border: 2px dashed #10a37f; padding: 20px; border-radius: 10px; text-align: center; background: #f0fff4; margin-bottom: 20px; }
    .stChatMessage { border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. EMAIL OTP ENGINE ---
S_EMAIL = "nichitesurekha61@gmail.com" 
S_PASS = "wlbyzggcamomaxsw" 

def send_otp_email(rec_email, otp):
    try:
        msg = EmailMessage()
        msg.set_content(f"Your Neo AI Security Code: {otp}")
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

# --- 4. AUTH GATEWAY ---
def show_auth():
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    st.title("🛡️ Neo Access")
    if st.session_state.auth_step == "email_entry":
        email = st.text_input("Enter Email", placeholder="user@gmail.com")
        if st.button("Get OTP"):
            if "@" in email:
                otp = str(random.randint(111111, 999999))
                if send_otp_email(email, otp):
                    st.session_state.gen_otp = otp
                    st.session_state.u_email = email
                    st.session_state.auth_step = "otp_verify"
                    st.rerun()
                else: st.error("Email Error.")
            else: st.error("Invalid Email.")
    elif st.session_state.auth_step == "otp_verify":
        code = st.text_input("Enter OTP", placeholder="XXXXXX")
        if st.button("Verify"):
            if code == st.session_state.gen_otp:
                st.session_state.auth_step = "verified"
                st.rerun()
            else: st.error("Wrong OTP.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. MAIN APP ---
if st.session_state.auth_step != "verified":
    show_auth()
else:
    with st.sidebar:
        st.title("Neo v11.0 Beast 🚀")
        st.write(f"Logged: {st.session_state.u_email}")
        m_key = st.text_input("Master Key", type="password")
        if m_key == "NEO_MASTER_2026":
            st.session_state.master = True
            st.success("MASTER ACTIVE")
        c_val = "∞" if st.session_state.master else st.session_state.credits
        st.markdown(f'<span class="premium-badge">IMG CREDITS: {c_val}</span>', unsafe_allow_html=True)
        st.markdown(f'<span class="premium-badge" style="border-color: #000; color: #000;">CHAT: UNLIMITED ♾️</span>', unsafe_allow_html=True)
        if st.button("🔴 Logout"):
            st.session_state.auth_step = "email_entry"
            st.rerun()

    t1, t2, t3 = st.tabs(["🗨️ Neo GPT (Unlimited)", "🖼️ Sketch to Photo", "💎 Pro Upgrade"])

    # --- TAB 1: NO LIMIT CHATBOT ---
    with t1:
        st.subheader("Neo GPT - Power of Gemini 3.1 Pro")
        
        # Clear Chat Button
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

        # Display Chat
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Chat Input
        if prompt := st.chat_input("Baat karo Beast se..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                try:
                    # Requesting Gemini 3.1 Pro for NO LIMIT Chat
                    response = chat_model.generate_content(prompt)
                    full_response = response.text
                    # Typewriter effect
                    curr_text = ""
                    for char in full_response:
                        curr_text += char
                        message_placeholder.markdown(curr_text + "▌")
                        time.sleep(0.005)
                    message_placeholder.markdown(full_response)
                    st.session_state.chat_history.append({"role": "assistant", "content": full_response})
                except Exception as e:
                    st.error(f"Chat Error: {e}")

    # --- TAB 2: SKETCH TO PHOTO ---
    with t2:
        st.subheader("🖼️ Realistic Transformation (Nano Banana 2)")
        up_sketch = st.file_uploader("Upload Sketch", type=["jpg", "png", "jpeg"])
        p_desc = st.text_area("Transformation Style", placeholder="e.g. Turn this sketch into a photorealistic 4K cinematic image.")
        
        if st.button("Generate Transformation"):
            if (st.session_state.credits > 0 or st.session_state.master) and up_sketch and p_desc:
                with st.spinner("🤖 Drawing..."):
                    try:
                        img = Image.open(up_sketch)
                        response = img_model.generate_content([img, f"Transform this sketch: {p_desc}"])
                        if response:
                            if not st.session_state.master: st.session_state.credits -= 1
                            col1, col2 = st.columns(2)
                            with col1: st.image(img, caption="Sketch", use_container_width=True)
                            with col2: st.image(response.generated_image, caption="AI Result", use_container_width=True)
                    except Exception as e:
                        st.error(f"Error: {e}")
            elif not up_sketch: st.error("Image upload karein!")
            else: st.error("No Credits Left for Images!")

    # --- TAB 3: PRO ---
    with t3:
        st.markdown(f"""
        <div style="border: 1px solid #EEE; padding: 25px; border-radius: 15px; text-align: center;">
            <h3>Neo Pro Upgrade - ₹49</h3>
            <p>Unlimited Image Generations & Early Access</p>
            <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoPro" class="btn-redirect">Pay via UPI</a>
        </div>
        """, unsafe_allow_html=True)
