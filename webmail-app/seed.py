from db import DB_PATH, get_connection

def initialize_webmail_db() -> None:
    if DB_PATH.exists():
        DB_PATH.unlink()

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS webmail_users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
            """
        )

        conn.executemany(
            """
            INSERT INTO webmail_users (username, password, role)
            VALUES (?, ?, ?)
            """,
            [
                ("hans.habicht", "Remington", "user"),
            ],
        )

if __name__ == "__main__":
    initialize_webmail_db()
    print(f"Webmail database created at: {DB_PATH}")