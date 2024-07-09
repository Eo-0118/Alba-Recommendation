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
elem.send_keys("경기도 성남시 분당구 미금일로58" + Keys.RETURN)
elem.send_keys(Keys.RETURN)

choice = "지코바정자1호점"

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

# print('걷는 시간')
# for walking_time in Walking_Time_list:
#     Walking_Time = walking_time.text
#     print(Walking_Time)
