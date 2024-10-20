from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.json.get('message')
    response = {"reply": f"You said: {user_input}"}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
