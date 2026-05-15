#!/with-contenv bash

# Wait for the /config directory to be ready and owned by the abc user
# Create the directory path if it doesn't exist yet
mkdir -p /config/.config/chromium/Default/

# Copy the bookmarks from your mapped configurations folder
if [ -f /config/Desktop/Bookmarks ]; then
    cp /config/Desktop/Bookmarks /config/.config/chromium/Default/Bookmarks
    # Ensure the abc user owns the new file so Chromium can read/write it
    chown abc:abc /config/.config/chromium/Default/Bookmarks
fi