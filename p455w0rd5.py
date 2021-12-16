import sqlite3


def create_table():
    db = sqlite3.connect('.database.db')
    statement = '''CREATE TABLE if not exists MANAGER(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        WEBSITE TEXT NOT NULL,
        PASSWORD TEXT NOT NULL,
        EMAIL TEXT NOT NULL
    );
    '''

    cur = db.cursor()
    cur.execute(statement)
    db.close()
    print('database created successfully!')


create_table()
