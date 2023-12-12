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


def db_add_sentence(sentence):
    try:
        db_name = 'language_game'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = "INSERT INTO sentence (sentence_text) VALUES (%s)"
        values = (sentence,)

        cur.execute(query, values)
        db_connection.commit()
        return "Success"

    except Exception as e:
        print(f"Error: {e}")
        raise DBConnectionError("Failed to insert sentence into sentence table")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def db_add_words(sentence_id, word_text, part_of_speech):
    try:
        db_name = 'language_game'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)
        query_word = "INSERT INTO word(word_text) VALUES (%s, %s)"
        values_word = (word_text, part_of_speech)

        cur.execute(query_word, values_word)
        db_connection.commit()
        return "Success"

    except Exception as e:
        print(f"Error: {e}")
        raise DBConnectionError("Failed to insert data into word table")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# if __name__ == '__main__':
#     db_add_sentence()

