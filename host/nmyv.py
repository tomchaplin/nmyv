#!/usr/bin/env python
import nativemessaging
import os
import re
import time
import json

# Check for nmyv and open if needed
stream = os.popen('tmux list-sessions | grep nmyv | wc -l')
numStreams = stream.read()
numStreams = numStreams.strip('\n')
numStreams = int(numStreams)
if numStreams == 0:
    os.system('tmux new -d -s nmyv')
    os.system('tmux send-keys -t nmyv youtube-viewer Enter')

# Main loop
vidRegex = re.compile('[a-zA-Z0-9_-]{11}');
while True:
    # Get the URL from the extension
    message = nativemessaging.get_message()
    # Close any currently running videos and close youtube-viewer
    os.system('tmux send-keys -t nmyv q Bspace :q Enter')
    sleep(0.2)
    # Check that we only got a valid youtube ID
    vidMatch = vidRegex.match(message["text"]);
    if vidMatch:
        timeStart = str(int(message["time"]));
        vid = vidMatch.string
        # Open the new video
        os.system('tmux send-keys -t nmyv youtube-viewer Space :v='+vid+' Space')
        os.system('tmux send-keys -t nmyv -l \'\' --append-arg=\\\"')
        os.system('tmux send-keys -t nmyv -l \'\' --x11-name=nmyv')
        os.system('tmux send-keys -t nmyv Space');
        os.system('tmux send-keys -t nmyv -l \'\' --start='+timeStart+'\\\"')
        os.system('tmux send-keys -t nmyv Enter');
