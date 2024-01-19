import nltk
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you.', 'I am good. How about you?']),
    (r'what is your name', ['I am a chatbot. You can call me ChatGPT.', 'I am ChatGPT, your virtual assistant.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'your favorite color', ['I don\'t have a favorite color. I am a text-based entity.']),
    (r'how old are you', ['I don\'t have an age. I am a program.']),
    (r'where are you from', ['I exist in the digital realm.']),
    (r'what can you do', ['I can answer questions, engage in conversation, and assist you with information.']),
    (r'(.*)', ["I'm sorry, I didn't understand that. Can you please rephrase?"])
]

# Create a chatbot using the patterns
chatbot = Chat(patterns, reflections)

# Main loop for the chatbot
def main():
    print("Chatbot: Hello! I'm your chatbot. Type 'bye' to exit.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        # Get and print chatbot response
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
