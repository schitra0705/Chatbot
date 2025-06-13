from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple responses for the chatbot
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm doing great, thanks for asking!",
    "what's your name": "I'm ChatBot, nice to meet you!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm not sure I understand. Could you please rephrase that?"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '').lower()
    
    # Get response based on user input
    response = responses.get(user_message, responses['default'])
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True) 