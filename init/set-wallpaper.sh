#!/with-contenv bash

# Define the path to the image inside the container
WALLPAPER_PATH="/desktop/remington.png"

# Wait for the desktop environment configuration to be available
# We use 'sudo -u abc' because gsettings must modify the user's dconf database
if [ -f "$WALLPAPER_PATH" ]; then
    echo "Setting wallpaper to $WALLPAPER_PATH..."
    
    # In Mate Desktop, these are the schema keys for the wallpaper
    sudo -u abc DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.mate.background picture-filename "$WALLPAPER_PATH"
    
    sudo -u abc DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus \
    gsettings set org.mate.background picture-options "zoom"
else
    echo "Wallpaper file not found at $WALLPAPER_PATH"
fi