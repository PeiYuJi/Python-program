import urllib.request as req
import ssl
ssl._create_default_https_context=ssl._create_unverified_context
from openpyxl import Workbook, load_workbook
url="https://www.ptt.cc/bbs/job/index.html"
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
print(data)

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
print(root.title.string)
titles=root.find_all("div",class_="title")
print(titles)

for title in titles:
    if title.a != None:
        print(title.a.string)

