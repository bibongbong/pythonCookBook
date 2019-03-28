####################################################################
#File:		getUrl.py
#Function:	Learning to how to get the specific URL, and parse the HTML page to get the content you want
#
####################################################################

import urllib2 
from bs4 import BeautifulSoup

import time
from datetime import datetime

lastTimeStamp = int(1000*time.time())
print "lastTimeStamp %s" %lastTimeStamp

def dumpTimeStamp():
	global lastTimeStamp
	currentTimeStamp = int(1000*time.time())
	delta =  currentTimeStamp - lastTimeStamp
	lastTimeStamp = currentTimeStamp

	return delta

def getNextPage(currentPageTable, nextPageUrl):
	timeStart = int(1000*time.time())
	navigationRow = currentPageTable.contents[45]
	
	totalPageNums = navigationRow.contents[1].contents[2].contents[1].string
        nextPageUrl[0]  += navigationRow.contents[1].contents[2].contents[9].contents[0]['href']
	#print "nextPageUrl is %s "%nextPageUrl[0]


	
	timeEnd = int(1000*time.time())
	print "getTableInCurrentPage %s " %(timeEnd - timeStart)


        return  nextPageUrl[0].find("pageNum="+totalPageNums)
       

def getTableInCurrentPage(winningNums, winningNumsRow):
	timeStart = int(1000*time.time())
	#print soup.table.contents[i]
	winningNumsCell = winningNumsRow.contents[5]


	#ballsBody is the table that contain 6 red balls and 1 blue ball
	winningNums[0] = winningNumsCell.contents[1].string
	winningNums[1] = winningNumsCell.contents[3].string
	winningNums[2] = winningNumsCell.contents[5].string
	winningNums[3] = winningNumsCell.contents[7].string
	winningNums[4] = winningNumsCell.contents[9].string
	winningNums[5] = winningNumsCell.contents[11].string
	winningNums[6] = winningNumsCell.contents[13].string

	# winningNums[7] is winning number's data and winningNums[8] is winning number's NO.
	winningNums[7] = winningNumsRow.contents[1].string
	winningNums[8] = winningNumsRow.contents[3].string
	#print "%s  %s  : %s,%s,%s,%s,%s,%s     %s\n\n" %(winningNums[7], winningNums[8], winningNums[0],winningNums[1],winningNums[2],winningNums[3],winningNums[4],winningNums[5],winningNums[6])

	timeEnd = int(1000*time.time())
	print "getTableInCurrentPage %s " %(timeEnd - timeStart)

	

def findInCurrentLine(searchNum, winningNums):

	match = True
	for i in range(0,6):
		if(searchNum[i] != int(winningNums[i])):
			match = False
	if(match):
		print "seacrhNum %s %s %s %s %s %s , %s  found. Data is  " %(searchNum[0],searchNum[1],searchNum[2],searchNum[3],searchNum[4],searchNum[5],searchNum[6])


	#print "findInCurrentLine %s " %(dumpTimeStamp())

	return match

def getBeautifulSoupFromHtml(htmllink):
	#def 
	# set the http proxy
	timeStart = int(1000*time.time())
	proxy_handler = urllib2.ProxyHandler({"http": 'http://135.245.48.12:8000'})

	time1 = int(1000*time.time())
	print "proxy_handler = urllib2.ProxyHandler %s " %(time1 - timeStart)
	
	opener = urllib2.build_opener(proxy_handler)

	time2 = int(1000*time.time())
	print "opener = urllib2.build_opener %s " %(time2 - time1)

	urllib2.install_opener(opener)
	time3 = int(1000*time.time())
	print "urllib2.install_opener %s " %(time3 - time2)

	#open the zhcw ShuangSeQiu page
	response = urllib2.urlopen(htmllink)
	time4 = int(1000*time.time())
	print "response = urllib2.urlopen %s " %(time4 - time3)

	html = response.read()
	#print html
	time5 = int(1000*time.time())
	print "html = response.read %s " %(time5 - time4)

	soup = BeautifulSoup(html)
	time6 = int(1000*time.time())
	print "soup = BeautifulSoup(html) %s " %(time6 - time5)

	timeEnd = int(1000*time.time())
	print "getBeautifulSoupFromHtml %s " %(timeEnd - timeStart)

	return soup
	
def findInCurrentPageTable(searchNum, currentPageTable):

	result = False
	timeStart = int(1000*time.time())
	winningNums = [0 for i in range(9)]
	#i = 0
	for i in range(5,45):
		#print "currentPageTable.contents[%s] is %s" %(i, currentPageTable.contents[i].string)
		#print " i = %s" %i
		if("\n" != currentPageTable.contents[i]):
			
			#read the one row red and blue balls into readBall list
			#find the row that contain the winning numbers
			winningNumsRow = currentPageTable.contents[i]
			getTableInCurrentPage(winningNums, winningNumsRow)
			


			#search the searchNum in the winningNums[]
			if(findInCurrentLine(searchNum, winningNums)):
				print "Num found, Data:%s" %winningNums[7] #print the found data
				result = True
				break

	timeEnd = int(1000*time.time())
	print "findInCurrentPageTable %s " %(timeEnd -timeStart )
	
	#if can not find in current page, then go to next page and search
	if(False == result):
	 	#if can not get the next page handler, it means current page is the last page

	 	nextPageUrl = ['http://kaijiang.zhcw.com']
	 	if(getNextPage(currentPageTable, nextPageUrl)):		

	 		print "*************************Search in nextPage Url %s" %nextPageUrl[0]
	 		nextPageSoup = getBeautifulSoupFromHtml(nextPageUrl[0])
	 		result = findInCurrentPageTable(searchNum, nextPageSoup.table)

	

	return result



	
htmlLink = 'http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp'
soup = getBeautifulSoupFromHtml(htmlLink)
firstPageTable = soup.table
#print "print table\n"
#print table
searchNum = [1,10,14,22,26,28,1]

result = findInCurrentPageTable(searchNum, firstPageTable)
print "The Number(%s) search result: %s" %(searchNum,result)


