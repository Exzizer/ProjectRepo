import pymysql
# Establishing a connection to DB
from pymysql import IntegrityError


def DB_Action(action, user_name, user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='uy1YDfuk1Y', passwd='3gbgbMmrWo', db='uy1YDfuk1Y')
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    if action == "GET":
        try:
            cursor.execute("SELECT * FROM uy1YDfuk1Y.users WHERE id=" + user_id)
            return cursor._rows[0][1]
        except IndexError:
            return -1

    elif action == "POST":
        try:
            result = cursor.execute(f"INSERT into uy1YDfuk1Y.users (id,name) VALUES ( '{user_id}', '{user_name}')")
            return result
        except IntegrityError:
            return -1

    elif action == "PUT":
        affected_rows = cursor.execute(f"UPDATE uy1YDfuk1Y.users SET name = '{user_name}' WHERE id = {user_id}")
        if affected_rows > 0:
            return 0
        else:
            return -1

    elif action == "DELETE":
        affected_rows = cursor.execute(f"DELETE from uy1YDfuk1Y.users where id = {user_id}")
        if affected_rows > 0:
            return 0
        else:
            return -1

    cursor.close()
    conn.close()