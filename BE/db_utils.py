import mysql.connector
from BE.config import USER, PASSWORD, HOST


class DBConnectionError(Exception):
    pass

def _connect_to_db(language_game_db):
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return connection