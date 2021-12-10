import os
def clear():
    folder_list = os.listdir('D:\BANDHU\Python');
    for i in folder_list:
        if os.path.isdir(i):
            if os.listdir(i) == []:
                os.rmdir(i)
clear();
