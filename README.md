# Eunyeoul Kakaotalk Mealbot with PHP

Python Flask로 작성된 두 번째 은여울중학교 급식봇 

## Tasklist

- [x] 급식 파싱
    - [x] 오늘 급식
    - [x] 내일 급식
    - [x] 모레 급식
- [x] 날씨 파싱
    - [x] 일러스트
- [ ] 시간표
    - [ ] 1학년
    - [ ] 2학년
    - [ ] 3학년
- [ ] 서버 내부 이미지 파일 서빙

## Features

### 급식 파싱
![screenshot - parse school meal infomation](./screenshots/meal.png)

- 나이스 학생서비스에서 제공하는 은여울중학교 식단표 데이터를 파싱해서 제공합니다.
- 급식 데이터를 가져오는 데 성공한 경우, 해당일의 날짜 및 요일과 함께 급식 정보가 출력됩니다.
- 급식이 없는 날이나 관련 데이터가 없는 날에는 해당일의 날짜 및 요일과 `급식 데이터를 가져올 수 없습니다.` 메세지가 출력됩니다.
- 급식 파싱에 필요한 학교코드(`schulCode`)는 본 저장소에 있는 [`sccode.py`](./sccode.py) 모듈을 이용해서 구할 수 있습니다.

### 날씨 파싱
![screenshot - parse weather infomation](./screenshots/weather.png)

- 기상청 RSS 서비스(동네예보 > 시간별예보)를 이용해서 실시간 날씨 데이터를 제공합니다.
- 은여울중학교와 가장 인접한 기상대가 위치한 경기도 김포시 구래동(`zone=4157057000`) 기준의 데이터입니다.
