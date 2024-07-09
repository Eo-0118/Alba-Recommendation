
#알바 정보 크롤링
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


alba_list = []
alba_list_iLink = []

brand_list_2 = soup.find_all('li', attrs={'id': re.compile("^BrandCode")})

for a in brand_list_2:
    x = a.find_all('ul')

    for b in x:
        y = b.find_all('a')
        temp1 = []
        temp2 = []
        for c in y:
            title = c.get_text()
            Link = 'http://www.alba.co.kr' + c['href']
            temp_tuple = (title,Link)
            temp1.append(title)
            temp2.append(temp_tuple)
        alba_list.append(temp1)
        alba_list_iLink.append(temp2)


print(alba_list_iLink)
print(alba_list)

#사용자가 원하는 원하는 직종에 대한 정보 얻기

from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Alba Joa')
root.geometry('540x600')



combobox1 = ttk.Combobox(root, height =5, values=category_list, state='readonly')
combobox1.set('원하는 카테고리를 선택하세요')
combobox1.pack()

def btncmd4():
    user_category_num = combobox1.current()
    combobox2 = ttk.Combobox(root, height=5, values=alba_list[user_category_num], state='readonly')
    combobox2.set('원하는 직종을 선택하세요')
    combobox2.pack()

    def btncmd5():
        user_alba_num = combobox2.current()
        user_alba_link = alba_list_iLink[user_category_num]
        user_alba_link = user_alba_link[user_alba_num]
        user_alba_link = user_alba_link[1]


    btn = Button(root, text='선택', command=btncmd5)
    btn.pack()



btn = Button(root, text='선택', command=btncmd4)
btn.pack()

root.mainloop()


