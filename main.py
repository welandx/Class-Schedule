import re
i=j=-1
NewDict={}
fo = open("C:/Users/hp165/Desktop/curriculum.txt",mode="r+",encoding='UTF-8')
print("文件名：",fo.name)
for line in fo.readlines():
    j+=1
    i=-1
    line = line.strip()
    #print(line)
    bj = re.finditer(r'([\u4E00-\u9FA5])+[^\t\b]', line, re.M | re.I)
    for match in bj:
        i+=1
        NewDict[(i,j)] = match.group()
print(NewDict)
fo.close()
