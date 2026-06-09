#!/bin/bash

CONFIG_PATH="/config/.custom-config"
AUTOSTART_PATH="/config/.config/autostart/"


if [ -d "$AUTOSTART_PATH" ]; then
    echo "Modifying autostart to set wallpaper to $WALLPAPER_PATH..."
    
    cp $CONFIG_PATH/set-wallpaper.desktop $AUTOSTART_PATH/set-wallpaper.desktop
    #cp $CONFIG_PATH/install-thunderbird.desktop $AUTOSTART_PATH/install-thunderbird.desktop

    echo "Autostart modified."
    ls -lit $AUTOSTART_PATH/
else
    echo "Autostart path not found at $AUTOSTART_PATH"
    echo "Create directory"

    mkdir -p "$AUTOSTART_PATH" && cp $CONFIG_PATH/set-wallpaper.desktop $AUTOSTART_PATH/set-wallpaper.desktop
    #cp $CONFIG_PATH/install-thunderbird.desktop $AUTOSTART_PATH/install-thunderbird.desktop

    echo "Autostart modified."
    ls -lit $AUTOSTART_PATH/
fi