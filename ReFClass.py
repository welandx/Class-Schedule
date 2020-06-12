from tkinter import *
from tkinter.filedialog import askopenfilename


class FileRead:
    #   以下变量存放必要的数据
    file = ""
    #   文件的地址
    workday = -1
    #   每周教学日
    Class_everyday = -1
    #   每日课程数
    ClassDict = {}
    #   存放每周课程
    ClassList = []
    #   存放每门课程对应的教学安排
    Total = set()
    #   存放所有课程坐标
    Search1 = set()
    Search2 = set()
    Search3 = set()
    #   存放每个筛选条件的结果
    Result = set()
    #   存放总结果


    def fileread(self):
        #   查找文件并获取地址
        root = Tk()
        root.withdraw()
        path = askopenfilename()
        self.file = open(path, mode="r+", encoding='UTF-8')


    def GetDictData(self):
        #   从文件中得到课程安排
        import re
        self.Class_everyday = -1
        for line in self.file.readlines():
            self.Class_everyday += 1
            self.workday = -1
            #   重置workday，因为是一行行读取
            bj = re.finditer(r'([\u4E00-\u9FA5])+[^\s*\b]', line, re.M | re.I)
            #   正则表达式剪切字符串
            for match in bj:
                self.workday += 1
                self.ClassDict[(self.workday, self.Class_everyday)] = match.group()
        self.file.close()
    def GetToatalSet(self):
        for i in range(1, self.workday+1):
            for j in range(1, self.Class_everyday+1):
                self.Total.add((i, j))


    def SearchClassName(self,ClassName):
        #   根据课程名，输出课程所在位置
        def get_key1(dct, value):
            return list(filter(lambda k: dct[k] == value, dct))
        if ClassName == "":
            self.Search1 = self.Total
        else:
            self.ClassList = get_key1(self.ClassDict, ClassName)
            for i in range(self.workday + 1):
                for j in range(self.Class_everyday + 1):
                    if (i, j) in self.ClassList:
                        self.Search1.add((i, j))



    def SearchClassPos(self,ClassPos):
        #   查询第几节课的所有课程
        if ClassPos == "":
             self.Search2 = self.Total
        else:
            ClassPos = int(ClassPos)
            if ClassPos > self.Class_everyday:
                print("输入错误！")
            else:
                for i in range(1, self.workday + 1):
                    if (i, ClassPos) in self.ClassDict:
                        self.Search2.add((i, ClassPos))


    def SearchClassWeek(self,Day):
        #   查询星期几的课
        if Day == "":
            self.Search3 = self.Total
        else:
            Day = int(Day)
            if Day > self.workday:
                print("输入错误！")
            else:
                for j in range(1, self.Class_everyday + 1):
                    if (Day, j) in self.ClassDict:
                        self.Search3.add((Day, j))

    def GetResult(self):
        self.Result = self.Search1.intersection(self.Search2, self.Search3)


