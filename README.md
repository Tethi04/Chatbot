
# 🤖 Chatbot

A professional rule-based chatbot built with Python and Flask that can handle various user queries while filtering sensitive content. Deployed live on Render.

## 🌐 Live Demo

**Live Website:** [https://chatbot-y1rl.onrender.com]

![Chatbot Demo](https://img.shields.io/badge/Status-Live-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-lightgrey)

## ✨ Features

- 🎯 **Rule-based Response System** - Handles multiple conversation patterns
- 🛡️ **Sensitive Content Filtering** - Automatically detects and blocks inappropriate content
- 💬 **Beautiful Web Interface** - Modern, responsive chat interface
- 📱 **Mobile Responsive** - Works perfectly on all devices
- ⚡ **Fast & Lightweight** - Built with Flask for optimal performance
- 🔒 **Safe & Secure** - Content moderation built-in

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tethi04/chatbot.git
   cd rule-based-chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

### File Structure
```
rule-based-chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── runtime.txt           # Python version specification
├── README.md             # Project documentation
└── templates/
    └── index.html        # Chatbot web interface
```

## 🎮 How to Use

1. **Visit** (https://chatbot-y1rl.onrender.com)
2. **Start chatting** by typing your message
3. **Try these examples:**
   - "Hello" or "Hi"
   - "What's your name?"
   - "Tell me a joke"
   - "How are you?"
   - "What can you do?"

## 🛡️ Content Safety

The chatbot automatically filters and blocks sensitive topics including:
- Violence and harmful content
- Illegal activities
- Inappropriate material
- Hate speech and discrimination

**Response to sensitive content:** "Sorry, I can't assist you with this. Please ask something else."

## 🛠️ Technologies Used

- **Backend:** Python, Flask, Gunicorn
- **Frontend:** HTML5, CSS3, JavaScript
- **Deployment:** Render
- **Version Control:** GitHub

## 📋 Response Patterns

The chatbot recognizes these conversation patterns:

     | Category | Example Triggers | Sample Response |
     |----------|------------------|-----------------|
     | Greetings | "hello", "hi", "hey" | "Hello! How can I assist you today?" |
     | Farewell | "bye", "goodbye" | "Goodbye! Have a great day!" |
     | Questions | "what can you do", "help" | "I can help with general information..." |
     | Entertainment | "joke", "funny" | "Why don't scientists trust atoms?" |
     | Technical | "programming", "python" | "I can help with basic programming concepts!" |

## 🌐 Deployment

This project is deployed on **Render** with the following configuration:

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Environment:** Python 3.9
- **Auto-deploy:** Enabled from GitHub

### Deployment Status
![Render Deployment](https://img.shields.io/badge/Render-Deployed-success)

## 🔧 API Endpoints

- `GET /` - Main chatbot interface
- `POST /chat` - Chat message processing
- `GET /health` - Health check endpoint


## 📝 License

This project is open source and available under the [MIT License](LICENSE).

# `https://chatbot-y1rl.onrender.com`
