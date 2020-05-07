#!/usr/bin/env python
import nativemessaging
import os
import re
import time

# We check if "nmyv" is open
# If not then we open it up with a youtube-viewer
# The main loop is as follows
# 1. Wait for a message
# 2. Close a potentially open video with "q<Backspace>"
# 3. Open the video

#print("nmyv host started")
# Check for nmyv and open if needed
stream = os.popen('tmux list-sessions | grep nmyv | wc -l')
numStreams = stream.read()
numStreams = numStreams.strip('\n')
numStreams = int(numStreams)
if numStreams == 0:
    os.system('tmux new -d -s nmyv')
    os.system('tmux send-keys -t nmyv youtube-viewer Enter')

# Main loop
myRegex = re.compile('[a-zA-Z0-9_-]{11}');
while True:
    # Get the URL from the extension
    message = nativemessaging.get_message()
    # Close any currently running videos
    os.system('tmux send-keys -t nmyv q BSpace')
    time.sleep(0.5)
    # Check that we only got a valid youtube ID
    vidMatch = myRegex.match(message["text"]);
    if vidMatch:
        vid = vidMatch.string
        # Open the new video
        os.system('tmux send-keys -t nmyv :v='+vid+' Enter')
