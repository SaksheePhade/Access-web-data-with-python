#iss open api
import requests
import urllib.request
from urllib.parse import urlparse


response1 = request.get("http://api.open-notify.org/iss-now.json")
response = urllib.request.urlopen("http://api.open-notify.org/iss-now.json")
html = response.read()
#print(html.iss_position)
parsed = urlparse("http://api.open-notify.org/iss-now.json")
print(parsed)