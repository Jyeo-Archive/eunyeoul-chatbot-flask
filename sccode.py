import re, requests, urllib.parse
from bs4 import BeautifulSoup

def searchSchoolcode(quary):
    html = requests.post('https://www.meatwatch.go.kr/biz/bm/sel/schoolListPopup.do', 
        data={ 'criteria': 'pageIndex=1&bsnmNm=' + urllib.parse.quote_plus(quary) }).text
    return [ re.sub('<[^<]+?>', '', str(result)).strip('\n').split('\n') for result in BeautifulSoup(html, 'html.parser').find_all('tbody')[1].find_all('tr')]

def getEduOfficeURL(address):
    pass

if __name__ == '__main__':
    print(searchSchoolcode('은여울중학교')[0][2])
