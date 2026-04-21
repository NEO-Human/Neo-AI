import streamlit as st

# --- 1. THEME & UI SETUP ---
st.set_page_config(page_title="Neo AI - Universal Academy", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .main-title { text-align: center; font-size: 3rem; font-weight: 800; background: linear-gradient(45deg, #00f2fe, #4facfe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; padding: 10px; }
    .course-card { border: 1px solid #1e1e1e; padding: 20px; border-radius: 15px; background: #111111; transition: 0.3s; margin-bottom: 15px; }
    .course-card:hover { border-color: #00f2fe; }
    .tutorial-step { background: #1a1a1a; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #00f2fe; }
    .btn-pay { display: block; background: #00f2fe; color: black !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .free-access { background: #238636; color: white; padding: 5px 15px; border-radius: 20px; font-size: 12px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION CONTROL ---
if "logged_in" not in st.session_state: st.session_state.logged_in = False
if "user_email" not in st.session_state: st.session_state.user_email = ""
if "active_course" not in st.session_state: st.session_state.active_course = None
if "free_access" not in st.session_state: st.session_state.free_access = False

# --- 3. COURSE DATABASE ---
DATA = {
    "📱 Instagram": {
        "Reels Algorithm Secrets": ["Negative Hook Theory", "Open Loop Storytelling", "Every 3-Sec Visual Change", "Audio Volume Hacking"],
        "Insta-Brand Growth": ["Profile SEO & Keywords", "Conversion Bio Formula", "Highlight Funnel Setup", "Collaborative Post Strategy"]
    },
    "🎥 YouTube": {
        "Shorts Viral Roadmap": ["Vertical Hook Mastery", "Looping Secrets", "YouTube SEO (Titles/Tags)", "Community Post Triggers"],
        "Faceless Channel Pro": ["High CPM Niche Selection", "AI Voiceover Excellence", "Stock Footage Sourcing", "Automation Workflow"]
    },
    "💻 Coding (10 Languages)": {
        "Python (AI/Data)": ["Syntax Basics", "NumPy & Pandas", "Automation Scripts", "Building Basic AI"],
        "JavaScript (Web)": ["DOM Manipulation", "ES6+ Features", "React Basics", "API Integration"],
        "Java (Enterprise)": ["OOPs Concepts", "Spring Boot", "Database (MySQL)", "Microservices"],
        "C++ (DSA/Game)": ["Pointers & Memory", "Data Structures", "Algorithms", "Unreal Engine Intro"],
        "Swift (iOS)": ["SwiftUI Layouts", "App Lifecycle", "State Management", "App Store Publishing"],
        "Kotlin (Android)": ["Jetpack Compose", "Retrofit API", "Material Design", "Room Database"],
        "PHP (Backend)": ["Server Logic", "Laravel Framework", "MySQL Advanced", "Web Security"],
        "Rust (Systems)": ["Ownership & Borrowing", "Memory Safety", "Cargo Ecosystem", "Web Assembly"],
        "Go (Backend/Cloud)": ["Concurrency (Goroutines)", "Interfaces", "Microservices", "Docker/K8s"],
        "Ruby (Web Apps)": ["Ruby on Rails", "MVC Architecture", "Active Record", "Deployment"]
    }
}

# --- 4. AUTHENTICATION ---
if not st.session_state.logged_in:
    st.markdown('<div class="main-title">NEO AI ACADEMY</div>', unsafe_allow_html=True)
    _, col_mid, _ = st.columns([1, 1.5, 1])
    with col_mid:
        email_input = st.text_input("Enter Student Email", placeholder="yourname@gmail.com")
        creator_code = st.text_input("Enter Creator/Promo Code (Optional)", type="password")
        if st.button("Unlock Knowledge 🚀", use_container_width=True):
            if "@" in email_input:
                st.session_state.logged_in = True
                st.session_state.user_email = email_input
                if creator_code == "NEO_CREATOR_2026":
                    st.session_state.free_access = True
                st.rerun()
            else: st.error("Invalid Email")

# --- 5. DASHBOARD ---
else:
    with st.sidebar:
        st.title("Neo AI Tutor 🤖")
        st.write(f"Logged: {st.session_state.user_email}")
        if st.session_state.free_access:
            st.markdown('<span class="free-access">VIP CREATOR ACCESS ACTIVE ✅</span>', unsafe_allow_html=True)
        st.divider()
        category = st.selectbox("Select Category", list(DATA.keys()))
        if st.button("🔴 Logout"):
            st.session_state.logged_in = False
            st.rerun()

    st.markdown(f'<h1 style="color: #00f2fe;">{category} Courses</h1>', unsafe_allow_html=True)
    
    # Filtered Courses Display
    courses = DATA[category]
    cols = st.columns(2)
    for i, (name, content) in enumerate(courses.items()):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="course-card">
                <h3>{name}</h3>
                <p style="color: #888;">Complete Step-by-Step AI Coach Roadmap</p>
                <h2 style="color: #00f2fe;">{'FREE' if st.session_state.free_access else '₹49'}</h2>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Start Learning {name}", key=name):
                st.session_state.active_course = (name, content)

    # --- COURSE DETAILS ---
    if st.session_state.active_course:
        st.divider()
        c_name, c_steps = st.session_state.active_course
        st.subheader(f"📖 Roadmap: {c_name}")
        
        l_col, r_col = st.columns([2, 1])
        with l_col:
            for step in c_steps:
                st.markdown(f'<div class="tutorial-step">✅ {step}</div>', unsafe_allow_html=True)
        
        with r_col:
            if st.session_state.free_access:
                st.success("You have full access to Video Tutorials and Assets!")
                st.button("📥 Download Master Resource Pack")
            else:
                st.markdown(f"""
                <div style="background: #111; padding: 25px; border-radius: 15px; border: 2px solid #00f2fe; text-align: center;">
                    <h4>Get Private Video Lessons</h4>
                    <p style="font-size: 14px;">In-depth tutorials & secret templates.</p>
                    <h1 style="color: #00f2fe;">₹49</h1>
                    <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn={c_name.replace(' ', '')}" class="btn-pay">UNLOCK FULL COURSE</a>
                </div>
                """, unsafe_allow_html=True)

    st.divider()
    st.caption("Neo AI Academy v16.0 | Professional Digital Learning Hub")
