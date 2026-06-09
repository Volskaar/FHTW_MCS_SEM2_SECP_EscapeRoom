#!/bin/bash

# Clear previous run artifacts
docker compose down
docker system prune -f; 
rm -r config/;

# Recreate sql files 
python3 -u ./powertool-app/seed.py
python3 -u ./powertool-app/create_backup.py
python3 -u ./webmail-app/seed.py

# Create webtop diretory 
mkdir config;

# Start docker services
docker compose build --no-cache;
docker compose up -d