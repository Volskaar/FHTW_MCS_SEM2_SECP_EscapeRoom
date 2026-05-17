#!/bin/bash

CONFIG_PATH="/config/.custom-config"

mkdir $CONFIG_PATH
cp -a /webtop_configurations/. $CONFIG_PATH/

mkdir /config/Desktop/IMPORTANT
cp -a /webtop_configurations/email /config/Desktop/IMPORTANT/email
cp /webtop_configurations/passwords.txt /config/Desktop/IMPORTANT/passwords.txt

chmod +x $CONFIG_PATH/set-wallpaper.sh
chown abc:abc $CONFIG_PATH/set-wallpaper.sh