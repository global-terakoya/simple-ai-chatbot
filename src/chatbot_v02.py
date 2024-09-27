from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import chainlit as cl

load_dotenv()
load_dotenv('.secrets')

llm = ChatOpenAI(model="gpt-4o-mini")


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(
        content="Hello, what can I help you with today?",
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    response = llm.invoke([
        ("human", message.content)
    ])
    await cl.Message(content=response.content).send()