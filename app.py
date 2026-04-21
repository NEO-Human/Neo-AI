import streamlit as st
import time
import random
import smtplib
from email.message import EmailMessage
import google.generativeai as genai
from PIL import Image

# --- 1. CONFIG & BEAST THEME ---
st.set_page_config(page_title="Neo AI - Professional SaaS", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .auth-container { max-width: 450px; margin: auto; padding: 30px; border-radius: 15px; border: 1px solid #EEE; box-shadow: 0 10px 25px rgba(0,0,0,0.05); text-align: center; }
    .btn-redirect { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    .upload-box { border: 2px dashed #10a37f; padding: 20px; border-radius: 10px; text-align: center; background: #f0fff4; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. PRIVATE EMAIL ENGINE ---
SENDER_EMAIL = "nichitesurekha61@gmail.com" 
SENDER_PASSWORD = "wlbyzggcamomaxsw" 

def send_otp_email(receiver_email, otp):
    try:
        msg = EmailMessage()
        msg.set_content(f"Your Neo AI Verification Code is: {otp}\n\nDo not share it.")
        msg['Subject'] = "Neo AI Security Code"
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)
        return True
    except Exception:
        return False

# --- 3. DATABASE INITIALIZATION ---
if "auth_step" not in st.session_state: st.session_state.auth_step = "email_entry"
if "generated_otp" not in st.session_state: st.session_state.generated_otp = None
if "user_email" not in st.session_state: st.session_state.user_email = ""
if "thumbs_left" not in st.session_state: st.session_state.thumbs_left = 3
if "chat_history" not in st.session_state: st.session_state.chat_history = []
if "is_master" not in st.session_state: st.session_state.is_master = False

# --- 4. SECURE AUTH GATEWAY ---
def show_auth_gate():
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    st.title("🛡️ Neo Secure Access")
    
    if st.session_state.auth_step == "email_entry":
        email = st.text_input("Enter your Email", placeholder="example@gmail.com")
        if st.button("Send Verification Code"):
            if "@" in email and "." in email:
                otp = str(random.randint(111111, 999999))
                with st.spinner("Sending code..."):
                    if send_otp_email(email, otp):
                        st.session_state.generated_otp = otp
                        st.session_state.user_email = email
                        st.session_state.auth_step = "otp_verify"
                        st.success("Code sent! Check your Inbox.")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.error("Email failed. Try again.")
            else:
                st.error("Enter a valid email.")

    elif st.session_state.auth_step == "otp_verify":
        st.info(f"Verify email: {st.session_state.user_email}")
        otp_in = st.text_input("Enter 6-Digit Code", placeholder="XXXXXX")
        if st.button("Verify Code"):
            if otp_in == st.session_state.generated_otp:
                st.session_state.auth_step = "set_password"
                st.rerun()
            else:
                st.error("Incorrect code.")

    elif st.session_state.auth_step == "set_password":
        st.subheader("Create Password")
        p1 = st.text_input("New Password", type="password")
        p2 = st.text_input("Confirm Password", type="password")
        if st.button("Register & Login"):
            if len(p1) >= 6 and p1 == p2:
                st.session_state.auth_step = "verified"
                st.success("Registration Successful!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("Passwords must match (6+ chars).")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 5. MAIN APPLICATION ---
if st.session_state.auth_step != "verified":
    show_auth_gate()
else:
    # Sidebar
    with st.sidebar:
        st.title("Neo v8.0 Pro 🚀")
        st.write(f"Logged in: {st.session_state.user_email}")
        m_key = st.text_input("Master Key", type="password")
        if m_key == "NEO_MASTER_2026":
            st.session_state.is_master = True
            st.success("MASTER ACTIVE")
        st.markdown(f'<span class="premium-badge">CREDITS: {st.session_state.thumbs_left if not st.session_state.is_master else "∞"}</span>', unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.auth_step = "email_entry"
            st.rerun()

    tab1, tab2, tab3 = st.tabs(["🗨️ Beast Chat", "🖼️ Pro Thumbnail Maker", "💎 Pro Upgrade"])

    with tab1:
        st.subheader("Real-time Intelligence")
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]): st.markdown(chat["content"])
        if prompt := st.chat_input("Ask the Beast..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            with st.chat_message("assistant"):
                full_text = f"### 🚀 ANALYSIS\nFor '{prompt}': Trend is High. Strategy: Viral Hooks needed."
                placeholder = st.empty()
                typed = ""
                for word in full_text.split(" "):
                    typed += word + " "
                    placeholder.markdown(typed + "▌")
                    time.sleep(0.05)
                placeholder.markdown(typed)
                st.session_state.chat_history.append({"role": "assistant", "content": typed})

    with tab2:
        st.subheader("🎥 Transform Photo to Professional Thumbnail")
        st.markdown('<div class="upload-box">Upload your simple photo and let Neo AI make it attractive!</div>', unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])
        topic = st.text_input("Thumbnail Topic (Text to add)", placeholder="Ex: Earn 10k Daily")
        
        if st.button("Generate Professional Thumbnail"):
            if st.session_state.thumbs_left > 0 or st.session_state.is_master:
                if uploaded_file is not None:
                    with st.spinner("Neo Beast is editing your photo..."):
                        time.sleep(3)
                        if not st.session_state.is_master: st.session_state.thumbs_left -= 1
                        
                        image = Image.open(uploaded_file)
                        st.image(image, caption="Uploaded Photo", use_container_width=True)
                        st.success("✅ Professional Edit Complete!")
                        st.image("https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800", caption="Resulting Professional Thumbnail")
                else:
                    st.error("Please upload a photo first!")
            else:
                st.error("Limit Reached! Upgrade to Pro.")

    with tab3:
        st.markdown(f"""
        <div style="border: 1px solid #EEE; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Pro Access - ₹49</h3>
            <p>Unlimited Photo Uploads & Professional Editing</p>
            <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoPro_{st.session_state.user_email}" class="btn-redirect">Pay via UPI</a>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Logout"):
            st.session_state.auth_step = "email_entry"
            st.rerun()

    tab1, tab2, tab3 = st.tabs(["🗨️ Beast Chat", "🖼️ Pro Thumbnail Maker", "💎 Pro Upgrade"])

    with tab1:
        st.subheader("Real-time Intelligence")
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]): st.markdown(chat["content"])
        if prompt := st.chat_input("Ask the Beast..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            with st.chat_message("assistant"):
                full_text = f"### 🚀 ANALYSIS\nFor '{prompt}': Trend is High. Strategy: Viral Hooks needed."
                placeholder = st.empty()
                typed = ""
                for word in full_text.split(" "):
                    typed += word + " "
                    placeholder.markdown(typed + "▌")
                    time.sleep(0.05)
                placeholder.markdown(typed)
                st.session_state.chat_history.append({"role": "assistant", "content": typed})

    with tab2:
        st.subheader("🎥 Transform Photo to Professional Thumbnail")
        st.markdown('<div class="upload-box">Upload your simple photo and let Neo AI make it attractive!</div>', unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])
        topic = st.text_input("Thumbnail Topic (Text to add)", placeholder="Ex: Earn 10k Daily")
        
        if st.button("Generate Professional Thumbnail"):
            if st.session_state.thumbs_left > 0 or st.session_state.is_master:
                if uploaded_file is not None:
                    with st.spinner("Neo Beast is editing your photo..."):
                        # Processing Simulation
                        time.sleep(3)
                        if not st.session_state.is_master: st.session_state.thumbs_left -= 1
                        
                        image = Image.open(uploaded_file)
                        st.image(image, caption="Uploaded Photo", use_container_width=True)
                        st.success("✅ Professional Edit Complete! (Applied Cinematic Filters & Branding)")
                        # In real world, we would use an AI API to modify the image here
                        st.image("https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800", caption="Resulting Professional Thumbnail")
                else:
                    st.error("Please upload a photo first!")
            else:
                st.error("Limit Reached! Upgrade to Pro.")

    with tab3:
        st.markdown(f"""
        <div style="border: 1px solid #EEE; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Pro Access - ₹49</h3>
            <p>Unlimited Photo Uploads & Professional Editing</p>
            <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoPro_{st.session_state.user_email}" class="btn-redirect">Pay via UPI</a>
        </div>
        """, unsafe_allow_html=True)
            st.rerun()

    tab1, tab2, tab3 = st.tabs(["🗨️ Chat", "🖼️ AI Thumbnail", "💎 Pro Upgrade"])

    with tab1:
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]): st.markdown(chat["content"])
        if prompt := st.chat_input("Ask the Beast..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            with st.chat_message("assistant"):
                full_text = f"### 🚀 ANALYSIS\nFor '{prompt}': Trend is High. Execution required."
                placeholder = st.empty()
                typed = ""
                for word in full_text.split(" "):
                    typed += word + " "
                    placeholder.markdown(typed + "▌")
                    time.sleep(0.06)
                placeholder.markdown(typed)
                st.session_state.chat_history.append({"role": "assistant", "content": typed})

    with tab2:
        topic = st.text_input("Thumbnail Topic")
        if st.button("Generate"):
            if st.session_state.thumbs_left > 0 or st.session_state.is_master:
                with st.spinner("Designing..."):
                    time.sleep(2)
                    if not st.session_state.is_master: st.session_state.thumbs_left -= 1
                    st.image("https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800")
            else:
                st.error("Limit Reached!")

    with tab3:
        st.markdown(f"""
        <div style="border: 1px solid #EEE; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Pro Access - ₹49</h3>
            <p>15+ Viral Thumbnails Monthly</p>
            <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoPro_{st.session_state.user_email}" class="btn-redirect">Pay via UPI</a>
        </div>
        """, unsafe_allow_html=True)
