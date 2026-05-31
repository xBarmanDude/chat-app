from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    msg = request.json['msg']
    messages.append(msg)
    return "OK"

@app.route('/get')
def get():
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)