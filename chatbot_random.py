import random
responses = {
    "hi": ["Hello!", "Hi there!", "Hi, how can I help you?"],
    "hello": ["Hello!", "Hi there!", "Hi, how can I assist you?"],
    "hey": ["Hey there!", "Hello!", "Hi! How can I help you today?"],
    "how are you": ["I'm doing well, thank you. How can I assist you today?", "I'm good, thanks for asking. What can I help you with?"],
    "what's up": ["Not much, how can I assist you today?", "Just here to help. What can I do for you?"],
    "what can you do": ["I can help answer your questions, provide information, and assist with various tasks. What can I help you with today?"],
    "who are you": ["I am a chatbot designed to assist with your needs. How can I help you today?"],
    "where are you from": ["I was created by a team of developers to assist with your needs. How can I assist you today?"],
    "what do you know": ["I know a lot about various topics, including technology, health, and entertainment. What can I help you with?"],
    "how old are you": ["I was just recently created, so I don't have an age yet. How can I assist you today?"],
    "default" : ["I'm sorry, I didn't understand."]
}

#only prepare this
def generate_response(message):
    message = message.lower()

    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

print("Welcome to our restaurant. How can I assist you?")

while True:
    message = input("You: ")
    response = generate_response(message)
    print("Bot: ", response)