import streamlit as st
import time
import google.generativeai as genai

# --- 1. CONFIG & BEAST THEME ---
st.set_page_config(page_title="Neo AI - Secure SaaS", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .auth-container { max-width: 500px; margin: auto; padding: 40px; border-radius: 20px; border: 1px solid #EEE; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; }
    .stChatMessage { border-radius: 12px; margin-bottom: 10px; }
    .btn-buy { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATABASE INITIALIZATION ---
if "is_verified" not in st.session_state: st.session_state.is_verified = False
if "otp_sent" not in st.session_state: st.session_state.otp_sent = False
if "thumbs_left" not in st.session_state: st.session_state.thumbs_left = 3
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# --- 3. SECURE AUTHENTICATION SYSTEM ---
def show_auth_gate():
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    st.title("🛡️ Neo Secure Login")
    st.write("One Email. One Account. Unlimited Beast Power.")
    
    email = st.text_input("Enter your Email", placeholder="yourname@gmail.com")
    
    if email:
        if not st.session_state.otp_sent:
            if st.button("Generate & Send OTP"):
                # Yahan hum OTP send karne ka simulation kar rahe hain
                with st.spinner("Sending OTP to " + email + "..."):
                    time.sleep(1.5)
                    st.session_state.otp_sent = True
                    st.success("OTP Sent! Check your inbox (Demo: 1234)")
                    st.rerun()
        
        if st.session_state.otp_sent:
            otp_input = st.text_input("Enter 4-Digit OTP", placeholder="1234")
            password = st.text_input("Set Account Password", type="password")
            
            if st.button("Verify & Access Neo"):
                if otp_input == "1234" and len(password) >= 6:
                    st.session_state.is_verified = True
                    st.session_state.user_email = email
                    st.success("Authentication Successful!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("Invalid OTP or Password too short.")
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- 4. MAIN APP CONTENT ---
if not st.session_state.is_verified:
    show_auth_gate()
else:
    # --- Sidebar ---
    with st.sidebar:
        st.title("Neo v5.5 Pro 🚀")
        st.write(f"Logged in as: **{st.session_state.user_email}**")
        st.markdown(f'<span class="premium-badge">FREE THUMBNAILS: {st.session_state.thumbs_left}</span>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🔴 Logout / Switch Account"):
            st.session_state.is_verified = False
            st.session_state.otp_sent = False
            st.rerun()
        st.write("💰 **UPI:** `9665145228-2@axl`")

    tab1, tab2, tab3 = st.tabs(["🗨️ Beast Chat", "🖼️ Thumbnail Maker", "💎 Buy 15+ Access"])

    # --- TAB 1: STREAMING CHAT ---
    with tab1:
        st.subheader("Real-time AI Intelligence")
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]): st.markdown(chat["content"])
        
        if prompt := st.chat_input("Ask Neo for a Step-by-Step Roadmap..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                full_text = f"""### 🚀 THE BEAST STRATEGY
                Aapka sawal "{prompt}" process ho gaya hai.
                
                1. **Facts:** Yeh topic market mein top 5% trends mein hai.
                2. **How-to:** Pehle account setup karein, phir Neo tools se automation lagayein.
                3. **Next Move:** Thumbnail generate karke launch karein!"""
                
                placeholder = st.empty()
                typed_msg = ""
                for word in full_text.split(" "):
                    typed_msg += word + " "
                    placeholder.markdown(typed_msg + "▌")
                    time.sleep(0.07)
                placeholder.markdown(typed_msg)
                st.session_state.chat_history.append({"role": "assistant", "content": typed_msg})

    # --- TAB 2: THUMBNAIL GENERATOR ---
    with tab2:
        st.subheader("🎥 Viral Thumbnail Generator")
        topic = st.text_input("Thumbnail Topic", placeholder="Ex: Earn money while sleeping")
        
        if st.button("Generate Thumbnail"):
            if st.session_state.thumbs_left > 0:
                with st.spinner("Beast is designing..."):
                    time.sleep(2)
                    st.session_state.thumbs_left -= 1
                    st.image("https://images.unsplash.com/photo-1626785774573-4b799315345d?q=80&w=800")
                    st.success(f"Generated! {st.session_state.thumbs_left} free left.")
            else:
                st.error("Limit Reached! Buy Pro for 15+ thumbnails.")

    # --- TAB 3: UPGRADE ---
    with tab3:
        st.subheader("💎 Unlock Unlimited Potential")
        st.write("Current Email: " + st.session_state.user_email)
        st.markdown("""
        - ✅ 15+ Viral Thumbnails
        - ✅ Priority GPT-4o Access
        - ✅ Market Trends Database
        """)
        upi_link = f"upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoPro_{st.session_state.user_email}"
        st.markdown(f'<a href="{upi_link}" class="btn-buy">Buy 15 Access - ₹49</a>', unsafe_allow_html=True)
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
