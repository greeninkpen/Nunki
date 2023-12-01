import mysql.connector
""" 
needed to run: pip install mysql-connector 
instead of: pip install mysql 
for package to install successfully - just
in case anyone else runs into that issue!
-D
"""
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
