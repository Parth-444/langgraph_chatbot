from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
import os
import sqlite3

key = os.getenv('GOOGLE_API_KEY_PRO')
llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", api_key=key)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    message = state['messages']
    response = llm.invoke(message)
    return {"messages": [response]}

conn = sqlite3.connect("chatbot.db", check_same_thread=False)

checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer)

def retrieve_all_threads():
    all_threads_set = set()
    for checkpoints in checkpointer.list(None):
        all_threads_set.add(checkpoints[0]['configurable']['thread_id'])
    return list(all_threads_set)