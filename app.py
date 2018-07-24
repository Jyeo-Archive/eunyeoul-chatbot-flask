#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, requests 
from flask import Flask, request, url_for
import mealparser, weatherparser

app = Flask(__name__)

def response_meal(days):
    response = { 'message' : {}, 'keyboard' : {} } 
    response['message']['text'] = mealparser.mealparse(days)
    response['keyboard']['type'] = 'buttons'
    response['keyboard']['buttons'] = ['오늘 급식', '내일 급식', '내일 모레 급식', '처음으로']
    return response

@app.route('/keyboard')
def default_keyboard():
    keyboard = {'type' : 'buttons', 'buttons' : ['대화 시작']}
    return json.dumps(keyboard, ensure_ascii=False)

@app.route('/message', methods=['GET', 'POST'])
def chat():
    data = request.get_json(silent=True)
    user_key = data['user_key']
    content = data['content']
    response = { 'message' : {}, 'keyboard' : {} } 
    menu_buttons = ['급식', '날씨']

    if content == '대화 시작':
        # 대화 시작
        # 메세지 : 안녕! 나는 은여울중학교 급식봇이야! ><
        # 키보드 : menu_buttons
        img_url = 'http://silvermealbot.dothome.co.kr/images/logo.jpg'
        response['message']['text'] = '안녕! 나는 은여울중학교 급식봇이야! ><'
        response['message'].update({'photo': {}})
        response['message']['photo']['url'] = img_url
        response['message']['photo']['width'] = 600
        response['message']['photo']['height'] = 600
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = menu_buttons
        return json.dumps(response, ensure_ascii=False)
    elif content == '처음으로':
        # 처음으로
        # 메세지 : 처음으로 돌아왔습니다.
        # 키보드 : menu_buttons
        response['message']['text'] = '처음으로 돌아왔습니다.'
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = menu_buttons
        return json.dumps(response, ensure_ascii=False)

    elif content == '급식':
        # 급식
        # 메세지 : 언제 급식을 알고 싶어?
        # 키보드 : [오늘 급식, 내일 급식, 내일 모레 급식, 처음으로]
        response['message']['text'] = '언제 급식을 알고 싶어?'
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = ['오늘 급식', '내일 급식', '내일 모레 급식', '처음으로']
        return json.dumps(response, ensure_ascii=False)
    # 요청한 날짜에 맞게 급식 데이터를 파싱해 출력
    elif content == '오늘 급식':
        return json.dumps(response_meal(0), ensure_ascii=False)
    elif content == '내일 급식':
        return json.dumps(response_meal(1), ensure_ascii=False)
    elif content == '내일 모레 급식':
        return json.dumps(response_meal(2), ensure_ascii=False)

    elif content == '날씨':
        # 날씨
        # 기상청 제공 RSS 서비스 파싱을 통해 최신 날씨 정보 출력
        # 키보드 : menu_buttons
        weather = weatherparser.weatherparse()
        img_url = 'http://silvermealbot.dothome.co.kr/images/' + weather['img']
        response['message']['text'] = weather['text']
        response['message'].update({'photo': {}})
        response['message']['photo']['url'] = img_url
        response['message']['photo']['width'] = 600
        response['message']['photo']['height'] = 600
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = menu_buttons
        return json.dumps(response, ensure_ascii=False)

    elif content == '시간표':
        # 시간표 (학년 선택)
        # 메세지 : 몇 학년이야?
        # 키보드 : [1학년, 2학년, 3학년, 처음으로]
        response['message']['text'] = '몇 학년이야?'
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = ['1학년', '2학년', '3학년', '처음으로']
        return json.dumps(response, ensure_ascii=False)
    elif content in [str(i) + '학년' for i in range(1, 4)]:
        # 시간표 (반 선택)
        # 메세지 : 학급을 선택해줘!
        # 키보드 : 입력한 학년과 각 반 학급 수에 맞게 출력
        grade = content[0]
        response['message']['text'] = '학급을 선택해줘!'
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = [f'{grade}학년 {i}반' for i in range(1, {'1':6, '2':5, '3':5}[grade]+1)]
        return json.dumps(response, ensure_ascii=False)
    elif ('학년' in content) and ('반' in content):
        if '(' not in content:
            # 시간표 (날짜 선택)
            # 메세지 : 언제 시간표가 필요해?
            # 키보드 : [content + ' (오늘)', content + ' (내일)' , content + ' (모레)']
            response['message']['text'] = '학급을 선택해줘!'
            response['keyboard']['type'] = 'buttons'
            response['keyboard']['buttons'] = [content + ' (오늘)', content + ' (내일)' , content + ' (모레)']
            return json.dumps(response, ensure_ascii=False)
        else:
            ['오늘', '내일', '모레'].index()
            return json.dumps(response, ensure_ascii=False)

    else:
        response['message']['text'] = '알 수 없는 입력 \'' + content + '\''
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = menu_buttons
        return json.dumps(response, ensure_ascii=False)   

if __name__ == '__main__':
    app.run(debug=True)
