import streamlit as st
import time

# --- 1. THEME & UI SETUP ---
st.set_page_config(page_title="Neo AI Elite Academy", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .main-title { text-align: center; font-size: 3.5rem; font-weight: 800; background: linear-gradient(45deg, #00f2fe, #4facfe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; padding: 20px; }
    .course-card { border: 1px solid #1e1e1e; padding: 25px; border-radius: 20px; background: #111111; transition: 0.4s; position: relative; overflow: hidden; }
    .course-card:hover { border-color: #00f2fe; box-shadow: 0 0 20px rgba(0, 242, 254, 0.2); }
    .premium-tag { position: absolute; top: 15px; right: 15px; background: #FFD700; color: black; padding: 2px 10px; border-radius: 5px; font-size: 10px; font-weight: bold; }
    .tutorial-step { background: #1a1a1a; padding: 20px; border-radius: 12px; margin: 15px 0; border-left: 4px solid #00f2fe; }
    .btn-pay { display: block; background: #00f2fe; color: black !important; padding: 15px; border-radius: 10px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 20px; font-size: 18px; }
    .btn-pay:hover { background: #4facfe; }
    .sidebar-info { padding: 15px; background: #111; border-radius: 10px; border: 1px solid #222; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION CONTROL ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "active_course" not in st.session_state: st.session_state.active_course = None

# --- 3. ELITE CONTENT DATABASE (Paid Strategies) ---
ELITE_COURSES = {
    "Viral Psychological Hooks": {
        "price": "49",
        "tag": "SECRET STRATEGY",
        "intro": "YouTube par koi nahi batata: Audience ke dimaag se kaise khelte hain.",
        "modules": [
            {"title": "The Negative Hook", "desc": "Kyun 'Don't do this' wali videos 'Do this' se 10x zyada chalti hain."},
            {"title": "Open Loop Theory", "desc": "Video ke beech mein loop kaise kholein taaki log end tak rukein."},
            {"title": "Retention Editing", "desc": "Every 3 seconds change rule - Visual storytelling ka asli sach."},
            {"title": "Algorithm Trigger", "desc": "Watch-time vs Engagement ka sahi ratio jo video push karta hai."}
        ],
        "upi_id": "9665145228-2@axl"
    },
    "High-End Creation Skills": {
        "price": "49",
        "tag": "CREATIVE EDGE",
        "intro": "Mobile se Professional level editing aur Color Grading (CapCut/VN).",
        "modules": [
            {"title": "Advanced Masking", "desc": "Clone yourself aur objects ko gayab karne wali professional techniques."},
            {"title": "Keyframe Mastery", "desc": "Smooth camera movements aur tracking bina gimbal ke."},
            {"title": "Color Psychology", "desc": "Mood ke hisaab se grading - Viral aesthetic looks kaise banayein."},
            {"title": "Sound Design", "desc": "SFX layering jo 50% video quality improve kar deti hai."}
        ],
        "upi_id": "9665145228-2@axl"
    },
    "Digital Sales Machine": {
        "price": "49",
        "tag": "MONEY MAKING",
        "intro": "Bina dikhe (Faceless) mahine ka ₹50k+ kaise earn karein.",
        "modules": [
            {"title": "Niche Goldmine", "desc": "Kam competition aur high CPM wale topics ki list."},
            {"title": "AI Automation", "desc": "Script, Voiceover aur Video AI se generate karke automate karna."},
            {"title": "Affiliate Funnel", "desc": "Instagram bio se passive income generate karne ka setup."},
            {"title": "Brand Deals", "desc": "Chote accounts par bhi brands ko kaise approach karein."}
        ],
        "upi_id": "9665145228-2@axl"
    }
}

# --- 4. LOGIN / AUTH ---
if not st.session_state.logged_in:
    st.markdown('<div class="main-title">NEO AI ELITE ACADEMY</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Premium Skills & Viral Strategies at Zero Inflation Price</p>", unsafe_allow_html=True)
    
    with st.container():
        _, col_mid, _ = st.columns([1, 1.5, 1])
        with col_mid:
            email = st.text_input("Student Email", placeholder="Your best email...")
            if st.button("Unlock Academy 🔓", use_container_width=True):
                if "@" in email:
                    st.session_state.logged_in = True
                    st.rerun()

# --- 5. DASHBOARD ---
else:
    with st.sidebar:
        st.title("Neo Coach 🤖")
        st.markdown(f"**Member:** {email}")
        st.markdown('<div class="sidebar-info">Status: <b>Elite Access</b></div>', unsafe_allow_html=True)
        st.divider()
        st.write("Current Ranking: #450/10,000 Students")
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown('<h2 style="text-align: center;">Pick Your Specialization</h2>', unsafe_allow_html=True)
    
    # Grid for Courses
    cols = st.columns(3)
    for i, (name, data) in enumerate(ELITE_COURSES.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="course-card">
                <span class="premium-tag">{data['tag']}</span>
                <h3>{name}</h3>
                <p style="color: #999; font-size: 14px;">{data['intro']}</p>
                <h2 style="color: #00f2fe;">₹{data['price']}</h2>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"View Syllabus", key=name, use_container_width=True):
                st.session_state.active_course = name

    # --- COURSE TUTORIALS SECTION ---
    if st.session_state.active_course:
        st.divider()
        selected = st.session_state.active_course
        course = ELITE_COURSES[selected]
        
        st.markdown(f"<h1 style='color: #00f2fe;'>📖 {selected}</h1>", unsafe_allow_html=True)
        
        left, right = st.columns([2, 1])
        
        with left:
            st.subheader("Advanced Tutorial Roadmap (Basic to Pro)")
            for mod in course["modules"]:
                st.markdown(f"""
                <div class="tutorial-step">
                    <h4>✅ {mod['title']}</h4>
                    <p style="margin: 0; color: #bbb;">{mod['desc']}</p>
                </div>
                """, unsafe_allow_html=True)

        with right:
            st.markdown(f"""
            <div style="background: #111; padding: 30px; border-radius: 20px; border: 2px solid #00f2fe; text-align: center;">
                <h3>Unlock Full Video Tutorials</h3>
                <p>Get exclusive access to screen-recordings, asset packs, and private community.</p>
                <h1 style="color: #00f2fe;">₹49</h1>
                <a href="upi://pay?pa={course['upi_id']}&pn=NeoAI&am=49&cu=INR&tn={selected.replace(' ', '')}" class="btn-pay">GET FULL ACCESS</a>
                <p style="margin-top:15px; font-size: 12px; color: #555;">Payment is 100% Secure via UPI</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
            st.write("🎯 **Skill Improvement:** Is course ke baad aapka content creation quality 5x improve ho jayega, guaranteed.")

    st.divider()
    st.caption("© 2026 Neo AI Academy - Breaking the ₹499 Course Barrier.")
