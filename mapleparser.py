#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#        _             _        __   _______      
#       | |_   _ _ __ | |__   __\ \ / / ____|___  
#    _  | | | | | '_ \| '_ \ / _ \ V /|  _| / _ \ 
#   | |_| | |_| | | | | | | | (_) | | | |__| (_) |
#    \___/ \__,_|_| |_|_| |_|\___/|_| |_____\___/ 
#                                                 
# Copyright (c) 2018 Junho Yeo                             

import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

def mapleparse(charactername):
    html = requests.get(('http://maplestory.nexon.com/MapleStory/Page/GnxPopup.aspx?'
        'URL=MyMaple/POP_Profile'
        '&strCharacterName=' + quote(charactername.encode('euc-kr'))
    )).text 
    soup = BeautifulSoup(html, 'html.parser').find(id='pop_content')
    name = soup.find(class_='stt').string
    avatar = soup.find('img', class_='avatar')['src']
    spec = [item.string for item in soup.find_all('span', class_='tx')]
    return {
        '이름' : name,
        '아바타' : avatar,
        '스펙' : {
            '직업' : spec[0],
            '레벨' : spec[1],
            '경험치' : spec[2],
            '인기도' : spec[3],
            '스타일' : spec[4],
            '주활동월드' : spec[5],
            '주활동마을' : spec[6],
            '친구목적' : spec[7],
            '종합랭킹' : spec[8],
            '월드랭킹' : spec[9],
            '직업랭킹' : spec[10],
            '인기랭킹' : spec[11]
        }
    }
    
if __name__ == '__main__':
    print(mapleparse('베베'))

'''
{
    '이름': '베베', 
    '아바타': 'http://avatar.maplestory.nexon.com/Character/GJPLHNADEFGHGKKJAJDIECOPLKHNJPMGOLFLCEGPDKMJHMPDAKMCDADMPAMMHGIACBPBJKJCIKLNACDEBBOEPGKCHCCLMECJICKMAJKLLLLPAJGJLNDLCPBMJPACMGFHEPBLIKFLFDFANDEIEJNJNJIFMLGFMEHHDPDEMOANHNAHBHMCMLAELMLJFDHHCGGMDMKODLIOFPIAKBGDNEMFMHFCIPLNPJKGDLCACOCLCIPLPGDPGBIGNAABBINNDLIB.png',
    '스펙': {
        '직업': '레지스탕스/', 
        '레벨': '250', 
        '경험치': '0', 
        '인기도': '20506', 
        '스타일': '영웅', 
        '주활동월드': '크로아', 
        '주활동마을': '리프레', 
        '친구목적': '하루종일', 
        '종합랭킹': '사냥을 함께할 친구를 구해요', 
        '월드랭킹': '1', 
        '직업랭킹': '1', 
        '인기랭킹': '1'
    }
}
'''
