import streamlit as st
import google.generativeai as genai

# --- 1. SETTINGS & PREMIUM BEAST THEME ---
st.set_page_config(page_title="Neo AI - Beast Mode", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    /* Main Background & Fonts */
    .stApp { background-color: #FFFFFF; color: #1A1A1B; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { background-color: #F8F9FA !important; border-right: 1px solid #E5E7EB; }
    
    /* Beast Response Styling */
    .beast-response { 
        border-left: 5px solid #000000; 
        padding: 20px; 
        background: #F9FAFB; 
        border-radius: 0 12px 12px 0; 
        margin-bottom: 25px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }
    .next-move-box { 
        background: #DCFCE7; 
        color: #15803D; 
        padding: 15px; 
        border-radius: 8px; 
        border: 1px solid #15803D; 
        font-weight: bold;
        margin-top: 15px;
    }
    
    /* Premium Store Cards */
    .premium-card {
        border: 1px solid #E5E7EB;
        padding: 20px;
        border-radius: 15px;
        background: #FFFFFF;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    .price-tag { color: #10a37f; font-weight: bold; font-size: 26px; }
    
    /* Action Buttons */
    .btn-redirect {
        display: block;
        background-color: #000000;
        color: white !important;
        padding: 12px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }
    .master-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 5px; border-radius: 5px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURATION & LOGIC ---
# Replace with your actual Gemini API Key
# genai.configure(api_key="YOUR_GEMINI_API_KEY")

UPI_ID = "9665145228-2@axl"
PAYEE_NAME = "Neo AI Creator"

def get_upi_link(amount, note):
    return f"upi://pay?pa={UPI_ID}&pn={PAYEE_NAME}&am={amount}&cu=INR&tn={note}"

# --- 3. SIDEBAR CONTROL ---
with st.sidebar:
    st.title("Neo v4.0 Beast 🚀")
    user_name = st.text_input("Identify Yourself", placeholder="Name")
    master_key = st.text_input("Master Key", type="password", placeholder="Secret Key")
    
    is_master = False
    if master_key == "NEO_MASTER_2026":
        is_master = True
        st.markdown('<div class="master-badge">🔓 MASTER ACCESS ACTIVE</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    if st.button("➕ New Beast Session"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("💰 **Direct Support**")
    st.markdown(f'<a href="tel:9665145228" class="btn-redirect">📞 Call Creator</a>', unsafe_allow_html=True)

# --- 4. MAIN APP LOGIC ---
if not user_name:
    st.title("Welcome to Neo Intelligence")
    st.subheader("The World's Cleanest AI Beast.")
    st.write("Enter your name in the sidebar to start the 10x Intelligence experience.")
    st.image("https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&q=80&w=1000")
else:
    if "messages" not in st.session_state: st.session_state.messages = []
    
    tab1, tab2, tab3 = st.tabs(["🗨️ Beast Chat", "💎 Premium Store", "📊 Intelligence"])

    # --- TAB 1: BEAST CHAT (DETAILED ANSWERS) ---
    with tab1:
        st.markdown(f"### Active Session: {user_name}")
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"], unsafe_allow_html=True)
        
        if prompt := st.chat_input("Ask the Beast for a Roadmap..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                # Beast Mode Logic: Structured Response
                beast_reply = f"""
                <div class="beast-response">
                ### 🚀 THE CORE ANSWER:
                Aapne pucha <b>"{prompt}"</b>. Iska seedha aur sabse powerful solution yeh hai ki aap core fundamentals par focus karein aur Neo ke tools ka use karke process ko automate karein.
                
                ### 📊 BEAST FACTS & DATA:
                * **Market Context:** 2026 mein is sector ki growth 35% CAGR se badh rahi hai.
                * **User Behavior:** 80% successful creators/businesses ab AI-first strategy use kar rahe hain.
                * **Verified Logic:** Factual data ke mutabik, execution speed hi sabse bada differentiator hai.

                ### 🛠️ STEP-BY-STEP EXECUTION:
                1. **Analysis:** Pehle niche market ka data scan karein (Neo Trends use karein).
                2. **Setup:** Apne digital assets aur AI workflow ko integrate karein.
                3. **Scaling:** Feedback loop banayein aur repetitive tasks ko Neo API ko saunp dein.

                <div class="next-move-box">
                🏁 THE NEXT MOVE: 
                Right now, aapko apne workflow ka audit karna chahiye. Agla kadam hai Neo Pro unlock karna taaki aapko "7-Day Future Projections" mil sakein!
                </div>
                </div>
                """
                st.markdown(beast_reply, unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": beast_reply})

    # --- TAB 2: PREMIUM STORE (UPI REDIRECT) ---
    with tab2:
        st.subheader("💎 Unlock Full Beast Potential")
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"""<div class="premium-card">
                <h3>Standard Beast</h3>
                <p>7-Day Future Trends Access</p>
                <div class="price-tag">₹29</div>
                {f'<a href="{get_upi_link(29, "NeoStandard")}" class="btn-redirect">Pay via UPI App</a>' if not is_master else '<b>FREE FOR MASTER</b>'}
            </div>""", unsafe_allow_html=True)

        with c2:
            st.markdown(f"""<div class="premium-card">
                <h3>Ultimate Monster</h3>
                <p>Full API + GPT-4o Access</p>
                <div class="price-tag">₹49</div>
                {f'<a href="{get_upi_link(49, "NeoUltimate")}" class="btn-redirect">Pay via UPI App</a>' if not is_master else '<b>FREE FOR MASTER</b>'}
            </div>""", unsafe_allow_html=True)
            
        st.markdown(f'<a href="https://wa.me/919665145228?text=I%20have%20paid%20for%20Neo%20Pro" target="_blank" style="color:#25D366; text-align:center; display:block; text-decoration:none; font-weight:bold;">✅ Send Payment Screenshot on WhatsApp</a>', unsafe_allow_html=True)

    # --- TAB 3: INTELLIGENCE ---
    with tab3:
        st.subheader("📊 7-Day Future Intelligence")
        if is_master:
            st.info("📈 **Master Stream Active:**\n\n1. Upcoming Viral Hook: 'AI is not the future, it's the present'.\n2. High ROI Skill: AI Workflow Engineering.\n3. Market Gap: Personalized AI agents for local Kirana stores.")
        else:
            st.warning("🔒 Intelligence Tab is Locked.")
            st.write("Upgrade to 'Standard Beast' to see future viral trends and market gaps.")
    with tab2:
        st.subheader("🚀 Upgrade to Beast Mode")
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown(f"""<div class="premium-card">
                <h3>Standard Pro</h3>
                <p>Unlock 7-Day Trends</p>
                <div class="price-tag">₹29</div>
                {f'<a href="{get_upi_link(29, "NeoStandard")}" class="buy-btn">Pay via UPI App</a>' if not is_master else '<b>FREE FOR MASTER</b>'}
            </div>""", unsafe_allow_html=True)
            if not is_master:
                st.markdown(f'<a href="https://wa.me/919665145228?text=Paid%2029%20for%20Neo" target="_blank" style="color:#25D366; text-align:center; display:block;">Verify on WhatsApp</a>', unsafe_allow_html=True)

        with c2:
            st.markdown(f"""<div class="premium-card">
                <h3>Ultimate Beast</h3>
                <p>Full API Access + GPT-4</p>
                <div class="price-tag">₹49</div>
                {f'<a href="{get_upi_link(49, "NeoUltimate")}" class="buy-btn">Pay via UPI App</a>' if not is_master else '<b>FREE FOR MASTER</b>'}
            </div>""", unsafe_allow_html=True)
            if not is_master:
                st.markdown(f'<a href="https://wa.me/919665145228?text=Paid%2049%20for%20Neo" target="_blank" style="color:#25D366; text-align:center; display:block;">Verify on WhatsApp</a>', unsafe_allow_html=True)

    # --- TRENDS TAB ---
    with tab3:
        st.subheader("📊 7-Day Intelligence")
        if is_master:
            st.success("✅ Live Data Stream Active")
            st.write("**Next Viral Trend:** AI-driven Faceless YouTube Channels.")
            st.write("**Growth Hack:** Micro-SaaS for Instagram automation.")
        else:
            st.warning("🔒 This section is locked for Free users.")
            st.info("Buy 'Standard Pro' to unlock 7-day viral projections.")
