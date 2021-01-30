from bs4 import BeautifulSoup
import hashlib
import requests

url = 'http://167.99.88.216:30926/'
r = requests.session()

print("Fetching page...")
req = r.get(url)

print("Parsing HTML...")
soup = BeautifulSoup(req.content,'html.parser')

string = soup.find('h3').text
print("String:", string)

print("Hashing String...")
hashed_string = hashlib.md5(string.encode()).hexdigest()

print("Hashed String:", hashed_string)

print("Sending Data...")
cookie = {'PHPSESSID': '9hq1suro84k4pmp6leiln3tog1'}
res = requests.post(url=url, cookies=cookie, data={'hash': hashed_string})

print(res.text)
