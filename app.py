from agentic_chatbot_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage
import streamlit as st

# thread_id = "1"
# config  = {'configurable':{'thread_id':thread_id}}

# response = chatbot.invoke({'messages': [HumanMessage(content="what is python?")]}, config=config)
# print(response['messages'][-1].content)

st.title(" Agentic Chatbot with LangGraph")

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

## add the session state to reducing the erase the previous chat

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversational memory from the session state
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])






user_input = st.chat_input("Ask Anything:")

if user_input:

    #first add the msg to the msg history
    st.session_state['message_history'].append({"role": "user", "content": user_input})

    # Display user message in chat message container
    with st.chat_message("user"):
        st.text(user_input)

    # Get response from chatbot
    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response['messages'][-1].content

    #first add the msg to the msg history
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.text(ai_message)
