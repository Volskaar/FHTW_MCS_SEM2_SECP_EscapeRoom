#!/with-contenv bash

# Wir schreiben den Befehl einfach in die Autostart-Datei des Users
# Das umgeht alle D-Bus Probleme beim Booten.

USER_AUTOSTART="/home/hans.habicht/.config/autostart"
mkdir -p "$USER_AUTOSTART"

echo "[Desktop Entry]
Type=Application
Name=SetWallpaper
Exec=gsettings set org.mate.background picture-filename '/custom/remington-dogtag.png'
" > "$USER_AUTOSTART/wallpaper.desktop"

# Rechte korrigieren, damit hans.habicht die Datei lesen darf
chown -R hans.habicht:hans.habicht /home/hans.habicht/.config