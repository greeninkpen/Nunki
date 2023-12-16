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
    db_name = 'language_game'
    db_connection = _connect_to_db(db_name)
    try:

        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "INSERT INTO sentence (sentence_text) VALUES (%s)"
        values = (sentence,)
        cur.execute(query, values)  # has to execute before lastrowid can be used
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

            sql_insert = "INSERT INTO sentence_word (sentence_id, word_id) VALUES (%s, %s)"
            values = (sentence_id, word_id)
            cur.execute(sql_insert, values)

        db_connection.commit()
        return "Success"

    except Exception as e:
        print(f"Error: {e}")
        raise DBConnectionError("Failed to insert sentence into sentence table")



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

def get_glossary():
    try:
        db_name = 'language_game'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "SELECT * FROM glossary;"
        cur.execute(query)

        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]

        result = [dict(zip(columns, row)) for row in rows]

        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

def get_game_dict():
    try:
        db_name = 'language_game'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
                            SELECT w.word_text, w.part_of_speech
                            FROM sentence s
                            JOIN sentence_word sw ON s.sentence_id = sw.sentence_id
                            JOIN word w ON sw.word_id = w.word_id
                            WHERE s.sentence_text = 'I like apples';
                            """
        cur.execute(query)

        rows = cur.fetchone()
        columns = [desc[0] for desc in cur.description]

        result = [dict(zip(columns, row)) for row in rows]

        return result

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

