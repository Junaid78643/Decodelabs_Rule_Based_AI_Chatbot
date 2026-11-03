# Rule-based AI Chatbot
# Simple chatbot that responds using if-else logic

print("Welcome to the Rule-Based Chatbot!")
print("Type 'exit' to quit the chat.")

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["hello", "hi", "hey", "greetings"]:
        print("Bot: Hello! How can I help you today?")
    elif user_input in ["how are you", "how are you?", "how are u"]:
        print("Bot: I'm doing well, thank you! How about you?")
    elif user_input in ["who are you", "what are you"]:
        print("Bot: I am a simple rule-based chatbot created to respond to common messages.")
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break
    elif user_input in ["thanks", "thank you"]:
        print("Bot: You're welcome!")
    else:
        print("Bot: I am not sure how to respond to that. Please ask something else.")
