import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you today?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm good, thanks for asking.", "All good! How about you?"]
    ],
    [
        r"(.*) your name ?",
        ["I'm just a chatbot.", "I'm a bot, I don't have a name.", "You can call me Chatbot."]
    ],
    [
        r"(.*) (buy|sell) (.* )?stock",
        ["I'm just a chatbot and I can't perform stock transactions.", "I can't buy or sell stocks for you.", "You'll need to use a brokerage platform for that."]
    ],
    [
        r"(.*) (weather|forecast) (.*)?",
        ["I don't have access to weather information at the moment.", "You can check the weather on a weather website or app.", "Sorry, I can't provide weather forecasts."]
    ],
    [
        r"(.*) (thank you|thanks) (.*)?",
        ["You're welcome!", "No problem!", "Anytime!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "Bye bye!", "See you later!"]
    ],
    [
        r"(.*)",
        ["Sorry, I didn't understand that.", "Can you please rephrase that?", "I'm not sure what you mean."]
    ]
]

# Create and train the chatbot
def chatbot():
    print("Hi, I'm Chatbot! How can I assist you today?")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    nltk.download("punkt")
    chatbot()
