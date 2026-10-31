# Datheon Python Internship - Task 2
# Intern: Peterclever Mmegwa | ID: DT-2026-K9SYK
print("=== DATHEON CHATBOT ===")
print("Type 'bye' to exit")
while True:
    user = input("You: ").lower()
    if user in ["bye","exit","quit"]:
        print("Bot: Goodbye! Thanks for chatting - from Datheon Intern")
        break
    elif "hello" in user or "hi" in user:
        print("Bot: Hello! I'm Datheon Bot, created by Peterclever")
    elif "how are you" in user:
        print("Bot: I'm great! Learning Python at Datheon")
    elif "name" in user:
        print("Bot: I'm DatheonBot, built by Peterclever Mmegwa")
    elif "python" in user:
        print("Bot: Python is awesome! I'm made with Python")
    elif "datheon" in user:
        print("Bot: Datheon is where I intern as Python developer")
    else:
        print("Bot: Interesting! Tell me more about", user)