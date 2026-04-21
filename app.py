import streamlit as st
import time
import google.generativeai as genai

# --- 1. CONFIG & THEME ---
st.set_page_config(page_title="Neo AI - SaaS Edition", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .stChatMessage { border-radius: 12px; margin-bottom: 10px; border: 1px solid #F3F4F6; }
    .auth-box { max-width: 400px; margin: auto; padding: 30px; border: 1px solid #EEE; border-radius: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    .btn-buy { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .thumb-preview { border: 2px dashed #D1D5DB; border-radius: 10px; padding: 20px; text-align: center; background: #F9FAFB; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. INITIALIZE DATABASE ---
if "auth" not in st.session_state: st.session_state.auth = False
if "thumbs_left" not in st.session_state: st.session_state.thumbs_left = 3
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# --- 3. LOGIN / OTP SYSTEM ---
def show_login():
    st.markdown("<div class='auth-box'>", unsafe_allow_html=True)
    st.title("🔐 Neo Secure Access")
    email = st.text_input("Email ID", placeholder="example@gmail.com")
    password = st.text_input("Set Password", type="password")
    otp = st.text_input("OTP (Sent to Email)", placeholder="Enter 4-digit OTP")
    
    if st.button("Verify & Enter Neo"):
        if email and len(password) >= 6 and otp == "1234": # Demo OTP '1234'
            st.session_state.auth = True
            st.session_state.user_email = email
            st.rerun()
        else:
            st.error("Invalid Details. Use OTP: 1234")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 4. MAIN BEAST APP ---
if not st.session_state.auth:
    show_login()
else:
    # --- Sidebar ---
    with st.sidebar:
        st.title("Neo v5.0 Pro 🚀")
        st.write(f"👤 User: **{st.session_state.user_email}**")
        st.markdown(f'<span class="premium-badge">FREE THUMBNAILS: {st.session_state.thumbs_left}</span>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🔴 Logout"):
            st.session_state.auth = False
            st.rerun()
        st.write("💰 **UPI:** `9665145228-2@axl`")

    tab1, tab2, tab3 = st.tabs(["🗨️ GPT Streaming Chat", "🎥 Thumbnail Generator", "💎 Premium Access"])

    # --- TAB 1: STREAMING CHAT (GPT STYLE) ---
    with tab1:
        st.subheader("Neo Deep Intelligence")
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]): st.markdown(chat["content"])
        
        if prompt := st.chat_input("Ask anything to the Beast..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                # Simulation of Gemini Response with Step-by-Step Flow
                full_text = f"""### 🚀 THE CORE ROADMAP
                Aapka sawal "{prompt}" bahut interesting hai. Neo iska deep analysis kar raha hai:

                1. **Market Fact:** Is topic par abhi competition low hai aur demand 45% up hai.
                2. **Execution:** Sabse pehle aapko data collect karke execution start karni hogi.
                3. **Scaling:** Neo API use karke aap ise 10x scale kar sakte hain.

                🏁 **NEXT MOVE:** Thumbnail tab mein jaakar ek viral image generate karein!"""
                
                placeholder = st.empty()
                typed_msg = ""
                # Word-by-word streaming effect
                for word in full_text.split(" "):
                    typed_msg += word + " "
                    placeholder.markdown(typed_msg + "▌")
                    time.sleep(0.07)
                placeholder.markdown(typed_msg)
                st.session_state.chat_history.append({"role": "assistant", "content": typed_msg})

    # --- TAB 2: THUMBNAIL MAKER (FREE LIMIT) ---
    with tab2:
        st.subheader("🖼️ YouTube Viral Thumbnail Maker")
        topic = st.text_input("Video Topic / Title", placeholder="Ex: Earn 1 Lakh with AI")
        
        if st.button("Generate AI Thumbnail"):
            if st.session_state.thumbs_left > 0:
                with st.spinner("Neo Beast is designing..."):
                    time.sleep(2.5)
                    st.session_state.thumbs_left -= 1
                    st.image("https://images.unsplash.com/photo-1626785774573-4b799315345d?q=80&w=800", 
                             caption=f"Preview for: {topic}")
                    st.success(f"Success! {st.session_state.thumbs_left} free generations left.")
            else:
                st.error("Free Limit Exhausted! Please upgrade for 15+ thumbnails.")

    # --- TAB 3: SUBSCRIPTION & PRO ---
    with tab3:
        st.subheader("💎 Unlock Unlimited Beast Potential")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""<div class='auth-box'>
                <h3>Pro Access</h3>
                <p>✅ 15+ Thumbnails</p>
                <p>✅ Real-time Trends</p>
                <h2 style='color:#10a37f;'>₹49 / Month</h2>
                </div>""", unsafe_allow_html=True)
            upi_link = "upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoProAccess"
            st.markdown(f'<a href="{upi_link}" class="btn-buy">Buy via UPI App</a>', unsafe_allow_html=True)
            
        with col2:
            st.info("💡 **Kaise kaam karega?**\n\nPayment karne ke baad Neo Pro apne aap detect nahi hoga (kyunki ye direct UPI hai). Aapko 'Call Creator' par click karke screenshot dena hoga, aur main aapko ek **Permanent Master Key** de dunga.")
        
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
