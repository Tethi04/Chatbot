from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

class RuleBasedChatbot:
    def __init__(self):
        self.sensitive_keywords = [
            'hate', 'violence', 'kill', 'harm', 'suicide', 'bomb', 'weapon',
            'drugs', 'illegal', 'porn', 'explicit', 'racist', 'discriminate',
            'attack', 'murder', 'terrorist', 'abuse'
        ]
        
        self.responses = {
            'greeting': [
                "Hello! How can I assist you today?",
                "Hi there! What can I help you with?",
                "Hey! Welcome to our chatbot service. How can I help?"
            ],
            'farewell': [
                "Goodbye! Have a great day!",
                "See you later! Feel free to come back if you have more questions.",
                "Bye! Take care!"
            ],
            'thanks': [
                "You're welcome!",
                "Happy to help!",
                "Anytime! Let me know if you need anything else."
            ],
            'name': [
                "I'm a rule-based chatbot created to assist you!",
                "You can call me ChatBot! I'm here to help answer your questions."
            ],
            'weather': [
                "I don't have real-time weather data, but you can check weather websites or apps for current conditions.",
                "For accurate weather information, I recommend checking reliable weather services."
            ],
            'time': [
                "I don't have access to current time. Please check your device's clock.",
                "You can check the time on your computer or phone for accurate current time."
            ],
            'joke': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "What do you call a fake noodle? An impasta!"
            ],
            'help': [
                "I can help you with general information, answer questions, tell jokes, and more! Just ask me anything.",
                "Feel free to ask me about various topics, and I'll do my best to assist you!"
            ],
            'math': [
                "I can help with basic math concepts! For complex calculations, you might need a calculator.",
                "Math is fun! I can discuss basic arithmetic and mathematical concepts."
            ],
            'programming': [
                "I can help with basic programming concepts! For complex code, you might need specialized tools.",
                "Programming is awesome! I can discuss basic coding principles and best practices."
            ],
            'default': [
                "I'm not sure I understand. Could you rephrase that?",
                "That's an interesting question. Could you provide more details?",
                "I'm still learning. Could you ask that in a different way?"
            ]
        }
    
    def is_sensitive(self, message):
        message_lower = message.lower()
        for keyword in self.sensitive_keywords:
            if keyword in message_lower:
                return True
        return False
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for sensitive content first
        if self.is_sensitive(user_input):
            return "Sorry, I can't assist you with this. Please ask something else."
        
        # Greeting patterns
        if any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon']):
            return self.responses['greeting'][0]
        
        # Farewell patterns
        elif any(word in user_input for word in ['bye', 'goodbye', 'see you', 'exit', 'quit', 'goodbye']):
            return self.responses['farewell'][0]
        
        # Thanks patterns
        elif any(word in user_input for word in ['thank', 'thanks', 'appreciate']):
            return self.responses['thanks'][0]
        
        # Name patterns
        elif any(word in user_input for word in ['who are you', 'what are you', 'your name', 'what is your name']):
            return self.responses['name'][0]
        
        # Weather patterns
        elif any(word in user_input for word in ['weather', 'temperature', 'forecast', 'rain', 'sunny']):
            return self.responses['weather'][0]
        
        # Time patterns
        elif any(word in user_input for word in ['time', 'clock', 'what time', 'current time']):
            return self.responses['time'][0]
        
        # Joke patterns
        elif any(word in user_input for word in ['joke', 'funny', 'make me laugh', 'tell me a joke']):
            return self.responses['joke'][0]
        
        # Help patterns
        elif any(word in user_input for word in ['help', 'what can you do', 'capabilities', 'how to use']):
            return self.responses['help'][0]
        
        # Math patterns
        elif any(word in user_input for word in ['math', 'calculate', 'addition', 'subtraction', 'multiplication', 'division']):
            return self.responses['math'][0]
        
        # Programming patterns
        elif any(word in user_input for word in ['programming', 'code', 'python', 'javascript', 'java', 'coding']):
            return self.responses['programming'][0]
        
        # How are you patterns
        elif any(word in user_input for word in ['how are you', 'how do you do', 'how is it going']):
            return "I'm just a chatbot, but I'm functioning well! How can I help you today?"
        
        # Default response
        else:
            return self.responses['default'][0]

# Initialize chatbot
chatbot = RuleBasedChatbot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        bot_response = chatbot.get_response(user_message)
        return jsonify({'response': bot_response})
    except Exception as e:
        return jsonify({'response': 'Sorry, I encountered an error. Please try again.'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'message': 'Chatbot is running!'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
