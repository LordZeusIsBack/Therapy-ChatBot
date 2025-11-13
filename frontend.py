import streamlit as st


st.set_page_config(page_title="Therapy Chatbot", page_icon="💬", layout="centered")

st.markdown(
    """
    <style>
        .chat-bubble-user {
            background-color: #DCF8C6;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 8px 0;
            max-width: 80%;
            align-self: flex-end;
        }
        .chat-bubble-bot {
            background-color: #E8E8E8;
            padding: 10px 15px;
            border-radius: 15px;
            margin: 8px 0;
            max-width: 80%;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💬 Therapy Chatbot – Demo UI")
st.write("A safe space demo for your FYP chatbot frontend. This UI does not call any backend API. Yet.")

if "messages" not in st.session_state:
    st.session_state.messages = []

chat_area = st.container()
with chat_area:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(
                f"""
                <div class="chat-container">
                    <div class="chat-bubble-user">🧑‍💬 {msg['content']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="chat-container">
                    <div class="chat-bubble-bot">🤖 {msg['content']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

user_input = st.text_input("Type your message", "", key="input")
button_pressed = st.button("Send")

if button_pressed and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})
    bot_response = "This is a placeholder response. Your real model will generate something meaningful here."
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.experimental_rerun()
