from dotenv import load_dotenv
load_dotenv()  # Load environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure Gemini AI API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Gemini model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])  # Initialize chat history for the model

def get_gemini_response(question):
    """
    Sends a message to Gemini model and retrieves a response.
    """
    response = chat.send_message(question)  # Send question to the model
    return response  # Return response from the model

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Chatbot", layout="wide")

# CSS for chat styling
st.markdown(
    """
    <style>
    .chat-history {
        max-height: 500px;
        overflow-y: auto;
        padding: 10px;
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        border-radius: 5px;
    }
    .user-message {
        background-color: #e9ecef;
        color: #000;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        text-align: left;
    }
    .bot-message {
        background-color: #d1e7ff;
        color: #000;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        text-align: left;
    }
    .input-box {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title of the chatbot
st.title("Gemini LLM Chatbot")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Function to handle input and get AI response
def handle_input():
    """
    Handles user input, sends it to the model, and updates the chat history.
    """
    user_input = st.session_state.temp_input.strip()
    if user_input:
        # Add user input to chat history
        st.session_state.chat_history.append(("You", user_input))
        
        # Send input to Gemini model and get response
        response = get_gemini_response(user_input)
        
        # Extract AI response
        bot_response = ""
        for chunk in response:
            bot_response += chunk.text
        
        # Add bot response to chat history
        st.session_state.chat_history.append(("Bot", bot_response))
        
        # Clear the input box
        st.session_state.temp_input = ""

# Chat history display
st.markdown("### Chat History")
st.markdown('<div class="chat-history">', unsafe_allow_html=True)
for role, text in st.session_state["chat_history"]:
    if role == "You":
        st.markdown(f'<div class="user-message"><b>{role}:</b> {text}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message"><b>{role}:</b> {text}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Input box at the bottom
st.markdown('<div class="input-box">', unsafe_allow_html=True)
st.text_input("Type your message:", key="temp_input", on_change=handle_input, label_visibility="collapsed")
st.markdown("</div>", unsafe_allow_html=True)
