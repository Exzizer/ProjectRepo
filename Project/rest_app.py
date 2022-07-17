from flask import Flask, request
import pymysql
import os
import signal
# Establishing a connection to DB
from pymysql import IntegrityError

from db_connector import db_action

conn = pymysql.connect(host='remotemysql.com', port=3306, user='uy1YDfuk1Y', passwd='3gbgbMmrWo', db='uy1YDfuk1Y')
conn.autocommit(True)

app = Flask(__name__)


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        result = db_action("GET", user_id=user_id, user_name="")
        if result != -1:
            return {"status": "ok", "user_name": result}, 200
        else:
            return {"status":"error","reason":"no such id"},500

    elif request.method == 'POST':

        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        result = db_action("POST", user_name=user_name, user_id=user_id)

        if result != -1:
            return {"status": "ok", "user_added": user_name}, 200
        else:
            return {"status": "error", "reason": "id already exists"}, 500

    elif request.method == 'PUT':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')

        result = db_action("PUT", user_name=user_name, user_id=user_id)

        if result != -1:
            return {"status": "ok", "user_updated": user_name}, 200
        else:
            return {"status": "error", "reason": "no such id or new name not different"}, 500

    elif request.method == 'DELETE':
        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')

        result = db_action("DELETE", user_name="", user_id=user_id)

        if result != -1:
            return {"status": "ok", "user_deleted": user_name}, 200
        else:
            return {"status": "error", "reason": "no such id"}, 500


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)