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