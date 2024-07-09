from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re



options = webdriver.ChromeOptions()
options.add_argument("headless")
browser = webdriver.Chrome("./chromedriver", options=options)
browser.get('http://www.alba.co.kr/job/annex/BrandList.asp?schtext=1205D003&categ=%C6%ED%C0%C7%C1%A1&brandname=%BC%BC%BA%EC%C0%CF%B7%B9%BA%EC')
browser.implicitly_wait(time_to_wait=1000)



browser.find_element(By.XPATH,'//*[@id="schWorkWeek"]/dd/ul/li[6]/span/label').click()
browser.implicitly_wait(time_to_wait=1000)

Mon_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[1]/span/label'
Tue_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[2]/span/label'
Wed_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[3]/span/label'
Thu_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[4]/span/label'
Fri_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[5]/span/label'
Sat_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[6]/span/label'
Sun_xpath = '//*[@id="schWorkWeek"]/dd/ul/li[6]/div/ul/li[7]/span/label'

browser.find_element(By.XPATH,Fri_xpath).click()
browser.find_element(By.XPATH,Sat_xpath).click()
browser.find_element(By.XPATH,Sun_xpath).click()
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
for i in range (len(Every_info)):
    if Every_info[i][0] == '경기 수원시 영통구':
        user_fit_alba.append(Every_info[i])

    user_fit_alba_del = []
    for v in user_fit_alba:
        if v not in user_fit_alba_del:
            user_fit_alba_del.append(v)

print(user_fit_alba_del)
