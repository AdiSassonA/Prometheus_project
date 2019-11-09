# This script tests the API server.

import requests
import sys

response = requests.get('http://127.0.0.1:8000')

if response.status_code == 200:
    print("The API server is up and running.")
    sys.exit(0)
else:
    print("Something is wrong with the API server.")
    sys.exit(1)
