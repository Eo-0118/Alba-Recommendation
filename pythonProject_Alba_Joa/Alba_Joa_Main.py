#지역정보 폴더에 있는 지역정보 읽어오기

import os

path = "./지역정보"
file_lst = os.listdir(path)

temp = []

for file in file_lst:
    temp.append(file.replace(".txt", ""))
new_file_list = temp

jun_gu_list = []

for file in file_lst:
    f = open(path + '/' + file, 'r')
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    jun_gu_list.append(lines)

#사용자 거주 지역에 대한 정보 얻기
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Alba Joa')
root.geometry('540x600')

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, '현재 거주하시는 장소를 자세하게 적어주세요' + '\n' + '예시)경기 용인시 기흥구 덕영대로 1732')

def btncmd5():
    global user_location
    user_location = txt.get('1.0', END)

btn = Button(root, text='완료', command=btncmd5)
btn.pack()
Label(root, text = '거주 지역을 입력하고 완료버튼을 누른 후 창을 닫아주세요').pack()


root.mainloop()

# 사용자가 알바를 원하는 장소에 대한 정보 얻기

from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Alba Joa')
root.geometry('540x700')



values = new_file_list
combobox = ttk.Combobox(root, height =5, values=values, state='readonly')
combobox.set('지역을 선택하세요')
combobox.pack()




user_choice_place_num = []
user_choice_place_string = []


def btncmd1():
    info = combobox.current()
    global user_si
    user_si = combobox.get()
    for i in range(len(jun_gu_list[info])):
        globals()['chkvar{}'.format(i)] = IntVar()
        globals()['chkbox{}'.format(i)]= Checkbutton(root, text='{}'.format(jun_gu_list[info][i]) , variable=globals()['chkvar{}'.format(i)])
        globals()['chkbox{}'.format(i)].pack()

    def btncmd2():
        for i in range(len(jun_gu_list[info])):
            globals()['new_info_{}'.format(i)] = globals()['chkvar{}'.format(i)].get()
            if globals()['new_info_{}'.format(i)] == 1:
                user_choice_place_num.append(i)

        for num in user_choice_place_num:
            user_choice_place_string.append(jun_gu_list[info][num])


    btn = Button(root, text='선택', command=btncmd2)
    btn.pack()
    Label(root, text = '지역 선택을 완료하고 창을 닫아주세요' + '\n' + '지역 최대 5까지 선택가능합니다.').pack()


btn = Button(root, text='선택', command=btncmd1)
btn.pack()

root.mainloop()

if len(user_choice_place_string) > 5:
    root = Tk()
    root.title('Alba Joa')
    root.geometry('540x600')
    Label(root, text='지역을 5개이하로 선택해주세요....' + '\n' + '창을 닫고 재시작해주세요').pack()
    root.mainloop()
    raise Exception("지역 5개이하로 선택하는거 잊지 말기!!")


#사용자가 알바를 원하는 요일에 대한 정보 얻기

from tkinter import *

root = Tk()
root.title('Alba Joa')
root.geometry('540x600')

day_list = ['월','화','수','목','금','토','일']
user_choice_day_num = []
user_choice_day_string = []

for i in range(len(day_list)):
    globals()['chkvar_{}'.format(i)] = IntVar()
    globals()['chkbox_{}'.format(i)] = Checkbutton(root, text='{}'.format(day_list[i]),variable=globals()['chkvar_{}'.format(i)])
    globals()['chkbox_{}'.format(i)].pack()

def btncmd3():
    for i in range(len(day_list)):
        globals()['info_{}'.format(i)] = globals()['chkvar_{}'.format(i)].get()
        if globals()['info_{}'.format(i)] == 1:
            user_choice_day_num.append(i)

    for num in user_choice_day_num:
        user_choice_day_string.append(day_list[num])


btn = Button(root, text='선택', command=btncmd3)
btn.pack()
Label(root, text='요일 선택을 완료하고 창을 닫아주세요').pack()

root.mainloop()


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
        global user_alba_link
        user_alba_num = combobox2.current()
        user_alba_link = alba_list_iLink[user_category_num]
        user_alba_link = user_alba_link[user_alba_num]
        user_alba_link = user_alba_link[1]



    btn = Button(root, text='선택', command=btncmd5)
    btn.pack()



btn = Button(root, text='선택', command=btncmd4)
btn.pack()

root.mainloop()

from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re



options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome("./chromedriver", options=options)
browser.get(user_alba_link)
browser.implicitly_wait(time_to_wait=1000)



browser.find_element(By.XPATH,'//*[@id="schWorkWeek"]/dd/ul/li[6]/span/label').click()
browser.implicitly_wait(time_to_wait=1000)

user_choice_day = []

Mon_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[1]/span/label'
Tue_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[2]/span/label'
Wed_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[3]/span/label'
Thu_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[4]/span/label'
Fri_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[5]/span/label'
Sat_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[6]/span/label'
Sun_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[7]/span/label'

if '월' in user_choice_day_string:
    user_choice_day.append(Mon_xpath)
if '화' in user_choice_day_string:
    user_choice_day.append(Tue_xpath)
if '수' in user_choice_day_string:
    user_choice_day.append(Wed_xpath)
if '목' in user_choice_day_string:
    user_choice_day.append(Thu_xpath)
if '금' in user_choice_day_string:
    user_choice_day.append(Fri_xpath)
if '토' in user_choice_day_string:
    user_choice_day.append(Sat_xpath)
if '일' in user_choice_day_string:
    user_choice_day.append(Sun_xpath)

for i in range(len(user_choice_day)):
    browser.find_element(By.XPATH,user_choice_day[i]).click()

browser.find_element(By.XPATH,'//*[@id="JobSearch"]/fieldset/div[4]/div[2]/a[1]').click()
browser.find_element(By.XPATH,'//*[@id="NormalInfo"]/div[2]/span[1]/a[1]').click()

url = browser.current_url


Every_info = []
temp = []
temp1 = []
temp2 = []
temp3 = []


for i in range(11):
    url = url.replace('page={}'.format(i),'page={}'.format(i+1))
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        pass

    soup = BeautifulSoup(res.text, 'html.parser')


    alba_title_list = soup.find_all('span', attrs={'class':'company'})
    for title in alba_title_list:
        title = title.text
        temp.append(title)


    alba_money_list = soup.find_all('span', attrs={'class':'number'})
    for money in alba_money_list:
        money = money.text
        temp1.append(money)


    alba_time_list = soup.find_all('td', attrs={'class':'data'})
    for time in alba_time_list:
        time = time.text
        temp2.append(time)


    alba_place_list = soup.find_all('td', attrs={'class':'local first'})
    for place in alba_place_list:
        place = place.text
        temp3.append(place)

    for i in range(len(temp)):
        Sum = (temp3[i],temp[i],temp1[i],temp2[i])
        Every_info.append(Sum)


user_fit_alba = []

#필터링

for i in range(len(Every_info)):
    for j in range(len(user_choice_place_string)):
        if Every_info[i][0] == user_si + ' ' +user_choice_place_string[j]:
            user_fit_alba.append(Every_info[i])


#중복 제거
import sys
user_fit_alba_del = []
for v in user_fit_alba:
    if v not in user_fit_alba_del:
        user_fit_alba_del.append(v)


if user_fit_alba_del == []:
    print('맞춤 알바가 없습니다...' + '\n' + '프로그램을 종료합니다')
    sys.exit()


#아르바이트와 사용자 사이의 거리 측정
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome("./chromedriver", options=options)
browser.get("https://map.naver.com/v5/directions")
browser.implicitly_wait(time_to_wait=1000)



elem = browser.find_element(By.XPATH,'//*[@id="directionStart0"]')
elem.send_keys(user_location + Keys.RETURN)
elem.send_keys(Keys.RETURN)

Time_list = []

for i in range(len(user_fit_alba_del)):
    choice = user_fit_alba_del[i][1]
    elem_2 = browser.find_element(By.XPATH,'//*[@id="directionGoal1"]')
    elem_2.send_keys(choice + Keys.RETURN)
    elem_2.send_keys(Keys.RETURN)

    elem_3 = browser.find_element(By.XPATH,'//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/div/directions-search/div[2]/button[2]')
    elem_3.click()

    WebDriverWait(browser, 1000).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/shrinkable-layout/div/directions-layout/directions-result/div[1]/directions-summary-list/directions-hover-scroll/div/div/directions-summary-item-pubtransit[1]/div[1]/strong/readable-duration')))

    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")


    Time_list = soup.find_all('readable-duration')
    Real_Time_list = Time_list[0::2]

    temp = []

    for time in Real_Time_list:
        Time = time.text
        Time = int(Time.replace("분",""))
        temp.append(Time)


    #상위 다섯개만 선정

    temp.sort()
    temp = temp[0:4]

    Time_Average = str(round(sum(temp)/len(temp)))
    print(Time_Average + "분")

    Time_list = moving_time.append(Time_Average)


for i in range(len(Time_list)):
    print(user_fit_alba_del[i][0], user_fit_alba_del[i][1], user_fit_alba_del[i][2], user_fit_alba_del[i][3], Time_list[i])
