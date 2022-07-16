import requests
import db_connector
from Project.backend_testing import backend_test
from Project.frontend_testing import selenium_test

try:
    user_name = "test_case_combined"
    user_id = "100"

    backend_test(user_id, user_name)
    result = selenium_test(user_id)
    if result == user_name:
        print("combined test successful!!")

except:
    raise Exception("test failed")
