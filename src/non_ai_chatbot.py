import random
import re

# Dictionary of pre-defined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm great! How about you?", "All good here!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "name": ["My name is ChatBot. Nice to meet you!", "I'm ChatBot. What's your name?"],
    "weather": ["I'm not able to check the weather, but I hope it's nice outside!", "Why don't you look out the window and tell me?"],
    "default": ["Interesting. Tell me more.", "I'm not sure I understand. Can you rephrase that?", "That's a new one for me!"]
}

def preprocess_input(user_input):
    # Convert to lowercase and remove punctuation
    processed = re.sub(r'[^\w\s]', '', user_input.lower())
    return processed.strip()

def get_response(user_input):
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

def chatbot():
    print("ChatBot: Hello! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        processed_input = preprocess_input(user_input)
        
        if processed_input == 'bye':
            print("ChatBot: Goodbye! It was nice chatting with you.")
            break
        
        response = get_response(processed_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chatbot()
