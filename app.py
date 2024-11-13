import time
import threading
from flask import Flask, jsonify, render_template
from googleapiclient.discovery import build

# Set up your API key and YouTube video ID
API_KEY = "Enter Your API key here"
VIDEO_ID = input("Enter Video ID")

# Initialize Flask app and YouTube API client
app = Flask(__name__)
youtube = build("youtube", "v3", developerKey=API_KEY)
chat_messages = []

def get_live_chat_id(video_id):
    """Retrieve the live chat ID of a YouTube live stream."""
    response = youtube.videos().list(part="liveStreamingDetails", id=video_id).execute()
    live_chat_id = response["items"][0]["liveStreamingDetails"].get("activeLiveChatId")
    return live_chat_id

def fetch_chat_messages(live_chat_id):
    """Continuously fetch chat messages and store them in the chat_messages list."""
    next_page_token = None
    while True:
        response = youtube.liveChatMessages().list(
            liveChatId=live_chat_id,
            part="snippet,authorDetails",
            pageToken=next_page_token
        ).execute()
        
        messages = response["items"]
        for message in messages:
            if "textMessageDetails" in message["snippet"]:
                message_text = message["snippet"]["textMessageDetails"]["messageText"]
                author_name = message["authorDetails"]["displayName"]
                timestamp = message["snippet"]["publishedAt"]
                
                # Add message to chat_messages list
                chat_messages.append({"timestamp": timestamp, "author": author_name, "text": message_text})
                
                # Limit the list size to prevent memory issues
                if len(chat_messages) > 100:
                    chat_messages.pop(0)
        
        next_page_token = response.get("nextPageToken")
        time.sleep(5)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_messages')
def get_messages():
    """Endpoint to get the latest chat messages."""
    return jsonify(chat_messages)

def start_fetching():
    """Start the message fetching in a separate thread."""
    live_chat_id = get_live_chat_id(VIDEO_ID)
    if live_chat_id:
        fetch_chat_messages(live_chat_id)

if __name__ == "__main__":
    # Start the message fetching thread
    thread = threading.Thread(target=start_fetching)
    thread.start()

    # Run the Flask app
    app.run(debug=True)
