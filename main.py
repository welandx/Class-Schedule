from tkinter import *
from tkinter.filedialog import askopenfilename
class FileRead:
    file = ""
    workday=-1
    Class_everyday = -1
    ClassDict = {}
    ClassList = []
    def fileread(self):
        root = Tk()
        root.withdraw()
        path = askopenfilename()
        #无用代码
        #def selectPath():
            #path_ = askopenfilename()
            #path.set(path_)
        #root = Tk()
        #path = StringVar()
        #Label(root, text="目标路径:").grid(row=0, column=0)
        #Entry(root, textvariable=path).grid(row=0, column=1)
        #Button(root, text="路径选择", command=selectPath).grid(row=0, column=2)
        #root.mainloop()
        self.file = open(path, mode="r+", encoding='UTF-8')
    def GetDictData(self):
        import re
        self.Class_everyday = -1
        for line in self.file.readlines():
            self.Class_everyday += 1
            self.workday = -1
            line = line.strip()
            bj = re.finditer(r'([\u4E00-\u9FA5])+[^\s*\b]', line, re.M | re.I)
            for match in bj:
                self.workday += 1
                self.ClassDict[(self.workday, self.Class_everyday)] = match.group()

class FileSearch(FileRead):
    def GetListData(self):
        SearchClassName = input()
        def get_key1(dct, value):
            return list(filter(lambda k: dct[k] == value, dct))
        print(get_key1(self.ClassDict,SearchClassName))
#测试class FileRead
a = FileRead()
a.fileread()
a.GetDictData()
print(a.ClassDict)
print(a.workday)
print(a.Class_everyday)
#测试class FileSearch
b=FileSearch()
b.GetListData()
