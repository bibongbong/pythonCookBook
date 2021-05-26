####################################################################
# File:		getUrl.py
# Function:	Learning to how to get the specific URL, and parse the HTML page to get the content you want
#
####################################################################

import urllib.request
import operator
from bs4 import BeautifulSoup


startUrl = 'https://www.meijutt.com/content/meiju22659.html'
serverUrl = 'https://www.meijutt.com/'




def searchPage(currentUrl):
    print("current url is %s " % (currentUrl))


    # open the zhcw ShuangSeQiu page
    response = urllib.request.urlopen(currentUrl)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

    all_strong = soup.find_all("strong")
    

    #loop all winNum in current page
    for strong in all_strong:
        a_elem = strong.find("a")
        link = a_elem['href']
        print(link)



result = searchPage(startUrl)

