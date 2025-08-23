import sqlite3
from typing import Optional

class DBHandler:
    """
    Handles all database interactions.

    Attributes:
        db (str): The file name of the target database in scr/data. Defaults to "vocabulary.db".
    """
    def __init__(self, db: str = "vocabulary.db"):
        connection = sqlite3.connect(f"data/{db}",check_same_thread=False)
        self.cur = connection.cursor()

    def check_if_exists(self, input: str, lection: int) -> tuple[bool, Optional[tuple[int, str, str, str]]]:
        """
        Checks if a word with the steam which matches the given input is included in the given
        lection of the database.

        Args:
            input (str): The steam which should match with the steam of a word in the database.
            lection (int): The lection witch should be scanned if the given steam is included.

        Returns:
            tuple[bool, Optional[tuple[int, str, str, str]]]:  
                A tuple containing:
                    - A boolean indicating whether a matching entry was found.
                    - A tuple with the database row values (id, vocab, tribe, german translation)  
                    if found, or None if no match was found.
        """
        self.cur.execute(f"SELECT * FROM lection_{lection} WHERE steam=?", (input,))
        result: Optional[tuple[int, str, str, str]] = self.cur.fetchone()
        if result is not None:
            found: bool = True
        else:
            found: bool = False
        return found, result


def main() -> None:
    db: DBHandler = DBHandler("demo.db")# TODO: Replace with actual database
    found, result = db.check_if_exists("puell", 1)
    if found:
        print(result[0])
    else:
        print("Not founded")

if __name__ == "__main__":
    main()