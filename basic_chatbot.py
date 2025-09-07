# Basic Chatbot
def simple_chatbot(user_input):
 greetings = ["hello", "hi", "hey"]
 farewells = ["bye", "goodbye", "see you"]  
  if user_input.lower() in greetings:
   return "Hello! How can I assist you?"
 elif user_input.lower() in farewells:
   return "Goodbye! Have a great day."
 else:
   return "I'm just a basic chatbot. I respond to greetings and farewells."  # Example usage
user_input = input("User: ")
bot_response = simple_chatbot(user_input)
print(f"Bot: {bot_response}")

