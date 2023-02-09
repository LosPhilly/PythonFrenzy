responses = {
    "hello": "Hello there!",
    "how are you": "I'm doing well, how about you?",
    "goodbye": "Goodbye!",
    "default": "Sorry, I didn't understand what you said."
}

def respond(message):
    if message in responses:
        return responses[message]
    else:
        return responses["default"]

print("Welcome to the chatbot!")
while True:
    message = input("You: ")
    if message.lower() == "goodbye":
        print(respond(message))
        break
    print("Chatbot: " + respond(message))
