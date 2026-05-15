# FHTW_MCS_SEM2_SECP_EscapeRoom
Security Awareness Escape Room Project for the second semester of the Master Studies Program

# SETUP
```powershell
cd <repo>
docker compose build --no-cache
mkdir config
docker compose up

access http://localhost:3000/ to see webtop interface

Cleanup
rm -r config/
docker system prune -f
```
