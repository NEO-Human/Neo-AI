import streamlit as st
import time
import random
import google.generativeai as genai

# --- 1. CONFIG & BEAST THEME ---
st.set_page_config(page_title="Neo AI - SaaS Beast", page_icon="🛡️", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF; }
    .auth-container { max-width: 450px; margin: auto; padding: 30px; border-radius: 15px; border: 1px solid #EEE; box-shadow: 0 10px 25px rgba(0,0,0,0.05); }
    .stChatMessage { border-radius: 12px; margin-bottom: 10px; border: 1px solid #F3F4F6; }
    .btn-buy { display: block; background: #000; color: white !important; padding: 12px; border-radius: 8px; text-align: center; text-decoration: none; font-weight: bold; margin-top: 15px; }
    .premium-badge { color: #10a37f; font-weight: bold; border: 1px solid #10a37f; padding: 4px 12px; border-radius: 20px; font-size: 13px; }
    .journey-card { background: #f8f9fa; border-radius: 10px; padding: 15px; border-left: 5px solid #000; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATABASE INITIALIZATION ---
if "auth_step" not in st.session_state: st.session_state.auth_step = "email_entry"
if "generated_otp" not in st.session_state: st.session_state.generated_otp = None
if "user_email" not in st.session_state: st.session_state.user_email = ""
if "thumbs_left" not in st.session_state: st.session_state.thumbs_left = 3
if "chat_history" not in st.session_state: st.session_state.chat_history = []

# --- 3. THE SECURE AUTH GATEWAY ---
def show_auth_gate():
    st.markdown("<div class='auth-container'>", unsafe_allow_html=True)
    st.title("🛡️ Neo Secure Access")
    
    # STEP 1: Email Entry
    if st.session_state.auth_step == "email_entry":
        email = st.text_input("Enter your Email", placeholder="example@gmail.com")
        if st.button("Send Verification Code"):
            if "@" in email and "." in email:
                st.session_state.generated_otp = str(random.randint(1000, 9999))
                st.session_state.user_email = email
                st.session_state.auth_step = "otp_verify"
                st.rerun()
            else:
                st.error("Please enter a valid email.")

    # STEP 2: OTP Verification
    elif st.session_state.auth_step == "otp_verify":
        st.info(f"Verification code sent to: {st.session_state.user_email}")
        # Simulation: Real world me ye email par jayega
        st.warning(f"DEV NOTE: Your Random OTP is **{st.session_state.generated_otp}**")
        
        otp_in = st.text_input("Enter 4-Digit Code", placeholder="XXXX")
        if st.button("Verify OTP"):
            if otp_in == st.session_state.generated_otp:
                st.session_state.auth_step = "set_password"
                st.rerun()
            else:
                st.error("Wrong Code! Try again.")

    # STEP 3: Password Setup
    elif st.session_state.auth_step == "set_password":
        st.subheader("Set Your Password")
        p1 = st.text_input("Create Password", type="password")
        p2 = st.text_input("Confirm Password", type="password")
        
        if st.button("Complete Registration"):
            if len(p1) >= 6 and p1 == p2:
                st.session_state.auth_step = "verified"
                st.success("Account Created Successfully!")
                time.sleep(1.5)
                st.rerun()
            else:
                st.error("Passwords must match and be at least 6 characters.")

    st.markdown("</div>", unsafe_allow_html=True)

# --- 4. MAIN BEAST APPLICATION CONTENT ---
if st.session_state.auth_step != "verified":
    show_auth_gate()
else:
    # --- Sidebar ---
    with st.sidebar:
        st.title("Neo v6.5 Pro 🚀")
        st.write(f"Logged in: **{st.session_state.user_email}**")
        st.markdown(f'<span class="premium-badge">FREE CREDITS: {st.session_state.thumbs_left}</span>', unsafe_allow_html=True)
        st.markdown("---")
        if st.button("🔴 Logout"):
            st.session_state.auth_step = "email_entry"
            st.rerun()
        st.write("💰 **UPI ID:** `9665145228-2@axl`")

    tab1, tab2, tab3, tab4 = st.tabs(["🗨️ Beast Chat", "🖼️ AI Thumbnail", "📈 Creator Roadmap", "💎 Buy Pro"])

    # --- TAB 1: STREAMING CHAT ---
    with tab1:
        st.subheader("Real-time Intelligence")
        for chat in st.session_state.chat_history:
            with st.chat_message(chat["role"]): st.markdown(chat["content"])
        
        if prompt := st.chat_input("Ask the Beast..."):
            st.session_state.chat_history.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            
            with st.chat_message("assistant"):
                full_text = f"### 🚀 BEAST ANALYSIS\n\n1. **Fact:** {prompt} niche is growing at 25% weekly.\n2. **Strategy:** Stop researching, start executing. Focus on the first 3 seconds of your content.\n3. **Next Move:** Use the 'Creator Roadmap' tab for scaling."
                placeholder = st.empty()
                typed_msg = ""
                for word in full_text.split(" "):
                    typed_msg += word + " "
                    placeholder.markdown(typed_msg + "▌")
                    time.sleep(0.06)
                placeholder.markdown(typed_msg)
                st.session_state.chat_history.append({"role": "assistant", "content": typed_msg})

    # --- TAB 2: THUMBNAIL MAKER ---
    with tab2:
        st.subheader("🎥 Viral Thumbnail Generator")
        topic = st.text_input("Thumbnail Topic", placeholder="Ex: Master AI in 10 Minutes")
        if st.button("Generate"):
            if st.session_state.thumbs_left > 0:
                with st.spinner("Neo is designing..."):
                    time.sleep(2)
                    st.session_state.thumbs_left -= 1
                    st.image("https://images.unsplash.com/photo-1611162617474-5b21e879e113?q=80&w=800")
                    st.success(f"Success! {st.session_state.thumbs_left} credits left.")
            else:
                st.error("Limit Exhausted! Upgrade to Pro.")

    # --- TAB 3: CREATOR JOURNEY ---
    with tab3:
        st.subheader("📈 YouTube & Instagram Blueprint")
        st.markdown("""
        <div class="journey-card">
        <h4>Level 1: The Setup (0-100 Followers)</h4>
        <p>Focus on: Bio optimization and 1 consistent niche. Use Neo Chat to find your 'Viral Hook'.</p>
        </div>
        <div class="journey-card">
        <h4>Level 2: The Viral Loop (100-10K)</h4>
        <p>Focus on: High-CTR Thumbnails and Storytelling. Don't post without checking Neo Trends.</p>
        </div>
        """, unsafe_allow_html=True)
        st.warning("Phase 3: 'Monetization Secrets' is locked for Free users.")

    # --- TAB 4: UPGRADE ---
    with tab4:
        st.subheader("💎 Unlock Unlimited Power")
        st.write(f"Account: {st.session_state.user_email}")
        st.markdown("""
        - ✅ **15+ AI Thumbnails Monthly**
        - ✅ **Full Monetization Roadmap**
        - ✅ **Priority Support & Master Key**
        - ✅ **Zero Login required after first verification**
        """)
        upi_link = f"upi://pay?pa=9665145228-2@axl&pn=NeoAI&am=49&cu=INR&tn=NeoPro_{st.session_state.user_email}"
        st.markdown(f'<a href="{upi_link}" class="btn-buy">Buy 15 Access - ₹49</a>', unsafe_allow_html=True)
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
