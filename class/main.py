
c= open('curriculum.txt', mode='rb')  # 打开文件
import os
c.seek(78,os.SEEK_CUR)  # 移动指针
i=1
j=1
from tkinter import *
import re

class Lesson:
    list1 = []  # 存放所有课程信息
    # 测试函数
    def judge(self,var):
        if re.match('星期\d',var):
            x=re.search('\d',var)
            self.doweekseek(int(x.group()))
        elif re.match('第\d节',var):
            x = re.search('\d', var)
            self.secnumseek(int(x.group()))
        elif re.match('[^x00-xff]',var):
            x=re.match('[^x00-xff]+',var)
            print(x.group())
            self.nameseek(x.group())
    def doweekseek(self,var):
        text = Text(top, width=17, height=11)  # 创建文本控件
        text.place(x=1,y=1)  # 在屏幕上放置文本控件
        for x in self.list1:
            if x['doweek']==var:
                src='星期%d 第%s节 %s' %(x['doweek'],x['secnum'],x['name'])
                text.insert(INSERT,src)  # 在控件上放置文本
    def secnumseek(self,var):
        text = Text(top, width=17, height=11)  # 创建文本控件
        text.place(x=1, y=1)  # 在屏幕上放置文本控件
        for x in self.list1:
            if x['secnum'] == var:
                src = '星期%d 第%s节 %s' % (x['doweek'], x['secnum'], x['name'])
                text.insert(INSERT, src)  # 在控件上放置文本
    def nameseek(self,var):
        text = Text(top, width=17, height=11)  # 创建文本控件
        text.place(x=1, y=1)  # 在屏幕上放置文本控件
        for x in self.list1:
            if x['name'] == var:
                src = '星期%d 第%s节 %s' % (x['doweek'], x['secnum'], x['name'])
                text.insert(INSERT, src)  # 在控件上放置文本
lesson1=Lesson()


top = Tk()  # 创建一个窗体
top.geometry("1100x400+200+50")  # 改变窗体的大小


# 读取与显示
while(j<11):
    while (i<6):
        b = c.read(6)
        a = b.decode('utf-8')
        locals()['lesson'+str(i)+str(j)]= {'doweek': i, 'name': a, 'secnum': j}
        lesson1.list1.append(locals()['lesson'+str(i)+str(j)])  # 存入list1
        c.seek(5, os.SEEK_CUR)  # 指针移动
        scr = locals()['lesson'+str(i)+str(j)]['name']

        # 确认文本的位置
        x = locals()['lesson'+str(i)+str(j)]['doweek']
        y = locals()['lesson'+str(i)+str(j)]['secnum']
        text = Text(top, width=30, height=5)  # 创建一个文本控件
        text.place(x=x * 215 + 80, y=locals()['lesson'+str(i)+str(j)]['secnum'] * 70 + 30)  # 在屏幕上放置文本控件
        text.insert(INSERT, scr)  # 在控件上放置文本

        i=i+1
    j=j+1
    i=1
    c.seek(7, os.SEEK_CUR)  # 指针移动
j=11
i=1
c.seek(3, os.SEEK_CUR)  # 指针移动
while (i<6):
    b = c.read(6)
    a = b.decode('utf-8')
    locals()['lesson'+str(i)+str(j)]= {'doweek': i, 'name': a, 'secnum': j}
    c.seek(5, os.SEEK_CUR)  # 指针移动
    lesson1.list1.append(locals()['lesson' + str(i) + str(j)])  # 存入list1
    scr = locals()['lesson' + str(i) + str(j)]['name']
    x = locals()['lesson' + str(i) + str(j)]['doweek']
    y = locals()['lesson' + str(i) + str(j)]['secnum']
    text = Text(top, width=30, height=5)  # 创建一个文本控件
    text.place(x=x * 215 + 80, y=locals()['lesson' + str(i) + str(j)]['secnum'] * 70 + 30)  # 在屏幕上放置文本控件
    text.insert(INSERT, scr)  # 在控件上放置文本
    i=i+1


# 放置输入框
entry=Entry(top,bd=4)
entry.pack()

# 搜索按钮
def insert_point():
    var = entry.get()  # 获取输入内容
    lesson1.judge(var)  # 测试
b1 = Button(top,text="搜索",width=15,height=2,command=insert_point)  # 按钮，绑定事件insert_input
b1.pack()

# 放置表格
i=1
while(i<6):
    text = Text(top, width=30, height=1)
    text.place(x=295+(i-1)*215,y=80)
    text.insert(INSERT,'星期%s' %i)
    i+=1
i=1
while(i<12):
    text = Text(top, width=10, height=5)
    text.place(x=220, y=100+(i-1)*70)
    text.insert(INSERT, '第%s节' % i)
    i += 1
top.mainloop()  # 进入消息循环