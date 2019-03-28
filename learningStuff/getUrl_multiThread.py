####################################################################
# File:		getUrl.py
# Function:	Learning to how to get the specific URL, and parse the HTML page to get the content you want
#
####################################################################

import urllib.request
import operator
from bs4 import BeautifulSoup
import asyncio

# testNum = [3,5,11,12,26,29,15]

#testNum = [11, 16, 19, 22, 25, 30, 8]
testNum = [8, 10, 17, 20, 27, 30, 1]
startUrl = 'http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp'
serverUrl = 'http://kaijiang.zhcw.com/'
isNeedProxy = True


def getWinNum(tr):
    win_num = []
    all_td = tr.find_all("td")
    for em in all_td[2]:
        if em.string.isdigit():
            win_num.append(int(em.string))
    return win_num


def getWinDate(tr):
    all_td = tr.find_all("td")
    winDate = all_td[0].string
    return winDate


def getnextPageUrl(i):
    return "http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum="+str(i)

def getLastPageNum(all_tr):
    nextPageTr = all_tr[-1]
    all_strong = nextPageTr.find_all("strong")
    nextPageItem = all_strong[5].a
    
    return nextPageItem['href'][35:]

def getResponse(currentUrl):
    print("current url is %s " % (currentUrl))

    if isNeedProxy:
        # set the http proxy
        proxy_handler = urllib.request.ProxyHandler({"http": 'http://135.245.248.89:8000'})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)
    print("getResponse ",currentUrl)
    # open the zhcw ShuangSeQiu page
    response = urllib.request.urlopen(currentUrl)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup 

def loopAllWinNumInCurrentPage(all_tr,myNum):
    #loop all winNum in current page
    for tr in all_tr[2:-1]:
        winNum = getWinNum(tr)
        if winNum == myNum:
            winDate = getWinDate(tr)
            isFound = True
            print("Found: %s" % winNum)
            print(winDate)
            raise StopIteration


def searchFirstPage(currentUrl, myNum):
    soup = getResponse(currentUrl)
    
    all_tr = soup.find_all("tr")
    isFound = False

    loopAllWinNumInCurrentPage(all_tr,myNum)

    lastPageNum = getLastPageNum(all_tr)
    return lastPageNum


def searchPage(i, myNum):
    print(i)
    currentUrl = getnextPageUrl(i)
    soup = yield from getResponse(currentUrl)

    all_tr = soup.find_all("tr")
    isFound = False

    loopAllWinNumInCurrentPage(all_tr,myNum)






lastPage = searchFirstPage(startUrl, testNum)
print("lastPage ",lastPage)
loop = asyncio.get_event_loop()
tasks = [searchPage(i, testNum) for i in range(int(lastPage))]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

