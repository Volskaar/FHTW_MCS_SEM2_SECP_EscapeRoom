#!/bin/bash

# Define the desktop path for the custom user (mapped to /config)

DESKTOP_DIR="/config/Desktop"
echo "Set shortcuts"

# 2. Copy Chromium shortcut
# Note: The filename may vary slightly depending on the install source
if [ -f "/usr/share/applications/chromium.desktop" ]; then
    ln -s /usr/share/applications/chromium.desktop "$DESKTOP_DIR/"
    echo "Chrome shortcut set."
elif [ -f "/usr/share/applications/chromium-browser.desktop" ]; then
    ln -s /usr/share/applications/chromium-browser.desktop "$DESKTOP_DIR/"
    echo "Chrome shortcut set."
fi
if [ -f "/usr/share/applications/mate-terminal.desktop" ]; then
    ln -s /usr/share/applications/mate-terminal.desktop "$DESKTOP_DIR/"
    echo "Terminal shortcut set."
fi