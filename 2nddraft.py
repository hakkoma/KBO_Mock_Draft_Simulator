import urllib
import requests
from bs4 import BeautifulSoup

res = urllib.requests.get('https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8/2017%EB%85%84/%EC%8B%A0%EC%9D%B8%EB%93%9C%EB%9E%98%ED%94%84%ED%8A%B8')

soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find('title')

print(title.string())
print(title.get_text())
