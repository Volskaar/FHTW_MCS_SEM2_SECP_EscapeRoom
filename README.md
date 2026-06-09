# FHTW_MCS_SEM2_SECP_EscapeRoom
Security Awareness Escape Room Project for the second semester of the Master Studies Program.

---

# Educational Value
The following learning objectives have been formally defined:
- Players understand common best practices in IT security
- Players are able to identify security vulnerabilities in everyday and work-related scenarios
- Players can derive basic protective measures and explain their significance
- Players work solo or collaboratively to solve tasks under time pressure

---

# Challenges
### Password Reuse (Level 1, Easy)
- Objective: Access the internal email program
- Problem: Login required
- Vulnerability: The password used for the computer login was reused
- Solution: Brute-force attack

### Password File (Level 2, Medium)
- Goal: Access to stored login credentials
- Problem: File in the “Work” folder is ‘encrypted’
- Vulnerability: Insecure “encryption”
- Solution: Clue in email conversation with IT; use of Base64 encoding; decoding via online tools
- Security Lesson: Encoding ≠ Encryption

### HR Platform Access (Level 1, Easy)
- Goal: Access user information
- Problem: Login required
- Solution: Use credentials from password file
- Security Lesson: Insecure storage of sensitive data

### HR Platform Admin Access (Level 2, Medium)
- Goal: Escalation of user privileges
- Problem: No admin access available
- Vulnerability: Hardcoded credentials
- Solution: Search public GitHub repository; find admin credentials in the code
- Security Lesson: Secrets never belong in source code

### Database Exfiltration (Level 3, Hard)
- Goal: Access to sensitive company data
- Problem: Access to database required
- Solution: Connect via SSH using admin credentials; identify the database file; download via SFTP
- Security Lesson: Lack of access restrictions, insufficient network segmentation, insecure backup strategy (local backup)

---

# PREREQUISITES

Docker & python3 installed 

---

# SETUP
```powershell
cd <repo>

# execute startup script
./startup.sh

# access http://localhost:3000/  or https://localhost:3001/ to see webtop interface
# access http://localhost:5001/ to see the read-only webmail viewer

Cleanup
rm -r config/
docker system prune -f
```
