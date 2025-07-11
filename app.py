import streamlit as st
import webbrowser

BUSINESS_INFO = {
    "working hours": "Monday–Friday, 9:00 AM – 6:00 PM",
    "location": "Yashnabad, Tashkent, Uzbekistan",
    "phone number": "+998 71 200 00 01",
    "email": "contact@alijontech.uz"
}


GITHUB_ISSUES_URL = "https://github.com/Alijon-Musaev/alijon-tech-assistant/issues/new"


st.set_page_config(page_title="Alijon's Tech Clinic Assistant", layout="centered")
st.title("🤖 Welcome to Alijon's Tech Clinic Assistant")
st.write("Ask me anything about our clinic — location, working hours, contact info, etc.")


user_question = st.text_input("💬 Your question:")

def answer_question(q):
    q = q.lower()
    for key in BUSINESS_INFO:
        if key in q:
            return BUSINESS_INFO[key]
    return None

if user_question:
    response = answer_question(user_question)
    if response:
        st.success(f"📍 {response}")
    else:
        st.warning("I couldn't find the answer. Would you like to open a support ticket?")
        if st.button("📩 Open Support Ticket"):
            webbrowser.open_new_tab(GITHUB_ISSUES_URL)
