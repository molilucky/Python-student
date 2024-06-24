import bs4
import requests


def open_url(url):
    res = requests.get(url)
    return res


def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    #电影名
    movies = []
    targets = soup.find_all("div", class_="p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16")
    for each in targets:
        movies.append(each.a.h2.text)
    #评分
    ranks = []
    targets = soup.find_all("div", class_="el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4")
    for each in targets:
        ranks.append(each.p.text)
    #资料

    messages = []
    targets = soup.find_all("div", "p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16")
    for each in targets:
        result = [i.span.text for i in each.find_all(class_='m-v-sm info') if i.span and i.span.text]
        messages.append(result)


    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + '\n' + ranks[i].strip() + str(messages[i]) + '\n'*2)
    return result


#找出有多少页面
def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    result = soup.find_all('li', class_='number')
    depth = result[-1].text
    return int(depth.strip())


def main():
    host = "https://ssr1.scrape.center"
    res = open_url(host)
    depth = find_depth(res)

    result = []
    for i in range(1, depth):
        url = host + '/page/' + str(i)
        res = open_url(url)
        result.extend(find_movies(res))

    with open('movies.md', 'w', encoding="utf8") as f:
        for each in result:
            f.write(each)


if __name__ == '__main__':
    main()
