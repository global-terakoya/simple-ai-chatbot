from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
import chainlit as cl

load_dotenv()
load_dotenv('.secrets')

llm = ChatOpenAI(model="gpt-4o-mini")


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("message_history", ChatMessageHistory())
    await cl.Message(
        content="Hello, what can I help you with today?",
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.add_user_message(message.content)
    response = llm.invoke(message_history.messages)
    message_history.add_ai_message(response.content)
    await cl.Message(content=response.content).send()
