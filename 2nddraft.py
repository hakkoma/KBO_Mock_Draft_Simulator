import requests
from bs4 import BeautifulSoup as BS

req = requests.get('https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8/2017%EB%85%84/%EC%8B%A0%EC%9D%B8%EB%93%9C%EB%9E%98%ED%94%84%ED%8A%B8')

html = BS(req.text, 'html.parser')

print(html)
