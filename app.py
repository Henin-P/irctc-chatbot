import streamlit as st
import ollama

# Page settings
st.set_page_config(
    page_title="IRCTC Chatbot",
    page_icon="🚆",
    layout="centered"
)

# Title
st.title("🚆 IRCTC Chatbot")
st.write("Ask your railway queries here.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask your question...")

if user_input:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send to DeepSeek model
    response = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=[
            {
                'role': 'system',
                'content': 'You are an IRCTC customer care chatbot. Answer politely.'
            },
            {
                'role': 'user',
                'content': user_input
            }
        ]
    )

    bot_reply = response['message']['content']

    # Show bot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save bot response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )