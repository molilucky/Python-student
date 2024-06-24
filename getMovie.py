import bs4
import requests

res = requests.get("https://ssr1.scrape.center/")
# print(res.text)

soup = bs4.BeautifulSoup(res.text, "html.parser")
# targets = soup.find_all("div", class_="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16")
# for each in targets:
#     print(each.a.h2.text)

massages = []
targets = soup.find_all("div", class_="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16")
for each in targets:
    result = [i.span.text for i in each.find_all(class_='m-v-sm info') if i.span and i.span.text]
    massages.append(result)
print(massages)

