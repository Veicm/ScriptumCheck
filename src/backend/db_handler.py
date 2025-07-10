import sqlite3

class DBHandler:
    def __init__(self, db:str="demo.db"):# TODO: replace with actual db.
        connection = sqlite3.connect(f"data/{db}")
        self.cur = connection.cursor()

    def check_if_exists(self, input:any, lection:int):
        self.cur.execute(f"SELECT * FROM lection_{lection} WHERE tribe=?", (input,))
        result = self.cur.fetchone()
        if result is not None:
            found = True
        else:
            found = False
        return found, result


def main():
    db = DBHandler()
    found, result = db.check_if_exists("puell", 1)
    if found:
        print(result[0])
    else:
        print("not founded")

if __name__ == "__main__":
    main()