#!/bin/bash

# Clear previous run artifacts
docker system prune -f; 
sudo rm -r config/;

python3 -u ./app/seed.py
python3 -u ./app/create_backup.py

mkdir config;

docker compose build --no-cache;
docker compose up