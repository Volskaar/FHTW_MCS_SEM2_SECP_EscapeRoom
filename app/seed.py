from db import get_connection, DB_PATH

def create_tables():
    DB_PATH.parent.mkdir(exist_ok=True)

    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                department TEXT NOT NULL,
                position TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                salary INTEGER
            )
        """)

def seed_data():
    with get_connection() as connection:
        connection.execute("DELETE FROM users")
        connection.execute("DELETE FROM employees")

        connection.executemany("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, [
            ("hans.habicht", "MeinSicheresPasswort1220!", "user"),
            ("admin", "FinTechAdmin2026!", "admin"),
        ])

        connection.executemany("""
            INSERT INTO employees (
                first_name, last_name, department, position,
                email, phone, salary
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, [
            ("Hans", "Habicht", "Personalabteilung", "Leiter Controlling", "hans.habicht@fintech-austria.local", None, 68000),
            ("Kerstin", "Krähe", "IT", "Leitung IT", "kerstin.kraehe@fintech-austria.local", "+43 660 44332211", 82000),
            ("Elias", "Ente", "R&D", "Leitung R&D", "elias.ente@fintech-austria.local", None, 89000),
            ("Regina", "Reiher", "Finance", "Leitung Finance", "regina.reiher@fintech-austria.local", None, 76000),
            ("Richard", "Rabe", "Marketing", "Leitung Marketing", "richard.rabe@fintech-austria.local", None, 74000),
            ("Alois", "Adler", "Management", "CEO", "alois.adler@fintech-austria.local", None, 120000),
            ("Monika", "Möwe", "Personalabteilung", "Leitung Recruiting", "monika.moewe@fintech-austria.local", None, 70000),
        ])

if __name__ == "__main__":
    create_tables()
    seed_data()
    print(f"Database created at: {DB_PATH}")