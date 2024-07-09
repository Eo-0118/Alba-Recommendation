#사용자 거주 지역에 대한 정보 얻기
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Alba Joa')
root.geometry('540x600')

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, '현재 거주하시는 장소를 자세하게 적어주세요' + '\n' + '예시)경기 용인시 기흥구 덕영대로 1732 경희대학교')

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
txt.insert(END, '현재 거주하시는 장소를 자세하게 적어주세요' + '\n' + '예시)경기 용인시 기흥구 덕영대로 1732 경희대학교')

def btncmd5():
    global user_location
    user_location = txt.get('1.0', END)

btn = Button(root, text='완료', command=btncmd5)
btn.pack()
Label(root, text = '거주 지역을 입력하고 완료버튼을 누른 후 창을 닫아주세요').pack()

root.mainloop()
