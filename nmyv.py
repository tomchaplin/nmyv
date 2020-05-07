#!/usr/bin/env python
import nativemessaging
import os
import re
import time

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
