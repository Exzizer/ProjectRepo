import requests

try:
    requests.get('http://127.0.0.1:5000/stop_server')
except:
    print("Server 5000 not responding.")

try:
    requests.get('http://127.0.0.1:5001/stop_server')
except:
    print("Server 5001 not responding.")