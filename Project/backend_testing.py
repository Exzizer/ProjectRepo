import requests
import db_connector


def backend_test(user_id, user_name):
    try:
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        result = db_connector.db_action("DELETE", user_id=99, user_name="")
        res = requests.post('http://127.0.0.1:5000/users/'+user_id, json={"user_name": user_name}, headers=headers)
        if res.status_code == 200:
            res = requests.get('http://127.0.0.1:5000/users/'+user_id, headers=headers)
            if res.status_code == 200:
                result = db_connector.db_action("GET", user_id=user_id, user_name="")
                if result == user_name:
                    print("backend test success")

    except:
        raise Exception("test failed")


backend_test("99", "test_case_99")
