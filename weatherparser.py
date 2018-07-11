#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def weatherparse():
    html = requests.get('http://www.weather.go.kr/wid/queryDFSRSS.jsp?zone=4157057000').text 
    # 경기도 김포시 구래동 기준
    weather_data = BeautifulSoup(html, 'html.parser').find_all('data')[0] # recent weather data
    highest = weather_data.tmx.string
    highest = '데이터 없음' if highest == -999 else highest
    lowest = weather_data.tmn.string
    lowest = '데이터 없음' if lowest == -999 else lowest
    weather = weather_data.wfkor.string
    result = (
        '현재 시간 온도 : ' + weather_data.temp.string + '\n'
        '최고 온도 : ' + highest + '\n'
        '최저 온도 : ' + lowest + '\n'
        '하늘 상태 : ' + ['맑음', '구름 조금', '구름 많음', '흐림'][int(weather_data.sky.string)-1] + '\n'
        '강수 상태 : ' + ['없음', '비', '비/눈', '눈/비', '눈'][int(weather_data.pty.string)] + '\n'
        '날씨 : ' + weather + '\n'
        '강수 확률 : ' + weather_data.pop.string + '\n'
        '습도 : ' + weather_data.reh.string + '%\n'
    )
    if '구름' in weather: weather = 'cloud'
    elif '비' in weather: weather = 'rain'
    else: weather = ['sun', 'mist', 'snow'][['맑음', '흐림', '눈'].index(weather)]
    return [result, weather + '.jpg']

if __name__ == '__main__': 
    print(weatherparse()) # function test
