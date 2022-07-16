from flask import Flask, request
import pymysql
# Establishing a connection to DB
from pymysql import IntegrityError
import os
import signal
conn = pymysql.connect(host='remotemysql.com', port=3306, user='uy1YDfuk1Y', passwd='3gbgbMmrWo', db='uy1YDfuk1Y')
conn.autocommit(True)

app = Flask(__name__)
def get_html_string(h1_id,h1_string):
    html_string = f'<body style="background-color: aliceblue;">' \
                    '<div style="justify-content: center; align-items: center; display: flex; height: 20%; background-color: lightblue;">' \
                        f'<h1 id="{h1_id}" style="color: darkslateblue; font-family: Segoe UI;">' \
                            f'{h1_string}' \
                        '</h1>' \
                    '</div>' \
                  '</body>'
    return html_string

@app.route('/users/get_user_data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        try:
            # Getting a cursor from Database
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM uy1YDfuk1Y.users WHERE id=" + user_id)
            user_name = cursor._rows[0][1]
            cursor.close()

            return get_html_string("user", user_name), 200
        except IndexError:
            return get_html_string("error", "No such user found"), 500

@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5001)