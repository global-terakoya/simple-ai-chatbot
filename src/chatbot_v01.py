from dotenv import load_dotenv
load_dotenv()
load_dotenv('.secrets')

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")


while True:
    input_text = input("Enter a message: ")
    if input_text == "exit":
        break
    response = llm.invoke([
        ("human", input_text)
    ])
    print(response.content)