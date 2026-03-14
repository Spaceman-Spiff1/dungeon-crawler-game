import sqlite3


def initialize_database(connection: sqlite3.Connection) -> None:
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            character_class TEXT NOT NULL,
            strength INTEGER NOT NULL,
            intelligence INTEGER NOT NULL,
            dexterity INTEGER NOT NULL,
            luck INTEGER NOT NULL,
            health INTEGER NOT NULL,
            mana INTEGER NOT NULL DEFAULT 0
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            slot TEXT NOT NULL,
            rarity TEXT NOT NULL,
            strength_bonus INTEGER NOT NULL DEFAULT 0,
            intelligence_bonus INTEGER NOT NULL DEFAULT 0,
            dexterity_bonus INTEGER NOT NULL DEFAULT 0,
            luck_bonus INTEGER NOT NULL DEFAULT 0,
            health_bonus INTEGER NOT NULL DEFAULT 0,
            mana_bonus INTEGER NOT NULL DEFAULT 0
        )
        """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            character_id INTEGER NOT NULL,
            item_id INTEGER NOT NULL,
            equipped INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (character_id) REFERENCES characters (id),
            FOREIGN KEY (item_id) REFERENCES items (id)
        )
        """
    )

    connection.commit()