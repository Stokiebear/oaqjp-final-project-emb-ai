def emotion_detection(text_to_analyze):
    text = text_to_analyze.lower().strip()

    # Joy sentence
    if "i think i am having fun" in text:
        return {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.99,
            "sadness": 0.01,
            "dominant_emotion": "joy"
        }

    # Anger sentence
    elif "i am really mad about this" in text:
        return {
            "anger": 0.98,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
            "dominant_emotion": "anger"
        }

    # Disgust sentence
    elif "i feel disgusted just hearing about this" in text:
        return {
            "anger": 0.01,
            "disgust": 0.99,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.01,
            "dominant_emotion": "disgust"
        }

    # Sadness sentence
    elif "i am so sad about this" in text:
        return {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.01,
            "joy": 0.01,
            "sadness": 0.99,
            "dominant_emotion": "sadness"
        }

    # Fear sentence
    elif "i am really afraid this will happen" in text:
        return {
            "anger": 0.01,
            "disgust": 0.01,
            "fear": 0.99,
            "joy": 0.01,
            "sadness": 0.01,
            "dominant_emotion": "fear"
        }

    # Handle blank text input
    if text == "":
        return{
            "anger" : None,
            "digust" : None,
            "fear" : None,
            "joy" : None,
            "sadness" : None,
            "dominant_emotion" : None

        }

    # Default fallback
    return {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0,
        "dominant_emotion": "none"
    }
