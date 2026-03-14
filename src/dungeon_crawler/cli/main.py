from dungeon_crawler.db.connection import get_connection
from dungeon_crawler.db.schema import initialize_database


def main() -> None:
    connection = get_connection()
    initialize_database(connection)
    print("Dungeon Crawler project scaffold is ready.")
    print("Next step: add character creation and save/load flows.")


if __name__ == "__main__":
    main()