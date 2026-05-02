from flask import Flask, render_template, request

app = Flask(__name__)

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! "
    elif "can you help me" in user_input or "can u help me" in user_input:
        return "yes offcourse!! how can i help you"
    elif "how are you" in user_input:
        return "I am fine!"
    elif "name" in user_input:
        return "I am your AI chatbot "
    elif "google" in user_input:
        return '<a href="https://www.google.com" target="_blank">Open Google</a>'
    elif "exam" in user_input:
        return "All the best for your exam! if u need any help then let me know"
    elif "youtube" in user_input:
        return '<a href="https://www.youtube.com" target="_blank">Open YouTube</a>'
    elif "sad" in user_input or "upset" in user_input:
        return "I'm sorry to hear that Stay strong!"
    elif "bye" in user_input:
        return "Goodbye!"

    else:
        return "sorry! Can you tell me more?."

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template(
        "index.html",
        response=chatbot_response(request.form["message"]) if request.method == "POST" else ""
    )

app.run(debug=True)