from ReFClass import *
import tkinter.messagebox
root = Tk()
root.geometry("900x660+200+50")
#   新建一个tk窗口
a = FileRead()
a.fileread()
a.GetDictData()
a.GetToatalSet()


frmLS = Frame(root, height=10)
frmLS.pack(side=TOP, expand=NO)
frmLL = Frame(root,height = 1000)
frmLL.pack(anchor="center")
Label1 = Label(frmLS, text="(请输入阿拉伯数字)查询：星期").grid(row=0, column=0)
entry1 = Entry(frmLS)
entry1.grid(row=0, column=1)
Label2 = Label(frmLS, text="    第").grid(row=0, column=2)
entry2 = Entry(frmLS)
entry2.grid(row=0, column=3)
Label3 = Label(frmLS, text="节   课程名：").grid(row=0, column=4)
entry3 = Entry(frmLS, bd=4)
entry3.grid(row=0, column=5)


#   布局第一行的搜索框和文本元素
def getData():
    rscr = ""
    Day = entry1.get()
    a.SearchClassWeek(Day)
    ClassPos = entry2.get()
    a.SearchClassPos(ClassPos)
    ClassName = entry3.get()
    a.SearchClassName(ClassName)
    a.GetResult()
    for i in range(1,a.workday):
        for j in range(1, a.Class_everyday):
            if (i,j) in a.Result:
                rscr += "星期%d第%d节课 %s\n"%(i,j,a.ClassDict[i,j])
    tkinter.messagebox.showinfo("查询结果",rscr)
b1 = Button(frmLS, text="搜索", width=10, height=1, command=getData).grid(row=0, column=7)
#   定义搜索按钮的功能

for i in range(0,a.workday+1):
    for j in range (0,a.Class_everyday+1):
        b=Label(frmLL, text=a.ClassDict[(i,j)],font=(42))
        b.grid(row=j, column=i, ipadx=15, ipady=5, padx=10, pady=10)

root.mainloop()
