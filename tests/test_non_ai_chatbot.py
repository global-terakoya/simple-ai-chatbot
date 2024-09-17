import unittest
from unittest.mock import patch
from io import StringIO
import sys
from non_ai_chatbot import preprocess_input, get_response, chatbot

class TestChatbot(unittest.TestCase):

    def test_preprocess_input(self):
        self.assertEqual(preprocess_input("Hello, how are you?"), "hello how are you")
        self.assertEqual(preprocess_input("What's your name?"), "whats your name")

    def test_get_response(self):
        self.assertIn(get_response("hello"), ["Hi there!", "Hello!", "Greetings!"])
        self.assertIn(get_response("how are you"), ["I'm doing well, thanks for asking!", "I'm great! How about you?", "All good here!"])
        self.assertIn(get_response("what's your name"), ["My name is ChatBot. Nice to meet you!", "I'm ChatBot. What's your name?"])
        self.assertIn(get_response("what is the weather in tokyo"), ["I'm not able to check the weather, but I hope it's nice outside!", "Why don't you look out the window and tell me?"])
        self.assertIn(get_response("what is the meaning of life"), ["Interesting. Tell me more.", "I'm not sure I understand. Can you rephrase that?", "That's a new one for me!"])

    @patch('builtins.input', side_effect=['hello', 'how are you', 'bye'])
    def test_chatbot(self, mock_input):
        # Redirect stdout to capture print statements
        captured_output = StringIO()
        sys.stdout = captured_output

        chatbot()

        # Reset stdout
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()
        self.assertIn("Hello! I'm a simple chatbot.", output)
        self.assertIn("ChatBot: Hi there!", output)
        self.assertIn("ChatBot: I'm doing well, thanks for asking!", output)
        self.assertIn("ChatBot: Goodbye! It was nice chatting with you.", output)

if __name__ == '__main__':
    unittest.main()