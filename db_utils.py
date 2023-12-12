import mysql.connector
from config import USER, PASSWORD, HOST


class DBConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection


def get_sentence():
    try:
        db_name = 'language_game'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "SELECT sentence_text FROM sentence ORDER BY RAND() LIMIT 1;"
        cur.execute(query)

        result = cur.fetchone()
        if result:
            return result[0]

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return None
