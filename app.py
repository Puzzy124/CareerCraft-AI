
import streamlit as st
from mentor_engine import get_career_advice

st.set_page_config(page_title="AI Career Mentor", layout="centered")
st.title("💼 AI Career Mentor")

st.sidebar.header("Select Domain")
domain = st.sidebar.selectbox("Career Domain", ["Data Science", "Cloud Engineering", "Cybersecurity"])

st.subheader("Ask Your Career Question")
user_query = st.text_area("Type your question here:")

if st.button("Get Advice"):
    if user_query:
        response = get_career_advice(domain, user_query)
        st.markdown("### 🧠 Career Advice")
        st.write(response)
    else:
        st.warning("Please enter a question.")
