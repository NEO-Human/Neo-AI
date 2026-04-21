import streamlit as st
import time

# --- 1. SETTINGS & STYLING ---
st.set_page_config(page_title="Neo AI - Viral Academy", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .course-card { border: 1px solid #30363d; padding: 20px; border-radius: 15px; background: #161b22; margin-bottom: 20px; transition: 0.3s; }
    .course-card:hover { border-color: #10a37f; transform: translateY(-5px); }
    .task-box { background: #21262d; border-radius: 10px; padding: 15px; margin: 10px 0; border-left: 5px solid #10a37f; color: #c9d1d9; }
    .btn-pay { display: block; background: #238636; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .btn-pay:hover { background: #2ea043; }
    .step-badge { background: #30363d; padding: 4px 10px; border-radius: 20px; font-size: 12px; color: #10a37f; border: 1px solid #10a37f; }
    .main-header { text-align: center; padding: 20px; background: linear-gradient(90deg, #10a37f, #007bff); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-size: 3rem; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SESSION STATE ---
if "auth" not in st.session_state: st.session_state.auth = False
if "course_unlocked" not in st.session_state: st.session_state.course_unlocked = None

# --- 3. VIRAL COURSE DATABASE ---
VIRAL_COURSES = {
    "Instagram Viral Mastery": {
        "price": "49",
        "description": "Reels algorithm ko crack karein aur 30 din mein followers badhayein.",
        "steps": [
            "Task 1: Profile Audit - SEO friendly bio aur professional DP lagayein.",
            "Task 2: The 3-Second Hook - Audience ko scroll karne se rokne ka formula.",
            "Task 3: Viral Transitions - CapCut/VN se cinematic cuts lagana sikhein.",
            "Task 4: Engagement Loop - Stories aur Comments se reach badhane ki trick."
        ],
        "bonus": "Instagram Hashtag Strategy PDF Included"
    },
    "YouTube Shorts Empire": {
        "price": "49",
        "description": "Shorts shelf par viral hone ke liye step-by-step content strategy.",
        "steps": [
            "Task 1: Niche Hunt - Kam mehnat aur zyada views wale topics.",
            "Task 2: High Retention Scripting - Log poori video dekhein aisi scripting.",
            "Task 3: Vertical SEO - Title aur Tags jo search mein rank karein.",
            "Task 4: Community Tab Hacks - Bina video ke 1000 subscribers."
        ],
        "bonus": "100+ Viral Shorts Hook Templates"
    },
    "Digital Marketing Pro": {
        "price": "49",
        "description": "Ads chalana aur products sell karna sikhein AI ki madad se.",
        "steps": [
            "Task 1: Meta Ads Setup - Facebook aur Instagram par ads launch karna.",
            "Task 2: Landing Page Design - Conversion badhane wala page kaise banayein.",
            "Task 3: Copywriting - Aise shabd jo sales layein.",
            "Task 4: Retargeting - Purane customers ko wapas kaise layein."
        ],
        "bonus": "Marketing Budget Calculator Tool"
    }
}

# --- 4. AUTHENTICATION ---
if not st.session_state.auth:
    st.markdown('<div class="main-header">NEO AI ACADEMY</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>AI Powered Viral Roadmap & Skill Learning</p>", unsafe_allow_html=True)
    
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        u_email = st.text_input("Enter Email to Access Courses", placeholder="example@gmail.com")
        if st.button("Enter Academy 🚀", use_container_width=True):
            if "@" in u_email:
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Please enter a valid email address.")

# --- 5. MAIN ACADEMY DASHBOARD ---
else:
    with st.sidebar:
        st.title("Neo AI Coach 🤖")
        st.write(f"Learning as: {st.session_state.u_email}")
        st.divider()
        st.markdown("### 🎯 Your Goal: 1M Reach")
        st.progress(35)
        st.divider()
        if st.button("🔴 Logout"):
            st.session_state.auth = False
            st.rerun()

    st.markdown('<div class="main-header" style="font-size: 2rem;">Choose Your Path to Success</div>', unsafe_allow_html=True)
    
    # Course Grid
    col1, col2, col3 = st.columns(3)
    
    for i, (name, data) in enumerate(VIRAL_COURSES.items()):
        current_col = [col1, col2, col3][i % 3]
        with current_col:
            st.markdown(f"""
            <div class="course-card">
                <span class="step-badge">4-Step Task Course</span>
                <h3 style="margin-top:10px;">{name}</h3>
                <p style="font-size: 14px; color: #8b949e;">{data['description']}</p>
                <h2 style="color:#10a37f;">₹{data['price']}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Start Roadmap", key=name, use_container_width=True):
                st.session_state.course_unlocked = name

    # --- COURSE DETAILS SECTION ---
    if st.session_state.course_unlocked:
        st.divider()
        selected = st.session_state.course_unlocked
        course_info = VIRAL_COURSES[selected]
        
        st.header(f"📖 Roadmap: {selected}")
        
        left_col, right_col = st.columns([2, 1])
        
        with left_col:
            st.subheader("Step-by-Step Viral Tasks")
            for step in course_info["steps"]:
                st.markdown(f'<div class="task-box">{step}</div>', unsafe_allow_html=True)
            
            st.info(f"🎁 **Bonus Content:** {course_info['bonus']}")

        with right_col:
            st.markdown(f"""
            <div style="border: 1px solid #10a37f; padding: 25px; border-radius: 15px; background: #161b22; text-align: center;">
                <h4>Unlock Certification & Assets</h4>
                <p style="font-size: 14px;">Pure roadmap aur hidden viral hacks unlock karne ke liye pay karein.</p>
                <h2 style="color:#10a37f;">₹49 Only</h2>
                <a href="upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn={selected.replace(' ', '')}" class="btn-pay">PAY VIA UPI & UNLOCK</a>
                <p style="font-size:10px; margin-top:10px; color: #8b949e;">Course valid for lifetime access</p>
            </div>
            """, unsafe_allow_html=True)

    # --- FOOTER ---
    st.divider()
    st.caption("Neo AI Academy v15.0 | Built for the next generation of creators.")

