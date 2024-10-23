import re
import requests
import tkinter as tk
from tkinter import scrolledtext

responses = {
    "hello": "Hi there! How can I help you today? Got any cool plans?",
    "hii": "Hii, How are You",
    "bye": "Goodbye! Don't forget to come back when you miss me!",
    "help": "I'm here to assist! Ask me about the weather, tell me a joke, or just chat with me.",
    "how are you": "I'm just a bot, but thanks for asking! I'm feeling binary-iffic!",
    "what's your name": "I'm Chatbot, your trusty virtual sidekick! Not to be confused with Siri or Alexa...",
    "what do you do": "I chat, tell jokes that my creator has taught me, and give weather updates. Basically, I make your life 10% more awesome!",
    "thank you": "You're welcome! If I had hands, I’d give you a high five right now!",
    "what's the time": "Time is just an illusion... but it’s probably a good idea to check your watch!",
    "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
    "what's the meaning of life": "42. But I’m still working on a few updates to get the full answer!",
    "how's the weather": "You'll have to ask me about a specific city. I can't predict global weather... yet!",
    "can you dance": "If typing counts as dancing, I’m doing the cha-cha right now!",
    "are you human": "Nope, I'm a bot. But if I were human, I’d probably be a coffee-loving introvert.",
    "do you sleep": "Nope! I’m always awake, unlike my human creators who need their beauty sleep.",
    "what's your favorite color": "I think I’m partial to #00FF00. It’s the perfect green, don't you think?",
    "can you tell the future": "Only if it involves me answering more questions!",
    "tell me something interesting": "Did you know that sharks have been around longer than trees? Crazy, right?",
    "are you smart": "I’m not the smartest bot, but I can fake it pretty well!",
}

def get_weather(city):
    api_key = "bdf62b2a2c30a0491a9b550254dc7e08"  # Use environment variables for security
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        temp = data['main']['temp']
        weather_desc = data['weather'][0]['description']
        return f"The temperature in {city} is {temp}°C with {weather_desc}."
    else:
        error_message = data.get('message', 'Unknown error')
        return f"Sorry, I couldn't retrieve the weather information. Error: {error_message}"

def get_response(user_input):
    user_input = user_input.lower()
    match = None

    # Check for small talk responses
    for key in responses:
        if key in user_input:
            return responses[key]

    # Check for greetings
    if any(greeting in user_input for greeting in ["hello", "hi", "hey"]):
        return responses["hello"]
    
    # Check for farewells
    elif any(farewell in user_input for farewell in ["bye", "goodbye", "see you"]):
        return responses["bye"]
    
    # Check for help
    elif "help" in user_input:
        return responses["help"]

    # Weather condition
    elif "weather" in user_input:
        match = re.search(r'weather.*(?:in|of|for)\s+([a-zA-Z\s]+)', user_input)
        if match:
            city = match.group(1).strip()
            return get_weather(city)
        else:
            return "Please specify a city to get the weather information."

    return "Sorry, I didn’t understand that. Can you ask something else?"

# Function to handle sending messages
def send_message(event=None):
    user_input = user_input_field.get()
    if user_input.strip():
        chat_area.config(state=tk.NORMAL)  # Enable editing
        chat_area.insert(tk.END, f"You: {user_input}\n")
        user_input_field.delete(0, tk.END)  # Clear input field
        bot_response = get_response(user_input)
        chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")
        chat_area.yview(tk.END)  # Scroll to the end
        chat_area.config(state=tk.DISABLED)  # Disable editing to prevent user input

# Create the main window
root = tk.Tk()
root.title("Weather Chatbot")

# Create chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20, width=50)
chat_area.grid(column=0, row=0, padx=10, pady=10)

# Create user input field
user_input_field = tk.Entry(root, width=50)
user_input_field.grid(column=0, row=1, padx=10, pady=10)
user_input_field.bind("<Return>", send_message)  # Bind Enter key to send message

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(column=0, row=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()

