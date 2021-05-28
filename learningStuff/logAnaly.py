'''
搜索当前目录下所有文件
1. 把所有以str1作为结尾的行的回车键删除，使下面一行和当前行处于同一行
2. 
'''

from contextlib import contextmanager
from datetime import time,datetime
import os
import re



strKey = {"App Actv Tsk srcEnt=217, Event=5":0
            ,"wrUmmChkAndTriggerUeInfoReq: SKIPPED triggering Ue info request for this message":0
            ,"Received RRCConnectionReestablishmentRequest message":0
            ,"wrUmmGetUe: Failed To get ue control block":0
            ,"Received RRCConnectionRequest message with establishmentCause":0
            ,"Populate the NHU header info":0
            ,"wrUmmChkAndTriggerUeInfoReq: Need not trigger Ue info request for this message":0}

#@contextmanager

prehandleFilename="pre.txt"
outFilename="out.txt"
def fileReaderGenerator(fn):
	with open(fn) as f:
		while True:
			block = f.readline()
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
    key1 = list(strKey.keys())[0]
    for eachline in alllines:
        #step1: 把所有以str1作为结尾的行的回车键删除，使下面一行和当前行处于同一行,并把写入到prefile
        a=re.sub(r'App Actv Tsk srcEnt=217, Event=5\n',key1,eachline)
        prefile.writelines(a)
    
    #prefile文件指针指向文件头
    prefile.seek(0)
    outfile=open(outfilepathname,'w+')
    prelines=prefile.readlines()
    for preline in prelines:
        #step2: 查找每个包含str1的行，这行其实是原文件 str1那一行和下面一行。并把这一行（相当于原文件的两行）写入outfile
        if key1 in preline:
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
            
            #count = [0,0,0,0,0,0,0]
            for line in fileReaderGenerator(prefilepathname):
                #step3： 查找每个关键字，比较 str1出现的次数和（str2到str7）出现次数的和
                i = 0
                for key in strKey.keys():
                    if i == 0:
                        strKey[key] -= line.count(key)
                    else:
                        strKey[key] += line.count(key)
                    i+=1
                    
            print(strKey)	
            print("sum(num for num in count)=",sum(num for num in strKey.values()))
            if sum(num for num in strKey.values()) == 0:
                print("match\n\n")
            else:
                print("-------------------------------something missing\n\n")
 
if __name__ == '__main__':
    filePath = "D:\\JIRA\\CRAN-12483- L3 Core\\dbglog_l3_cuId_1_2021_5_23_13_49_36"
    eachFile(filePath)