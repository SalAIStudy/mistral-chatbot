import streamlit as st
from app.chatbot import ChatBot


st.set_page_config(
    page_title="Codestral Chatbot",
    page_icon="💻"
)

st.title("💻 Codestral AI Assistant")

# initialize bot
if "bot" not in st.session_state:
    st.session_state.bot = ChatBot()

# initialize history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display old messages
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# input box
prompt = st.chat_input("Ask coding questions...")

if prompt:

    # show user msg
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # get response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.bot.get_response(prompt)

            st.markdown(response)

    # save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })