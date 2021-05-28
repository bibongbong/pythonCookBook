'''
搜索当前目录下所有文件
1. 把所有以str1作为结尾的行的回车键删除，使下面一行和当前行处于同一行
2. 
'''

from contextlib import contextmanager
from datetime import time,datetime
import os
import re


str1 = "App Actv Tsk srcEnt=217, Event=5"
str2 = "wrUmmChkAndTriggerUeInfoReq: SKIPPED triggering Ue info request for this message"
str3 = "Received RRCConnectionReestablishmentRequest message"
str4 = "wrUmmGetUe: Failed To get ue control block"
str5 = "Received RRCConnectionRequest message with establishmentCause"
str6 = "Populate the NHU header info"
str7 = "wrUmmChkAndTriggerUeInfoReq: Need not trigger Ue info request for this message"


#@contextmanager

prehandleFilename="pre.txt"
outFilename="out.txt"
def fileReaderGenerator(fn):
	with open(fn) as f:
		while True:
			block = f.read()
			if block:
				yield block
			else:
				f.close()
				return
                
def preHandle(filename):
    print("preHandling :",filename)
    f=open(filename,'r')
    pathname,fname = os.path.split(filename)
    alllines=f.readlines()
    f.close()
    #往预处理文件里追加  
    prefilepathname = os.path.join('%s\\%s' % (pathname, prehandleFilename))
    outfilepathname = os.path.join('%s\\%s' % (pathname, outFilename))
    prefile=open(prefilepathname,'w+')
    for eachline in alllines:
        #step1: 把所有以str1作为结尾的行的回车键删除，使下面一行和当前行处于同一行,并把写入到prefile
        a=re.sub(r'App Actv Tsk srcEnt=217, Event=5\n',str1,eachline)
        prefile.writelines(a)
    
    #prefile文件指针指向文件头
    prefile.seek(0)
    outfile=open(outfilepathname,'w+')
    prelines=prefile.readlines()
    for preline in prelines:
        #step2: 查找每个包含str1的行，这行其实是原文件 str1那一行和下面一行。并把这一行（相当于原文件的两行）写入outfile
        if str1 in preline:
            outfile.writelines(preline)
    outfile.close()
    
    return outfilepathname

# 遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        if allDir != prehandleFilename and allDir != outFilename:
            child = os.path.join('%s\\%s' % (filepath, allDir))
            prefilepathname = preHandle(child)
            
            str1Count = 0
            str2Count = 0
            str3Count = 0
            str4Count = 0
            str5Count = 0
            str6Count = 0
            str7Count = 0
            for i in fileReaderGenerator(prefilepathname):
                #step3： 查找每个关键字，比较 str1出现的次数和（str2到str7）出现次数的和
                str1Count += i.count(str1)
                str2Count += i.count(str2)
                str3Count += i.count(str3)
                str4Count += i.count(str4)
                str5Count += i.count(str5)
                str6Count += i.count(str6)
                str7Count += i.count(str7)
            print("str1Count={},str2Count={},str3Count={},str4Count={},str5Count={},str6Count={},str7Count={}".format(str1Count,str2Count,str3Count,str4Count,str5Count,str6Count,str7Count))	
            print("str2Count+:str7Count=",(str2Count+str3Count+str4Count+str5Count+str6Count+str7Count))
            if str1Count==(str2Count+str3Count+str4Count+str5Count+str6Count+str7Count):
                print("match\n\n")
            else:
                print("-------------------------------something missing\n\n")
 
if __name__ == '__main__':
    filePath = "D:\\JIRA\\CRAN-12483- L3 Core\\cu\\log\\23may_531PM_2021_05_23-12_01_25\\New folder\\dbglog_l3_cuId_4_2021_5_23_13_41_3"
    eachFile(filePath)