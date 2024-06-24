import requests
from bs4 import BeautifulSoup

res = requests.get('https://ssr1.scrape.center/')
soup = BeautifulSoup(res.text, 'html.parser')

message = []
targets = soup.find_all('div', class_='p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16')
for each in targets:
    message.append(each.a.h2.text)
f = open('movie.txt', 'w')
f.writelines(message)
