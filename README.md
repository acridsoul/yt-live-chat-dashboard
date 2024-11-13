# YouTube Live Chat Dashboard

A real-time dashboard for viewing YouTube live chat messages using Flask, JavaScript, and the YouTube Data API.

## Features

- Displays real-time chat messages from a YouTube livestream.
- Filters messages by user and keywords (configurable).
- Customizable display with auto-refresh.

## Setup

**1. Clone the repository:**
   ```bash
   git clone https://github.com/username/yt-live-chat-dashboard.git
   cd yt-live-chat-dashboard
   ```

**2. Set up a virtual environment**

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**3. Install the dependencies** 

   ```
   pip install -r requirements.txt
   ```
   * **Set up the YouTube Data API key** :
   * Go to the [Google Developers Console](https://console.cloud.google.com).
   * Create a new project and enable the YouTube Data API v3.
   * Generate an API key and replace `YOUR_YOUTUBE_API_KEY` in `app.py` with your actual key.
   * You also need the YouTube live stream's video ID. Find this from the live stream URL (`https://www.youtube.com/watch?v=VIDEO_ID`).
   * **Run the app** :
     ```
     python3 app.py
     ```
