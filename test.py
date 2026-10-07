# from agentic_chatbot_backend import chatbot
# from langchain_core.messages import BaseMessage, HumanMessage


# CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# # Not adding streaming features

# # response = chatbot.invoke({'messages': [HumanMessage(content="what is python?")]},config=CONFIG)
# # print(response['messages'][-1].content) 

# # After adding streaming features

# # for message_chunk,metadata in chatbot.stream(
# #     {'messages': [HumanMessage(content="Generate a blog about Machine Learning?")]},
# #     config=CONFIG,
# #     stream_mode = "message"):
    
# #     if message_chunk.content:
# #         print(message_chunk.content, end="", flush=True)



# response = chatbot.invoke(
#     {'messages': [HumanMessage(content="what is python?")]},
#     config=CONFIG
# )

# print(response['messages'][-1].content)


from agentic_chatbot_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {
    'configurable': {
        'thread_id': 'thread-1'
    }
}

print("Starting streaming...")

for message_chunk, metadata in chatbot.stream(
    {
        'messages': [
            HumanMessage(content="Generate a blog about Machine Learning?")
        ]
    },
    config=CONFIG,
    stream_mode="messages"
):
    print("CHUNK:", message_chunk)
    print("CONTENT:", message_chunk.content)

print("Streaming finished!")
