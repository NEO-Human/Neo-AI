import streamlit as st
import google.generativeai as genai

# --- 1. SETTINGS & PREMIUM THEME ---
st.set_page_config(page_title="Neo AI - Master Beast", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #FFFFFF; color: #1A1A1B; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { background-color: #F8F9FA !important; border-right: 1px solid #E5E7EB; }
    
    /* Premium Card Design */
    .premium-card {
        border: 1px solid #E5E7EB;
        padding: 25px;
        border-radius: 15px;
        background: #FFFFFF;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .premium-card:hover { transform: translateY(-5px); border-color: #10a37f; }
    
    /* Pricing & Buttons */
    .price-tag { color: #10a37f; font-weight: bold; font-size: 28px; margin: 10px 0; }
    .buy-btn {
        display: block;
        background-color: #000000;
        color: white !important;
        padding: 12px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
    }
    .master-unlock { 
        background-color: #ecfdf5; 
        color: #10a37f; 
        font-weight: bold; 
        border: 1px solid #10a37f; 
        padding: 10px; 
        border-radius: 8px; 
        text-align: center; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CONFIGURATION & MASTER LOGIC ---
UPI_ID = "9665145228-2@axl"
PAYEE_NAME = "Neo AI Creator"

def get_upi_link(amount, note):
    return f"upi://pay?pa={UPI_ID}&pn={PAYEE_NAME}&am={amount}&cu=INR&tn={note}"

with st.sidebar:
    st.title("Neo v3.0 🚀")
    user_name = st.text_input("Identify Yourself", placeholder="Name")
    master_key = st.text_input("Master Key", type="password", placeholder="Secret Key")
    
    is_master = False
    if master_key == "NEO_MASTER_2026":
        is_master = True
        st.markdown('<div class="master-unlock">🔓 MASTER ACCESS ACTIVE</div>', unsafe_allow_html=True)
    
    st.markdown("---")
    if st.button("➕ New Session"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("📞 **Direct Support**")
    st.markdown(f'<a href="tel:9665145228" class="buy-btn" style="text-align:center;">Call Creator</a>', unsafe_allow_html=True)

# --- 3. MAIN APP INTERFACE ---
if not user_name:
    st.title("Welcome to Neo Intelligence")
    st.subheader("The World's Most Advanced AI Personal Assistant.")
    st.write("Please enter your name in the sidebar to unlock the beast.")
    st.image("https://images.unsplash.com/photo-1620712943543-bcc4628c9757?auto=format&fit=crop&q=80&w=1000")
else:
    if "messages" not in st.session_state: st.session_state.messages = []
    
    tab1, tab2, tab3 = st.tabs(["🗨️ Unlimited Chat", "💎 Premium Store", "📊 Trends"])

    # --- CHAT TAB ---
    with tab1:
        st.markdown(f"### Neo Intelligence | Active: {user_name}")
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
        
        if prompt := st.chat_input("Ask Neo anything..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                if is_master:
                    response = "Master, I have scanned all secure databases. Here is your privileged information..."
                else:
                    response = "I am processing your request. For real-time future predictions, consider Neo Pro."
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

    # --- STORE TAB (UPI REDIRECT) ---
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
