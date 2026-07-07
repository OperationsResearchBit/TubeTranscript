from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
import re

app = Flask(__name__)
CORS(app)


def extract_video_id(url):
    patterns = [
        r"youtube\.com/watch\?v=([^&]+)",
        r"youtu\.be/([^?]+)",
        r"youtube\.com/embed/([^?]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/transcript", methods=["POST"])
def transcript():

    data = request.json
    url = data.get("url")

    video_id = extract_video_id(url)

    if not video_id:
        return jsonify({
            "error": "Invalid YouTube URL"
        })


    try:

        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        text = "\n".join(
            snippet.text for snippet in transcript
        )


        return jsonify({
            "transcript": text
        })


    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5001
    )