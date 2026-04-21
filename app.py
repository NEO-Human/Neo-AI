import streamlit as st

# --- 1. SETTINGS & UI ---
st.set_page_config(page_title="Neo AI - Learning Hub", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .level-box { background: #111; padding: 20px; border-radius: 15px; border: 1px solid #222; margin-bottom: 10px; }
    .lock-icon { color: #555; font-size: 14px; }
    .unlock-icon { color: #00f2fe; font-size: 14px; font-weight: bold; }
    .video-container { border: 2px solid #00f2fe; border-radius: 15px; overflow: hidden; margin-bottom: 20px; }
    .quiz-container { background: #1a1a1a; padding: 20px; border-radius: 12px; border-left: 5px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE (For Progress Tracking) ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "current_level" not in st.session_state: st.session_state.current_level = 1
if "score" not in st.session_state: st.session_state.score = 0
if "is_paid" not in st.session_state: st.session_state.is_paid = False

# --- 3. COURSE CONTENT (Videos & Quizzes) ---
# Yahan aap apni YouTube video links aur Quizzes add kar sakte hain
COURSE_DATA = {
    1: {
        "title": "Level 1: The Viral Psychology",
        "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", # Replace with your tutorial link
        "lesson": "Is video mein sikhein kaise audience ke dimaag se khel kar hooks banate hain.",
        "quiz_q": "Viral hone ke liye video ke pehle ___ seconds sabse zaroori hain?",
        "quiz_a": ["10 Seconds", "3 Seconds", "30 Seconds"],
        "correct": "3 Seconds"
    },
    2: {
        "title": "Level 2: Advanced Editing Hacks",
        "video": "https://www.youtube.com/watch?v=your_video_2",
        "lesson": "CapCut aur VN mein professional keyframing kaise karein.",
        "quiz_q": "Smooth motion ke liye kis tool ka use hota hai?",
        "quiz_a": ["Filters", "Keyframes", "Crop"],
        "correct": "Keyframes"
    }
}

# --- 4. LOGIN & PAYMENT GATE ---
if not st.session_state.logged_in:
    st.title("🛡️ Neo AI Masterclass")
    email = st.text_input("Enter Email")
    code = st.text_input("Creator Code (Optional)", type="password")
    if st.button("Start My Journey"):
        if "@" in email:
            st.session_state.logged_in = True
            if code == "NEO_CREATOR_2026": st.session_state.is_paid = True
            st.rerun()

# --- 5. MAIN LEARNING DASHBOARD ---
else:
    with st.sidebar:
        st.title("Neo Coach 🤖")
        st.markdown(f"**Level Reached:** {st.session_state.current_level}")
        if not st.session_state.is_paid:
            st.warning("Locked: Pay ₹49 for Full Access")
        else:
            st.success("Elite Access Unlocked ✅")
        
        if st.button("🔴 Logout"):
            st.session_state.logged_in = False
            st.rerun()

    # --- COURSE INTERFACE ---
    st.title("🚀 Social Media Mastery")
    
    # Levels Sidebar/Buttons
    cols = st.columns(len(COURSE_DATA))
    for i, lvl in enumerate(COURSE_DATA):
        with cols[i]:
            if st.session_state.current_level >= lvl:
                if st.button(f"✅ Level {lvl}", use_container_width=True):
                    pass # Current level active
            else:
                st.button(f"🔒 Level {lvl}", disabled=True, use_container_width=True)

    st.divider()

    # --- ACTIVE LEVEL CONTENT ---
    curr = st.session_state.current_level
    if curr in COURSE_DATA:
        data = COURSE_DATA[curr]
        
        # Payment Check
        if not st.session_state.is_paid and curr > 1:
            st.error("Aage badhne ke liye course unlock karein!")
            st.markdown(f"""
                <div style="text-align: center; background: #111; padding: 30px; border-radius: 15px; border: 1px solid #00f2fe;">
                    <h3>Unlock Advanced Levels</h3>
                    <p>Get Master Notes + All Video Tutorials</p>
                    <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=Masterclass" 
                       style="background:#00f2fe; color:black; padding:12px 25px; text-decoration:none; border-radius:8px; font-weight:bold;">PAY ₹49 NOW</a>
                </div>
            """, unsafe_allow_html=True)
        else:
            # Video Player
            st.subheader(data["title"])
            st.video(data["video"])
            st.info(data["lesson"])

            # Quiz Section
            st.markdown('<div class="quiz-container">', unsafe_allow_html=True)
            st.write(f"**Quiz:** {data['quiz_q']}")
            ans = st.radio("Sahi jawab chunein:", data["quiz_a"], key=f"q_{curr}")
            
            if st.button("Submit Answer & Next Level"):
                if ans == data["correct"]:
                    st.success("Sahi Jawab! Agla Level Unlock Ho Gaya.")
                    st.session_state.current_level += 1
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Galat jawab! Video phir se dekhein.")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.balloons()
        st.success("Badhai ho! Aapne pura course complete kar liya hai.")
