import requests
import sys
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#url = "http://192.168.0.10:8080/"
url = sys.argv[1]

req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')

#print(soup.prettify())
if len(sys.argv) == 2 or sys.argv[2] == "-r":
    for l in soup.find_all('a'):
        print(l.get('href'))
elif sys.argv[2] == "-t":
    print(soup.get_text())
