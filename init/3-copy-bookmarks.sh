#!/with-contenv bash

# Wait for the /config directory to be ready and owned by the abc user
# Create the directory path if it doesn't exist yet
(
    su - abc -c "chromium --no-sandbox"
) &

sleep 10

pkill -9 chromium

echo "Add Bookmarks"

# Copy the bookmarks from your mapped configurations folder
if [ -f /config/.custom-config/Bookmarks ]; then
    cp /config/.custom-config/Bookmarks /config/.config/chromium/Default/Bookmarks
    # Ensure the abc user owns the new file so Chromium can read/write it
    chmod 755 -R /config/.config/chromium/
    chown abc:abc -R /config/.config/chromium/
    echo "Bookmarks added"
fi

# Update the Preferences file to add the websites to the startup screen
if [ -f /config/.config/chromium/Default/Preferences ]; then
    jq '.session += {"restore_on_startup": 4, "startup_urls": ["http://172.10.10.24:5000/", "https://github.com/eliasentefintech/fintech-hr-powertool"]}'  ~/.config/chromium/Default/Preferences > Preferences.tmp && mv Preferences.tmp ~/.config/chromium/Default/Preferences
    echo "Added startup websites"
fi