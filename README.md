# Weather-Chat-Bot

This is a simple chatbot application built with Python's `Tkinter` for the graphical user interface (GUI) and OpenWeatherMap API for fetching weather information. The chatbot supports small talk and provides weather updates for specific cities when prompted.

## Features

- **Small Talk**: The bot can engage in casual conversation with predefined witty and fun responses.
- **Weather Information**: Users can ask the bot for the current weather in a specific city. The bot fetches real-time weather data using the OpenWeatherMap API.
- **Interactive GUI**: The bot operates via a graphical interface where users can type in questions and receive responses.
- **Error Handling**: Gracefully handles invalid or missing weather data.

## How It Works

1. **Small Talk**: The bot recognizes certain keywords or phrases, such as "hello", "thank you", or "tell me a joke", and responds with preset answers.
2. **Weather Queries**: When the user asks about the weather in a particular city, the bot extracts the city name from the user’s input using a regular expression and then fetches weather data from OpenWeatherMap.
3. **Tkinter GUI**: The chatbot interface consists of a scrollable chat area, a user input field, and a send button.

## Example Interaction

```text
You: Hello
Bot: Hi there! How can I help you today? Got any cool plans?

You: What's the weather in London?
Bot: The temperature in London is 15°C with scattered clouds.

You: Tell me a joke.
Bot: Why don't programmers like nature? It has too many bugs!

You: Goodbye
Bot: Goodbye! Don't forget to come back when you miss me!
