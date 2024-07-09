from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


Every_info = []
temp = []
temp1 = []
temp2 = []
temp3 = []


for i in range(1,11):
    url ='https://www.alba.co.kr/job/annex/brandlist.asp?page={}&pagesize=50&schtext=1205D003&categ=&brandname=%BC%BC%BA%EC%C0%CF%B7%B9%BA%EC&sidocd=&gugun=&dong=&d_area=&d_areacd=&strAreaMulti=&hidJobKind=&hidJobKindMulti=&WorkTime=&searchterm=&AcceptMethod=&ElecContract=&HireTypeCD=&CareerCD=&CareercdUnRelated=&LastSchoolCD=&LastSchoolcdUnRelated=&GenderCD=&GenderUnRelated=&AgeLimit=0&AgeUnRelated=&PayCD=&PayStart=&WelfareCD=&Special=&WorkWeekCD=D07&WeekDays=C01,%20C02,%20C03&hidSortCnt=50&hidSortOrder=&hidSortDate=&WorkPeriodCD=&hidSort=&hidSortFilter=Y&hidListView=LIST&WsSrchKeywordWord=&hidWsearchInOut=&hidSchContainText='.format(i)
    print(url)
    res = requests.get(url)
    try:
        res.raise_for_status()
    except:
        pass

    soup = BeautifulSoup(res.text, 'html.parser')


    num = soup.find('a', attrs={'class':"page"})
    print(num)




    alba_title_list = soup.find_all('span', attrs={'class':'company'})
    for title in alba_title_list:
        title = title.text
        temp.append(title)
    print(temp)


    alba_money_list = soup.find_all('span', attrs={'class':'number'})
    for money in alba_money_list:
        money = money.text
        temp1.append(money)
    print(temp1)


    alba_time_list = soup.find_all('td', attrs={'class':'data'})
    for time in alba_time_list:
        time = time.text
        temp2.append(time)
    print(temp2)


    alba_place_list = soup.find_all('td', attrs={'class':'local first'})
    for place in alba_place_list:
        place = place.text
        temp3.append(place)
    print(temp3)

    for i in range(len(temp)):
        Sum = (temp3[i],temp[i],temp1[i],temp2[i])
        Every_info.append(Sum)
    print(Every_info)
