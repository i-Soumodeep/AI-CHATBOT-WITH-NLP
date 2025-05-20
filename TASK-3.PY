import random
import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

# Define chatbot pairs (patterns and responses)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I'm a simple chatbot created with NLTK!", "You can call me ChatBot."]
    ],
    [
        r"how are you?",
        ["I'm just a program, but I'm functioning well!", "All systems are operational!"]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not connected to weather services, but you can check your favorite weather app!"]
    ],
    [
        r"(.*) help (.*)",
        ["I can answer simple questions. Try asking me about my capabilities!"]
    ],
    [
        r"(.*) your capabilities(.*)",
        ["I can greet you, introduce myself, and respond to basic questions!"]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a great day!", "It was nice talking to you!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you rephrase that?", 
         "Interesting! Can you tell me more?",
         "I'm still learning. Could you ask me something else?"]
    ]
]

class EnhancedChatbot:
    def __init__(self):
        self.chatbot = Chat(pairs, reflections)
        self.context = {}
        
    def respond(self, user_input):
        # Convert to lowercase and remove extra whitespace
        cleaned_input = user_input.lower().strip()
        
        # Check for empty input
        if not cleaned_input:
            return "Please say something so I can respond!"
            
        # Get response from NLTK chat
        response = self.chatbot.respond(cleaned_input)
        
        # Add some variability if multiple responses exist
        if isinstance(response, list):
            return random.choice(response)
        return response

    def start_chat(self):
        print("ChatBot: Hello! I'm a simple chatbot. Type 'quit' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'bye', 'exit']:
                print("ChatBot: Goodbye!")
                break
            response = self.respond(user_input)
            print(f"ChatBot: {response}")

if __name__ == "__main__":
    # Initialize and start the chatbot
    bot = EnhancedChatbot()
    
    # Start interactive chat session
    bot.start_chat()
