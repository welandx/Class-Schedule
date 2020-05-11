c= open('curriculum.txt', mode='rb')
import os
c.seek(78,os.SEEK_CUR)
i=1
j=1
from tkinter import *

top = Tk()  # 创建一个窗体
top.geometry("1100x400+200+50") # 改变窗体的大小
while(j<11):
    while (i<6):
        b = c.read(6)
        a = b.decode('utf-8')
        print(a)
        locals()['lesson'+str(i)+str(j)]= {'doweek': i, 'name': a, 'secnum': j}

        c.seek(5, os.SEEK_CUR)
        scr = locals()['lesson'+str(i)+str(j)]['name']
        print(scr)

        # 确认文本的位置
        x = locals()['lesson'+str(i)+str(j)]['doweek']
        y = locals()['lesson'+str(i)+str(j)]['secnum']
        text = Text(top, width=30, height=5)  # 创建一个文本控件
        text.place(x=x * 215 + 10, y=locals()['lesson'+str(i)+str(j)]['secnum'] * 70 + 20)  # 在屏幕上放置文本控件
        text.insert(INSERT, scr)  # 在控件上放置文本

        i=i+1
    j=j+1
    i=1
    c.seek(7, os.SEEK_CUR)
j=11
i=1
c.seek(3, os.SEEK_CUR)
while (i<6):
    b = c.read(6)
    a = b.decode('utf-8')
    print(a)
    locals()['lesson'+str(i)+str(j)]= {'doweek': i, 'name': a, 'secnum': j}
    i=i+1
    c.seek(5, os.SEEK_CUR)
top.mainloop()  # 进入消息循环
