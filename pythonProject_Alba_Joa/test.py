import os

path = "./지역정보"
file_lst = os.listdir(path)

temp = []

for file in file_lst:
    temp.append(file.replace(".txt", ""))
new_file_list = temp

temp = []

for file in file_lst:
    f = open(path + '/' + file, 'r')
    # temp.append(file.replace(".txt",""))
    lines = f.readlines()
    # lines.insert(0,file.replace(".txt",""))
    lines = [line.rstrip('\n') for line in lines]
    temp.append(lines)



from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title('Alba Joa')
root.geometry('540x600')



values = new_file_list
combobox = ttk.Combobox(root, height =5, values=values, state='readonly')
combobox.set('지역을 선택하세요')
combobox.pack()




user_choice_place_num = []
user_choice_place_string = []


def btncmd1():
    info = combobox.current()

    for i in range(len(temp[info])):
        globals()['chkvar{}'.format(i)] = IntVar()
        globals()['chkbox{}'.format(i)]= Checkbutton(root, text='{}'.format(temp[info][i]) , variable=globals()['chkvar{}'.format(i)])
        globals()['chkbox{}'.format(i)].pack()

    def btncmd2():
        for i in range(len(temp[info])):
            globals()['new_info_{}'.format(i)] = globals()['chkvar{}'.format(i)].get()
            if globals()['new_info_{}'.format(i)] == 1:
                user_choice_place_num.append(i)

        for num in user_choice_place_num:
            user_choice_place_string.append(temp[info][num])

        print(user_choice_place_string)

    btn = Button(root, text='선택', command=btncmd2)
    btn.pack()
    Label(root, text = '전체를 선택하고 싶을 경우 전체만 체크해주세요'
                       + '\n' + '지역 선택을 완료하고 창을 닫아주세요'
                       + '\n' + '지역 최대 5까지 선택가능합니다.').pack()


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

    print(user_choice_day_string)


btn = Button(root, text='선택', command=btncmd3)
btn.pack()
Label(root, text='지역 선택을 완료하고 창을 닫아주세요').pack()


root.mainloop()