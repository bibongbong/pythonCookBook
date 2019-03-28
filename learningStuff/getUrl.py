####################################################################
# File:		getUrl.py
# Function:	Learning to how to get the specific URL, and parse the HTML page to get the content you want
#
####################################################################

import urllib.request
import operator
from bs4 import BeautifulSoup

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


def getnextPageUrl(all_tr):
    nextPageTr = all_tr[-1]
    all_strong = nextPageTr.find_all("strong")
    nextPageItem = all_strong[4].a
    nextPageUrl = serverUrl + nextPageItem['href']
    return nextPageUrl


def searchPage(currentUrl, myNum):
    print("current url is %s " % (currentUrl))

    if isNeedProxy:
        # set the http proxy
        proxy_handler = urllib.request.ProxyHandler({"http": 'http://135.245.248.89:8000'})
        opener = urllib.request.build_opener(proxy_handler)
        urllib.request.install_opener(opener)

    # open the zhcw ShuangSeQiu page
    response = urllib.request.urlopen(currentUrl)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    all_tr = soup.find_all("tr")
    isFound = False

    #loop all winNum in current page
    for tr in all_tr[2:-1]:
        winNum = getWinNum(tr)
        if winNum == myNum:
            winDate = getWinDate(tr)
            isFound = True
            print("Found: %s" % winNum)
            print(winDate)

    # If there is next page, search next page.
    # If not, it means all pages not match
    if not isFound:
        nextPageUrl = getnextPageUrl(all_tr)
        if nextPageUrl != currentUrl:
            isFound = searchPage(nextPageUrl, myNum)

    return isFound


result = searchPage(startUrl, testNum)
if result:
    print(" You missing somthing big")
else:
    print(" No missing. Go ON")
