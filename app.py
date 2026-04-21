import streamlit as st
import time
import random
import smtplib
from email.message import EmailMessage

# --- 1. CONFIG ---
st.set_page_config(page_title="Neo AI Academy", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    .course-card { border: 1px solid #ddd; padding: 20px; border-radius: 15px; background: white; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
    .premium-badge { background: #ff4b4b; color: white; padding: 2px 10px; border-radius: 10px; font-size: 12px; }
    .btn-pay { display: block; background: #28a745; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .tutor-msg { background: #e9ecef; padding: 15px; border-radius: 10px; border-left: 5px solid #007bff; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AUTH & SESSION ---
if "auth_step" not in st.session_state: st.session_state.auth_step = "login"
if "u_email" not in st.session_state: st.session_state.u_email = ""
if "is_pro" not in st.session_state: st.session_state.is_pro = False

# --- 3. TEACHING CONTENT (The "AI" Brain) ---
COURSES = {
    "Digital Marketing": [
        "Module 1: SEO Basics - Search Engine Optimization kya hai?",
        "Module 2: Social Media Ads - Facebook/Instagram par ads kaise chalayein.",
        "Module 3: Email Marketing - Customers ko engage kaise rakhein.",
        "Module 4: Google Analytics - Data padhna sikhein."
    ],
    "Video Editing": [
        "CapCut & VN: Mobile editing ke hidden features.",
        "Premiere Pro: Professional cutting aur color grading.",
        "Transitions: Cinematic feel kaise laayein.",
        "Audio Sync: Sound effects aur music layering."
    ]
}

# --- 4. LOGIN INTERFACE ---
if st.session_state.auth_step == "login":
    st.title("🎓 Neo AI Academy")
    email = st.text_input("Enter Email to Start Learning")
    if st.button("Access Academy"):
        if "@" in email:
            st.session_state.u_email = email
            st.session_state.auth_step = "main"
            st.rerun()

# --- 5. MAIN ACADEMY ---
else:
    with st.sidebar:
        st.title("Neo AI Tutor 🤖")
        st.write(f"Logged: {st.session_state.u_email}")
        if st.session_state.is_pro:
            st.success("✅ PRO MEMBER")
        else:
            st.warning("⚡ FREE TIER")
        
        # Admin Bypass
        master = st.text_input("Master Key", type="password")
        if master == "NEO_MASTER_2026":
            st.session_state.is_pro = True
        
        if st.button("Logout"):
            st.session_state.auth_step = "login"
            st.rerun()

    st.title("Sikhein Digital Skills, AI ke saath! 🚀")
    
    t1, t2, t3 = st.tabs(["📚 My Courses", "🤖 AI Tutor (Chat)", "💎 Upgrade"])

    with t1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="course-card"><h3>📈 Digital Marketing</h3><p>Master Google Ads, Meta Ads and SEO.</p></div>', unsafe_allow_html=True)
            for m in COURSES["Digital Marketing"]:
                st.write(f"✅ {m}")
        
        with col2:
            st.markdown('<div class="course-card"><h3>🎬 Professional Editing</h3><p>Learn CapCut, Premiere Pro & VN.</p></div>', unsafe_allow_html=True)
            for m in COURSES["Video Editing"]:
                st.write(f"✅ {m}")

    with t2:
        st.subheader("Neo AI Personal Tutor")
        query = st.chat_input("Editing ya Marketing ke baare mein pucho...")
        
        if query:
            with st.chat_message("user"): st.write(query)
            with st.chat_message("assistant"):
                # Intelligent Rule-Based Response (No API needed)
                if "marketing" in query.lower():
                    st.write("Digital Marketing mein success ke liye 3 cheezein zaroori hain: Right Audience, Catchy Hook, aur Retargeting. Aapko Meta Ads Manager se shuru karna chahiye!")
                elif "editing" in query.lower() or "software" in query.lower():
                    st.write("Professional editing ke liye VN (Mobile) ya Premiere Pro (PC) best hai. Keyframes aur Masking seekhna sabse important hai.")
                else:
                    st.write("Bhai, main aapka Neo AI Tutor hoon. Main aapko Digital Marketing aur Video Editing sikhane mein help kar sakta hoon. Kya aap shuru karna chahte hain?")

    with t3:
        if not st.session_state.is_pro:
            st.markdown(f"""
            <div style="border: 2px solid #ff4b4b; padding: 30px; border-radius: 15px; text-align: center; background: white;">
                <h2>Unlock Full Mastery Course</h2>
                <p>Advance Video Editing + Digital Marketing + AI Automation</p>
                <h1 style="color: #ff4b4b;">₹49</h1>
                <p>Ek baar pay karein, hamesha ke liye sikhein.</p>
                <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=Course_{st.session_state.u_email}" class="btn-pay">PAY VIA UPI - ₹49</a>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.success("Aapke paas full access hai! Niche se advanced resources download karein.")
            st.button("📥 Download Editing Assets (Overlays/Presets)")
