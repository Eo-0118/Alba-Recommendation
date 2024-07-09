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