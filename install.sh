#!/bin/bash
HOST_NAME="com.tom.nmyv"
WORKING_DIR="$( pwd )"
TARGET_DIR="$HOME/.config/chromium/NativeMessagingHosts"

# Create directory to store native messaging host manifest
mkdir -p "$TARGET_DIR"

# Copy native messaging host manifest.
cp "$WORKING_DIR/host/$HOST_NAME.json" "$TARGET_DIR"

# Update host path in the manifest.
HOST_PATH="$WORKING_DIR/host/nmyv.py"
ESCAPED_HOST_PATH=${HOST_PATH////\\/}
sed -i -e "s/HOST_PATH/$ESCAPED_HOST_PATH/" "$TARGET_DIR/$HOST_NAME.json"

# Set permissions for the manifest so that all users can read it.
chmod o+r "$TARGET_DIR/$HOST_NAME.json"

echo "Native messaging host $HOST_NAME has been installed."
