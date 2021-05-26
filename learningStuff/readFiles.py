
import os

str1 = "python"
str2 = "print"
str3 = "Method"
 
# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\\%s' % (filepath, allDir))
        #child.decode('gbk')
        print("open file:",child)
        readFile(child)
 
# 读取文件内容并打印
def readFile(filename):
    fopen = open(filename, encoding='utf-8') # r 代表read
    str1Count = 0
    str2Count = 0
    str3Count = 0
    for eachLine in fopen:
        str1Count += eachLine.count(str1)
        str2Count += eachLine.count(str2)
        str3Count += eachLine.count(str3)
    print("str1Count={},str2Count={},str3Count={}\n".format(str1Count,str2Count,str3Count))
    fopen.close()
    

 
if __name__ == '__main__':
    filePath = "D:\\GitCode\\pythonCookBook\\learningStuff"
    eachFile(filePath)
    #readFile(filePath)