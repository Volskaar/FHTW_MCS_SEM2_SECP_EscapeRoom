#!/bin/bash
# Force the correct user home directory context
export HOME="/config"
export PATH="$HOME/.local/bin:$PATH"

echo "Install thunderbird"
# Call the proot manager script with explicit arguments in the background
/config/.local/bin/proot-apps install thunderbird > /config/thunderbird_install.log 2>&1 &