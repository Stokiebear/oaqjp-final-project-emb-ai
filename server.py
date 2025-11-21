"""
Server module for Emotion Detection project.
Module defines the Flask application and exports the
endpoint used by the frontend to process emotion detection
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detection

app = Flask(__name__)

@app.route("/")
def home():
    """
    Uses the main HTML interface for the emotion detection application.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def get_emotion():
    """
    Endpoint that handles emotion detection requests
    Extracts the input text from the query params, calls the emotion_detection function,
    and returns the JSON response expected by the frontend.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    # Call your emotion detection function
    result = emotion_detection(text_to_analyze)

    if result["dominant_emotion"] is None:
        return jsonify(
            {
            "error":"Invalid text! Try again!"
            }
            )

    # Return JSON because the JS script expects JSON
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
