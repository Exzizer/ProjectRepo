import pymysql
# Establishing a connection to DB
from pymysql import IntegrityError


def db_action(action, user_name, user_id):
    conn = pymysql.connect(host='sql.freedb.tech', port=3306, user='freedb_my_db_user', passwd='k@6*XvNGS!!ftxC', db='freedb_my_database')
    conn.autocommit(True)
    # Getting a cursor from Database
    cursor = conn.cursor()
    if action == "GET":
        try:
            cursor.execute("SELECT * FROM freedb_my_database.users WHERE user_id=" + user_id)
            return cursor._rows[0][1]
        except IndexError:
            return -1

    elif action == "POST":
        try:
            result = cursor.execute(f"INSERT into freedb_my_database.users (user_id,user_name) VALUES ( '{user_id}', '{user_name}')")
            return result
        except IntegrityError:
            return -1

    elif action == "PUT":
        affected_rows = cursor.execute(f"UPDATE freedb_my_database.users SET user_name = '{user_name}' WHERE user_id = {user_id}")
        if affected_rows > 0:
            return 0
        else:
            return -1

    elif action == "DELETE":
        affected_rows = cursor.execute(f"DELETE from freedb_my_database.users where user_id = {user_id}")
        if affected_rows > 0:
            return 0
        else:
            return -1

    cursor.close()
    conn.close()

