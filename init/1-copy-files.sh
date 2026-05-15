#!/bin/bash

CONFIG_PATH="/config/.custom-config"

mkdir $CONFIG_PATH
cp -a /webtop_configurations/. $CONFIG_PATH/


chmod +x $CONFIG_PATH/set-wallpaper.sh
chown abc:abc $CONFIG_PATH/set-wallpaper.sh