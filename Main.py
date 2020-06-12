from ReFClass import *
import tkinter.messagebox
root = Tk()
root.geometry("900x660+200+50")
#   新建一个tk窗口
a = FileRead()
a.fileread()
a.GetDictData()
a.GetToatalSet()
#   开始准备工作

frmLS = Frame(root, height=10)
frmLS.pack(side=TOP, expand=NO)
#   设置放置第一行的区域
frmLL = Frame(root,height = 700)
frmLL.pack(anchor="center")
#   设置放置课程表的区域
Label1 = Label(frmLS, text="(请输入阿拉伯数字)查询：星期").grid(row=0, column=0)
entry1 = Entry(frmLS)
entry1.delete(0, "end")
entry1.insert(0, "")
#   修改默认输入
entry1.grid(row=0, column=1)
Label2 = Label(frmLS, text="    第").grid(row=0, column=2)
entry2 = Entry(frmLS)
entry2.delete(0, "end")
entry2.insert(0, "")
entry2.grid(row=0, column=3)
Label3 = Label(frmLS, text="节   课程名：").grid(row=0, column=4)
entry3 = Entry(frmLS, bd=4)
entry3.delete(0, "end")
entry3.insert(0, "")
entry3.grid(row=0, column=5)
#   布局第一行的搜索框和文本元素


def getData():
    rscr = ""
    #   创建一个空字符串
    a.GetToatalSet()

    Day = entry1.get()
    a.SearchClassWeek(Day)      # Search3 星期几

    ClassPos = entry2.get()
    a.SearchClassPos(ClassPos)  # Search2  第几节

    ClassName = entry3.get()
    a.SearchClassName(ClassName) # Search1  课程名

    a.GetResult()

    for i in range(1,a.workday+1):
        for j in range(1, a.Class_everyday+1):
            a.Search1.discard((i,j))
            a.Search2.discard((i,j))
            a.Search3.discard((i,j))
            #   删除三个集合中的元素，为下一次搜索做准备
            if (i,j) in a.Result:
                rscr += "星期%d第%d节课 %s\n"%(i, j, a.ClassDict[i, j])
            #   遍历，找到最终结果
    tkinter.messagebox.showinfo("查询结果", rscr)
    #   弹窗显示结果
    del a.Result
    #   重置结果


b1 = Button(frmLS, text="搜索", width=10, height=1, command=getData).grid(row=0, column=7)
#   定义搜索按钮的功能

for i in range(0, a.workday+1):
    for j in range(0, a.Class_everyday+1):
        b = Label(frmLL, bg="#DCDCDC", text=a.ClassDict[(i, j)], font=42)
        b.grid(row=j, column=i, ipadx=15, ipady=5, padx=10, pady=10)
#   放置课程表
root.mainloop()
