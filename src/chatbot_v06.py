from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain.agents import Tool
from langgraph.prebuilt import create_react_agent
import chainlit as cl
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper  # Add this import

load_dotenv()
load_dotenv('.secrets')




def generate_image(prompt):
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url


dalle_tool = Tool(
    name="DALL-E",
    func=generate_image,
    description="Generate an image based on a given prompt."
)


search = DuckDuckGoSearchAPIWrapper()
web_search_tool = Tool(
    name="Web-Search",
    func=search.run,
    description="Search the web for current information on a given topic."
)

llm = ChatOpenAI(model="gpt-4o-mini")

graph = create_react_agent(llm, [dalle_tool, web_search_tool])


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("message_history", ChatMessageHistory())
    await cl.Message(
        content="Hello, what can I help you with today?"
    ).send()


@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    message_history.add_user_message(message.content)
    response = graph.invoke({
        'messages': message_history.messages,
    })
    response_message = response['messages'][-1].content
    message_history.add_ai_message(response_message)
    await cl.Message(content=response_message).send()