import streamlit as st
import time  # <--- Ye line missing thi, ab fix ho gayi hai

# --- 1. SETTINGS & UI ---
st.set_page_config(page_title="Neo AI - Masterclass Hub", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .main-title { text-align: center; font-size: 3rem; font-weight: 800; background: linear-gradient(45deg, #00f2fe, #4facfe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; padding: 10px; }
    .course-card { border: 1px solid #1e1e1e; padding: 20px; border-radius: 15px; background: #111111; transition: 0.3s; margin-bottom: 15px; }
    .course-card:hover { border-color: #00f2fe; }
    .tutorial-step { background: #1a1a1a; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #00f2fe; }
    .quiz-container { background: #0e1117; padding: 20px; border-radius: 15px; border: 1px solid #333; margin-top: 20px; }
    .btn-pay { display: block; background: #00f2fe; color: black !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .creator-badge { background: #238636; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_email" not in st.session_state: st.session_state.user_email = ""
if "is_paid" not in st.session_state: st.session_state.is_paid = False
if "current_level" not in st.session_state: st.session_state.current_level = 1
if "active_tab" not in st.session_state: st.session_state.active_tab = "Social Media"

# --- 3. DATA & LEVELS ---
SOCIAL_LEVELS = {
    1: {"title": "L1: Viral Psychology", "q": "Viral video ke pehle 3 seconds ko kya kehte hain?", "a": ["Ending", "Hook", "Mid-roll"], "correct": "Hook"},
    2: {"title": "L2: Algorithm Secrets", "q": "Koshish karein ki aapka Watch-time kitne % se upar ho?", "a": ["20%", "40%", "70%"], "correct": "70%"},
    3: {"title": "L3: High-End Editing", "q": "Moving objects ko track karne ke liye kya use hota hai?", "a": ["Filter", "Keyframe", "Crop"], "correct": "Keyframe"}
}

CODING_DATA = {
    "Python": ["Syntax", "Automation", "AI Intro"], "JS": ["DOM", "React", "APIs"],
    "Java": ["OOPs", "Spring"], "C++": ["DSA", "Game Dev"], "Swift": ["iOS Apps"],
    "Kotlin": ["Android"], "PHP": ["Laravel"], "Rust": ["Safety"], "Go": ["Cloud"], "Ruby": ["Rails"]
}

# --- 4. LOGIN & AUTH ---
if not st.session_state.logged_in:
    st.markdown('<div class="main-title">NEO AI ACADEMY</div>', unsafe_allow_html=True)
    _, col_mid, _ = st.columns([1, 1.5, 1])
    with col_mid:
        email = st.text_input("Enter Email")
        code = st.text_input("Creator Code (Optional)", type="password")
        if st.button("Start Journey 🚀", use_container_width=True):
            if "@" in email:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                if code == "NEO_CREATOR_2026": st.session_state.is_paid = True
                st.rerun()
            else: st.error("Valid email please.")

# --- 5. MAIN DASHBOARD ---
else:
    with st.sidebar:
        st.title("Neo Coach 🤖")
        st.write(f"Logged: {st.session_state.user_email}")
        if st.session_state.is_paid: st.markdown('<span class="creator-badge">CREATOR ACCESS ACTIVE</span>', unsafe_allow_html=True)
        st.divider()
        st.session_state.active_tab = st.selectbox("Switch Department", ["Social Media", "Coding Academy"])
        if st.button("🔴 Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # --- DEPARTMENT 1: SOCIAL MEDIA (LEVELS & QUIZ) ---
    if st.session_state.active_tab == "Social Media":
        st.title("🚀 Social Media Masterclass")
        
        # Level Indicators
        l_cols = st.columns(len(SOCIAL_LEVELS))
        for i, lvl in enumerate(SOCIAL_LEVELS):
            with l_cols[i]:
                if st.session_state.current_level >= lvl:
                    st.success(SOCIAL_LEVELS[lvl]["title"])
                else:
                    st.info(f"🔒 Locked")

        st.divider()
        curr = st.session_state.current_level
        if curr in SOCIAL_LEVELS:
            data = SOCIAL_LEVELS[curr]
            if not st.session_state.is_paid and curr > 1:
                st.error("Unlock Masterclass to proceed to Level 2!")
                st.markdown(f'<a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=Masterclass" class="btn-pay">PAY ₹49 TO UNLOCK ALL LEVELS</a>', unsafe_allow_html=True)
            else:
                st.subheader(f"Level {curr}: Tutorial Video")
                st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Replace with your real tutorial link
                
                with st.container():
                    st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
                    st.write(f"**Question:** {data['q']}")
                    ans = st.radio("Choose correct answer:", data["a"], key=f"q{curr}")
                    if st.button("Submit & Next Level"):
                        if ans == data["correct"]:
                            st.success("Sahi Jawab! Next Level Unlocked.")
                            st.session_state.current_level += 1
                            time.sleep(1) # <--- Ab Error nahi aayega
                            st.rerun()
                        else: st.error("Galat! Video dhyan se dekhein.")
                    st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.balloons()
            st.success("Mastery Complete! You are now a Viral Expert.")

    # --- DEPARTMENT 2: CODING ACADEMY ---
    else:
        st.title("💻 10 Language Coding Bootcamp")
        c_cols = st.columns(2)
        for i, (lang, steps) in enumerate(CODING_DATA.items()):
            with c_cols[i % 2]:
                with st.expander(f"🚀 {lang} Roadmap"):
                    for s in steps:
                        st.write(f"✅ {s}")
                    if not st.session_state.is_paid:
                        st.markdown(f'<a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn={lang}" class="btn-pay">Unlock {lang} Tutorials - ₹49</a>', unsafe_allow_html=True)
                    else:
                        st.button(f"Download {lang} Notes (Free for You)")

