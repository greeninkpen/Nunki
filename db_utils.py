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

def db_add_sentence_and_words(sentence, words):
    sentence_id = 0
    try:
        db_name = 'language_game'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "INSERT INTO sentence (sentence_text) VALUES (%s)"
        values = (sentence,)
        cur.execute(query, values) # has to execute before lastrowid can be used
        sentence_id = cur.lastrowid
        print("SENTENCE ID: ")
        print(sentence_id)

        for element in words:
            sql_insert = "INSERT INTO word (word_text, part_of_speech) VALUES (%s, %s)"
            values = (element["word"], element["part_of_speech"])
            cur.execute(sql_insert, values)
            word_id = cur.lastrowid
            print("WORD ID: ")
            print(word_id)

            sql_insert = "INSERT INTO sentence_word (sentence_id, word_id) VALUES (%d, %d)"
            values = (sentence_id, word_id)
            cur.execute(sql_insert, values)

        db_connection.commit()
        return "Success"


    except Exception as e:
        print(f"Error: {e}")
        raise DBConnectionError("Failed to insert sentence into sentence table")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


