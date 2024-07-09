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

    print(user_choice_day_string)


btn = Button(root, text='선택', command=btncmd3)
btn.pack()
Label(root, text='지역 선택을 완료하고 창을 닫아주세요').pack()


root.mainloop()