#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, requests 
from flask import Flask, request
import mealparser

app = Flask(__name__)
server_url = 'http://silvermealbot.dothome.co.kr/'

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
    if content == '대화 시작':
        # 대화 시작
        # 메세지 : 안녕! 나는 은여울중학교 급식봇이야! ><
        # 키보드 : [급식]
        response['message']['text'] = '안녕! 나는 은여울중학교 급식봇이야! ><'
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = ['급식']
        return json.dumps(response, ensure_ascii=False)
    elif content == '처음으로':
        # 처음으로
        # 메세지 : 처음으로 돌아왔습니다.
        # 키보드 : [급식]
        response['message']['text'] = '처음으로 돌아왔습니다.'
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = ['급식']
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
    else:
        response['message']['text'] = '알 수 없는 입력 \'' + content + '\''
        response['keyboard']['type'] = 'buttons'
        response['keyboard']['buttons'] = ['급식']
        return json.dumps(response, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)
