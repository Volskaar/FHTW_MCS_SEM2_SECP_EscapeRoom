import csv
from pathlib import Path
from db import get_connection
import shutil

BASE_DIR = Path(__file__).resolve().parent.parent
BACKUP_DIR = BASE_DIR / "backups"
BACKUP_FILE = BACKUP_DIR / "BACKUP_2026-06-02.csv"

def create_backup():
    if BACKUP_DIR.exists():
        shutil.rmtree(BACKUP_DIR)

    BACKUP_DIR.mkdir(exist_ok=True)

    with get_connection() as connection:
        employees = connection.execute("""
            SELECT
                first_name,
                last_name,
                department,
                position,
                email,
                phone,
                university,
                salary
            FROM employees
        """).fetchall()

    with open(BACKUP_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow([
            "first_name",
            "last_name",
            "department",
            "position",
            "email",
            "phone",
            "university",
            "salary"
        ])

        for employee in employees:
            writer.writerow([
                employee["first_name"],
                employee["last_name"],
                employee["department"],
                employee["position"],
                employee["email"],
                employee["phone"],
                employee["university"],
                employee["salary"]
            ])

    print(f"Backup created at: {BACKUP_FILE}")

if __name__ == "__main__":
    create_backup()