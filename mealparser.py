#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, datetime
from bs4 import BeautifulSoup

def mealparse(days): 
    try:
        dt = datetime.datetime.today() + datetime.timedelta(days=days) # parse (current date + days)
        date = dt.strftime('%Y.%m.%d') # yyyy.mm.dd
        day = dt.weekday()+1 # day of the week
        if day == 6 or day == 7:
            return (
                date + '(' + ['월', '화', '수', '목', '금', '토', '일'][day-1] + ')\n'
                '오늘은 급식이 없습니다.' # empty lists
            )
        URL = ( 
                'http://stu.goe.go.kr/sts_sci_md01_001.do?'
                'schulCode=J100006779' # school code
                '&schulCrseScCode=3'
                '&schulKndScCode=03'
                '&schMmealScCode=2'
                '&schYmd=' + date
        )
        html = requests.get(URL).text 
        data = str(BeautifulSoup(html, 'html.parser').find_all('tr')[2].find_all('td')[day])
        for filter_data in ['[', ']', '<td class="textC">', '<td class="textC last">', '</td>', '.']:
            data = data.replace(filter_data, '') # filter html tags
        data = data.split('<br/>')
        data = data[:len(data)-1]
        for idx, item in enumerate(data):
            for char in reversed(item):
                if char.isdigit(): data[idx] = data[idx][:-1] # crop allergy infomation
                else: break
        if not data:
            return (
                date + '(' + ['월', '화', '수', '목', '금', '토', '일'][day-1] + ')\n'
                '급식 데이터를 가져올 수 없습니다.' # empty lists
            )
        else:
            data = '\n'.join(data)
            return (
                date + '(' + ['월', '화', '수', '목', '금', '토', '일'][day-1] + ')\n'
                '은여울중학교 급식 정보야!\n\n' + data
            )
    except: 
        return '에러가 발생했습니다.' # if error occured

if __name__ == '__main__':
    print(str(datetime.datetime.today().strftime('%Y.%m.%d')))
    n = int(input('input : '))
    print('-----')
    print(mealparse(n)) # function test

'''
 junhoyeo@Macbookui-MacBook-Pro  ~/Documents/flask-mealbot  python3 meal-parser.py
2018.07.11
input : 1
-----
2018.07.12(목)
은여울중학교 급식 정보야!

현미밥
오꼬노미온더치킨
오이깍두기
배추김치
호박새우젓찌개(중)
자몽푸딩
'''
