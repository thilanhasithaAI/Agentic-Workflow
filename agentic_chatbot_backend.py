from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver

load_dotenv()  # Load environment variables from .env file

llm = ChatOpenAI()

# defining  the convosationsal states
from langgraph.graph.message import add_messages

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state:ChatState):

    #take the user query from state
    messages = state['messages']

    #passing to the llm 
    response = llm.invoke(messages)

    #response store state
    return {'messages':[response]}

checkpoint = MemorySaver()  # memory is store inside the RAM

# define the graph

graph = StateGraph(ChatState)

# add nodes to the graph
graph.add_node('chat_node',chat_node)

# edge connection
graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpoint)



