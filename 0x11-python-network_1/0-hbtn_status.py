#!/usr/bin/python3
# script that retrieve data from response
import urllib
from urllib import request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    data = response.read()
print("Body response:")
print("- type: ", type(data))
print("- content:", data)
print("- utf8 content:", data.decode("utf-8"))
