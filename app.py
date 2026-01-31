import streamlit as st
import time
from openai import OpenAI

# Page Config
st.set_page_config(page_title="AI Professional Writing Assistant", page_icon="✍️", layout="centered")

# --- Session State Initialization ---
if "credits" not in st.session_state:
    st.session_state.credits = 3
if "page" not in st.session_state:
    st.session_state.page = "landing"

# --- Functions ---

def show_landing_page():
    st.title("Welcome to AI Professional Writing Assistant ✍️")
    st.subheader("Elevate your writing with the power of AI.")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Why use us?
        - ✨ **Instant Polish**: Turn rough drafts into professional emails.
        - 🎭 **Tone Adjustment**: Switch between Friendly, Professional, and Persuasive.
        - 🚀 **Powered by GPT-4o**: State-of-the-art AI model.
        """)
    
    with col2:
        st.info("Start with 3 FREE credits when you join!")
        if st.button("Login / Get Started 🚀", type="primary"):
            st.session_state.page = "app"
            st.rerun()

def show_main_app():
    # --- Sidebar ---
    st.sidebar.header("Account Info")
    st.sidebar.subheader(f"Credits Remaining: {st.session_state.credits}")
    st.sidebar.info("Each generation costs 1 credit.")
    
    if st.sidebar.button("Logout"):
        st.session_state.page = "landing"
        st.rerun()

    # --- Main Interface ---
    st.title("✍️ AI Professional Writing Assistant")
    st.write("Refine your draft with professional AI editing.")

    # Text Input
    user_input = st.text_area("Enter your draft or topic here...", height=150)

    # Tone Selection
    tone = st.selectbox("Select Tone", ["Professional", "Friendly", "Persuasive"])

    # --- Logic & Buttons ---
    try:
        api_key = st.secrets.get("OPENAI_API_KEY")
    except Exception:
        api_key = None

    if api_key:
        client = OpenAI(api_key=api_key)

        # 1. GENERATE BUTTON (Visible if Credits > 0)
        if st.session_state.credits > 0:
            if st.button("Generate ✨", type="primary"):
                if not user_input.strip():
                    st.warning("Please enter some text first.")
                else:
                    with st.spinner("Polishing your text..."):
                        try:
                            system_prompt = f"You are an expert copywriter. Rewrite the user's text to match the selected tone: {tone}."
                            response = client.chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[
                                    {"role": "system", "content": system_prompt},
                                    {"role": "user", "content": user_input}
                                ]
                            )
                            result = response.choices[0].message.content
                            
                            # Save result and deduct credit
                            st.session_state.last_result = result
                            st.session_state.credits -= 1
                            st.rerun()
                            
                        except Exception as e:
                            st.error(f"API Error: {e}")

        # 2. BUY BUTTON (Visible if Credits == 0)
        else:
            st.error("You have run out of credits!")
            if st.button("Buy 10 Credits for $4.99 💳"):
                with st.spinner("Processing payment..."):
                    time.sleep(1.5) # Simulate payment delay
                    st.session_state.credits = 10
                    st.balloons()
                    st.success("Purchase successful! 10 Credits added.")
                    time.sleep(1)
                    st.rerun()

        # 3. Display Result (if exists)
        if "last_result" in st.session_state:
             st.divider()
             st.subheader("Your Refined Text:")
             st.markdown(f"> {st.session_state.last_result}")

    else:
        st.warning("⚠️ OpenAI API Key is missing. Please set `OPENAI_API_KEY` in `.streamlit/secrets.toml`.")

# --- Routing ---
if st.session_state.page == "landing":
    show_landing_page()
else:
    show_main_app()
