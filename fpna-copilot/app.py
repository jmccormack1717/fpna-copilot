import streamlit as st
from agent import tools

st.set_page_config(page_title="CFO Copilot", layout="wide")

st.title("💼 CFO Copilot")
st.write("Ask me about revenue vs budget, gross margin %, opex, or cash runway.")

# Chat input
question = st.chat_input("Ask your CFO question...")

if question:
    st.write(f"**Q:** {question}")

    response_text, chart = tools.handle_question(question)

    # Display text response
    st.write(response_text)

    # Display chart if available
    if chart is not None:
        st.pyplot(chart)
