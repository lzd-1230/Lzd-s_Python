import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{i}"
    for i in range(1,5)
]


def spider(url):
    res = requests.get(url)
    # print(url,len(res.text))
    return res.text

def parse(html):
    # class="post-item-title"
    soup = BeautifulSoup(html,"lxml")
    links = soup.find_all("a",class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]

if __name__ == "__main__":
    print(parse(spider(urls[0])))