import requests
from bs4 import BeautifulSoup
import re

url = "http://www.alba.co.kr/job/annex/Brand.asp"
headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }

res = requests.get(url)
res.raise_for_status()
html = res.content.decode('euc-kr','replace')
soup = BeautifulSoup(html, "html.parser")


category_list = []

brand_list = soup.find('div', attrs={'class': "brandList"}).find_all('h2')

for brands in brand_list:
    category = brands.get_text()
    category = category.replace("더보기","")
    category_list.append(category)
print(category_list)


alba_list = []

brand_list_2 = soup.find_all('li', attrs={'id': re.compile("^BrandCode")})

for a in brand_list_2:
    x = a.find_all('ul')

    for b in x:
        y = b.find_all('a')
        temp = []
        for c in y:
            title = c.get_text()
            Link = 'http://www.alba.co.kr' + c['href']
            temp_tuple = (title,Link)
            temp.append(temp_tuple)
        alba_list.append(temp)


for i in range(len(alba_list)):
    print(alba_list[i])




