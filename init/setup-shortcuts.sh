#!/with-contenv bash

# Define the desktop path for the custom user (mapped to /config)
DESKTOP_DIR="/config/Desktop"
mkdir -p "$DESKTOP_DIR"

# 1. Copy Evolution shortcut
if [ -f "/usr/share/applications/org.gnome.Evolution.desktop" ]; then
    cp /usr/share/applications/org.gnome.Evolution.desktop "$DESKTOP_DIR/"
    chmod +x "$DESKTOP_DIR/org.gnome.Evolution.desktop"
fi

# 2. Copy Chromium shortcut
# Note: The filename may vary slightly depending on the install source
if [ -f "/usr/share/applications/chromium.desktop" ]; then
    cp /usr/share/applications/chromium.desktop "$DESKTOP_DIR/"
    chmod +x "$DESKTOP_DIR/chromium.desktop"
elif [ -f "/usr/share/applications/chromium-browser.desktop" ]; then
    cp /usr/share/applications/chromium-browser.desktop "$DESKTOP_DIR/"
    chmod +x "$DESKTOP_DIR/chromium-browser.desktop"
fi

# 3. Fix permissions so 'hans.habicht' (abc) owns them
chown -R abc:abc "$DESKTOP_DIR"