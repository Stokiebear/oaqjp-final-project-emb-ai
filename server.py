from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def get_emotion():
    # Read the text from the query parameter
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Call your emotion detection function
    result = emotion_detection(text_to_analyze)

    # Return JSON because the JS script expects JSON
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
