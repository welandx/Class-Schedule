
c= open('curriculum.txt', mode='rb')  # 打开文件
import os
def move(x):
    c.seek(x,os.SEEK_CUR)  # 移动指针
def setext():
    pass
move(78)
i=1
j=1
from tkinter import *
import re

class Lesson:
    list1 = []  # 存放所有课程信息
    asw=[]
    answer=[]
    # 测试函数
    def judge(self,var):
        # 搜索
        self.search1(var,'doweek','星期\d','\d')
        self.search1(var,'secnum','第\d节','\d')
        self.search2(var,'name',r'\b[^x00-xff]+\b')

        # 筛选结果
        k=0
        for dict in self.asw:
            j=0
            for item in self.asw:

                if dict['doweek'] == item['doweek'] and dict['secnum'] == item['secnum'] and k!=j:
                    self.answer.append(dict)  # 相同的元素保留
                else:
                    pass
                j+=1
            k+=1
        if self.answer==[]:
            self.answer=self.asw  # 无相同元素直接输出asw
        # 去重算法，无用
        from functools import reduce
        run_function = lambda x, y: x if y in x else x+[y]
        self.answer = reduce(run_function, [[], ] + self.answer)

        # 放置消息
        from tkinter import messagebox
        messagebox
        text = Text(top, width=17, height=11)  # 创建文本控件
        text.place(x=1,y=1)  # 在屏幕上放置文本控件
        for x in self.answer:
            src = '星期%d 第%s节 %s' % (x['doweek'], x['secnum'], x['name'])
            text.insert(INSERT, src)  # 在控件上放置文本
    def search1(self,var,key,mtcsrc,mtc1):
        if re.search(mtcsrc,var):
            x=re.search(mtcsrc,var)
            x=x.group()
            x1=re.search(mtc1,x)
            for x in self.list1:
                if x[key]==int(x1.group()):
                    self.asw.append(x)
    def search2(self, var, key, mtcsrc):
        if re.search(mtcsrc, var):
            a=re.search(mtcsrc, var)
            x1=a.group()
            x1=x1.strip()
            for x in self.list1:
                if x[key] == x1:
                    self.asw.append(x)
lesson1=Lesson()


top = Tk()  # 创建一个窗体
top.geometry("1100x400+200+50")  # 改变窗体的大小

# 读取与显示
def fuc():
    i=1
    while (i<6):
        b = c.read(6)
        a = b.decode('utf-8')
        locals()['lesson'+str(i)+str(j)]= {'doweek': i, 'name': a, 'secnum': j}
        lesson1.list1.append(locals()['lesson'+str(i)+str(j)])  # 存入list1
        move(5)  # 指针移动
        scr = locals()['lesson'+str(i)+str(j)]['name']

        # 确认文本的位置
        x = locals()['lesson'+str(i)+str(j)]['doweek']
        y = locals()['lesson'+str(i)+str(j)]['secnum']
        text = Text(top, width=30, height=5)  # 创建一个文本控件
        text.place(x=x * 215 + 80, y=locals()['lesson'+str(i)+str(j)]['secnum'] * 70 + 30)  # 在屏幕上放置文本控件
        text.insert(INSERT, scr)  # 在控件上放置文本

        i=i+1
while(j<11):
    fuc()
    j=j+1
    move(7)  # 指针移动
j=11
move(3)  # 指针移动
fuc()


# 放置输入框
entry=Entry(top,bd=4)
entry.pack()

# 搜索按钮
def insert_point():
    var = entry.get()  # 获取输入内容
    print(type(var))
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