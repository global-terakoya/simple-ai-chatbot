# simple-ai-chatbot

Super simple AI chatbot examples using LangChain and Chainlit.

| Version | Text response | Web UI | Memory | User session | Image gen. | Web Search |  
| :-----: | :-----------: | :----: | :----: | :----------: | :--------: | :--------: |
|  v0.1   |       ✅       |        |        |             |            |            |
|  v0.2   |       ✅       |   ✅    |        |             |            |            |
|  v0.3   |       ✅       |   ✅    |   ✅    |            |            |            |
|  v0.4   |       ✅       |   ✅    |   ✅    |      ✅     |           |            |
|  v0.5   |       ✅       |   ✅    |   ✅    |      ✅     |     ✅     |            |
|  v0.6   |       ✅       |   ✅    |   ✅    |      ✅     |     ✅     |     ✅     |

# Setup

## DevContainer

```bash
echo "OPENAI_API_KEY=<your-key>" >> .secrets
```

## Local

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "OPENAI_API_KEY=<your-key>" >> .secrets
```

# Run

For v01, you can run the chatbot with the following command.

```bash
python src/chatbot_v01.py
```

For v02 to v05, you can run the chatbots with the following command.

```bash
chainlit run src/chatbot_v0[2-5].py
```

# References

- [Chainlit](https://github.com/chainlit/chainlit)
- [LangChain](https://github.com/langchain-ai/langchain)
