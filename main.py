import os
import streamlit as st
from anthropic import Anthropic

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic()

def generate_response(prompt):
    
    message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=1000,
    temperature=0,
    system="You are a world-class physician. Respond only with friendly, helpful, evidenced based medical advice.",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f'{prompt}'
                }
            ]
        }
      ]
    )
    return message.content.strip()

def main():
    st.set_page_config(page_title="Doctor AI Chat", page_icon=":stethoscope:", layout="wide")

    # Custom CSS styles
    st.markdown(
        """
        <style>
        .chat-container {
            display: flex;
            flex-direction: column;
            height: 100vh;
            padding: 20px;
        }
        .chat-header {
            text-align: center;
            margin-bottom: 20px;
        }
        .chat-history {
            flex-grow: 1;
            overflow-y: auto;
            margin-bottom: 20px;
        }
        .user-message {
            background-color: #e6e6e6;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .assistant-message {
            background-color: #d9d9d9;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .input-container {
            display: flex;
        }
        .input-container input {
            flex-grow: 1;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        .input-container button {
            padding: 10px 20px;
            border-radius: 5px;
            background-color: #4CAF50;
            color: white;
            border: none;
            margin-left: 10px;
            cursor: pointer;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Chat interface
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown('<div class="chat-header"><h1>Doctor AI Chat</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="chat-history">', unsafe_allow_html=True)

    chat_history = []
    user_input = st.text_input("You:", key="user_input")

    if st.button("Send"):
        chat_history.append(("user", user_input))
        prompt = "\n".join([f"{role}: {message}" for role, message in chat_history])
        response = generate_response(prompt)
        chat_history.append(("assistant", response))

    for role, message in chat_history:
        if role == "user":
            st.markdown(f'<div class="user-message">{message}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-message">{message}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.warning("Please note that this is a basic assessment and not a substitute for professional medical advice. Always consult a qualified healthcare provider for accurate diagnosis and treatment.")

if __name__ == "__main__":
    main()
