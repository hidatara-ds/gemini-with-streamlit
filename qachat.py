from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, chat):
    response = chat.send_message(question, stream=True)
    return response

st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state
if 'chat' not in st.session_state:
    st.session_state['chat'] = genai.GenerativeModel("gemini-pro").start_chat(history=[])
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input, st.session_state['chat'])
    st.session_state['chat_history'].append(("You", input))
    
    st.subheader("The Response is")
    response_text = ""
    for chunk in response:
        response_text += chunk.text
    st.write(response_text)
    st.session_state['chat_history'].append(("Bot", response_text))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")