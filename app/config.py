# TODO: Move these credentials to environment variables before production deployment.
# Temporary technical user for HR server maintenance.

HR_SERVER_HOST = "secp-s26-n2.cs.technikum-wien.at"
HR_SERVER_SSH_PORT = 2222

# TODO NICHT FÜRS SZENARIO: mit tatsächlichen ssh creds austauschen
HR_SERVER_USERNAME = "hr-admin"
HR_SERVER_PASSWORD = "change me"

BACKUP_DIRECTORY = "/opt/fintech/backups"
BACKUP_FILE = "BACKUP_2026-06-02.csv"