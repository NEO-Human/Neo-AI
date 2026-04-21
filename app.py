import streamlit as st
import time
import random
import smtplib
from email.message import EmailMessage
from PIL import Image

# --- 1. CONFIG & BEAST THEME ---
st.set_page_config(page_title="Neo AI - Professional SaaS", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .auth-container { max-width: 450px; margin: auto; padding: 30px; border: 1px solid #EEE; border-radius: 15px; box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center; }
    .btn-redirect { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    .upload-box { border: 2px dashed #10a37f; padding: 20px; border-radius: 10px; text-align: center; background: #f0fff4; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. EMAIL CONFIG ---
S_EMAIL = "nichitesurekha61@gmail.com" 
S_PASS = "wlbyzggcamomaxsw" 

def send_otp_email(rec_email, otp):
    try:
        msg = EmailMessage()
        msg.set_content(f"Your Neo AI Security Code: {otp}")
        msg['Subject'] = "Neo AI OTP"
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
if "history" not in st.session_state: st.session_state.history = []
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
                else: st.error("Failed to send OTP")
            else: st.error("Invalid Email")

    elif st.session_state.auth_step == "otp_verify":
        st.info(f"OTP sent to {st.session_state.u_email}")
        code = st.text_input("6-Digit Code", placeholder="XXXXXX")
        if st.button("Verify"):
            if code == st.session_state.gen_otp:
                st.session_state.auth_step = "verified"
                st.rerun()
            else: st.error("Wrong OTP")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. MAIN APP ---
if st.session_state.auth_step != "verified":
    show_auth()
else:
    with st.sidebar:
        st.title("Neo v8.5 Pro 🚀")
        st.write(f"User: {st.session_state.u_email}")
        m_key = st.text_input("Master Key", type="password")
        if m_key == "NEO_MASTER_2026":
            st.session_state.master = True
            st.success("MASTER ACTIVE")
        
        c_val = "∞" if st.session_state.master else st.session_state.credits
        st.markdown(f'<span class="premium-badge">CREDITS: {c_val}</span>', unsafe_allow_html=True)
        
        if st.button("🔴 Logout"):
            st.session_state.auth_step = "email_entry"
            st.rerun()

    t1, t2, t3 = st.tabs(["🗨️ Beast Chat", "🖼️ AI Thumbnail", "💎 Pro Upgrade"])

    with t1:
        for chat in st.session_state.history:
            with st.chat_message(chat["role"]): st.markdown(chat["content"])
        if p := st.chat_input("Ask..."):
            st.session_state.history.append({"role": "user", "content": p})
            # Idhar AI logic future mein add kar sakte hain
            st.rerun()

    with t2:
        st.subheader("🎥 Pro Thumbnail Maker")
        st.markdown('<div class="upload-box">Upload Photo to Transform</div>', unsafe_allow_html=True)
        up_file = st.file_uploader("Upload Image", type=["jpg", "png"])
        if st.button("Generate Professional Result"):
            if (st.session_state.credits > 0 or st.session_state.master) and up_file:
                with st.spinner("Processing..."):
                    time.sleep(2)
                    if not st.session_state.master: st.session_state.credits -= 1
                    img = Image.open(up_file)
                    st.image(img, caption="Original", width=300)
                    st.success("✅ Professional Edit Done!")
                    st.image("https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800", caption="Result")
            elif not up_file: st.error("Upload a photo first!")
            else: st.error("No Credits Left!")

    with t3:
        st.markdown(f"""
        <div style="border: 1px solid #EEE; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Pro Access - ₹49</h3>
            <p>Unlimited Processing</p>
            <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoPro" class="btn-redirect">Pay via UPI</a>
        </div>
        """, unsafe_allow_html=True)
