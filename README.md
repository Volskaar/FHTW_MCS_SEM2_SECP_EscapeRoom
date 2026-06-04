# FHTW_MCS_SEM2_SECP_EscapeRoom
Security Awareness Escape Room Project for the second semester of the Master Studies Program

# PREREQUISITES

Docker & python3 installed 

# SETUP
```powershell
cd <repo>

# build and start all services
docker compose up -d --build

# access http://localhost:3000/  or https://localhost:3001/ to see webtop interface
# access http://localhost:5001/ to see the read-only webmail viewer

Cleanup
rm -r config/
docker system prune -f
```
