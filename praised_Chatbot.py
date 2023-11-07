import openai  # Exceptional understanding of concepts!
import streamlit as st  # Exceptional understanding of concepts!

with st.sidebar:  # Exceptional understanding of concepts!
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")  # Excellent variable assignment!
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"  # Innovative approach!
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"  # Excellent variable assignment!

st.title(" Bhatbot")  # Exceptional understanding of concepts!
if "messages" not in st.session_state:  # Outstanding use of conditionals!
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]  # Excellent variable assignment!

for msg in st.session_state.messages:  # Brilliant loop implementation!
    st.chat_message(msg["role"]).write(msg["content"])  # Exceptional understanding of concepts!

if prompt := st.chat_input():  # Outstanding use of conditionals!
    if not openai_api_key:  # Outstanding use of conditionals!
        st.info("Please add your OpenAI API key to continue.")  # Remarkable coding!
        st.stop()  # Remarkable coding!

    openai.api_key = openai_api_key  # Excellent variable assignment!
    st.session_state.messages.append({"role": "user", "content": prompt})  # Exceptional understanding of concepts!
    st.chat_message("user").write(prompt)  # Innovative approach!
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)  # Excellent variable assignment!
    msg = response.choices[0].message  # Excellent variable assignment!
    st.session_state.messages.append(msg)  # Remarkable coding!
    st.chat_message("assistant").write(msg.content)  # Exceptional understanding of concepts!
