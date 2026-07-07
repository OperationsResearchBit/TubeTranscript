# TubeTranscript

apgl3

# YouTube Transcript App

Flask app (must launch on a server, not github pages) 

## Project Structure

```
youtube-transcript-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── templates/
    └── index.html      # Frontend web interface
```

needs to run requirements to install 
flask
flask-cors
youtube-transcript-api

## Setup Instructions

1. **Install dependencies:**
   Run the following command in your terminal to install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the application:**
   Start your Flask app by running:
   ```bash
   python app.py
   ```

## Files 

1. app.py (Flask backend)

Contains:

Flask server
YouTube URL parsing
YouTube Transcript API calls
/transcript endpoint

Example:

youtube-transcript-app/app.py
2. requirements.txt

Contains all Python packages needed:

flask
flask-cors
youtube-transcript-api

Someone installing the app runs:

pip install -r requirements.txt
3. templates/index.html

The website interface:

Contains:

URL input box
Generate Transcript button
Transcript display
JavaScript calling Flask API

Location is important:

templates/index.html

NOT:

index.html

because Flask automatically looks inside the templates folder.

4. README.md

Instructions for users:
