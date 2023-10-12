# flask란
    - 파이썬 기반 웹서비스를 구현하는 패키지
        - 분석 기반 서비스, AI기반 서비스 등등
            - 차트가 동반, 데이터 표현 등등
            - 분석 파이썬 + 서비스(웹) 파이썬 => 동일 언어
    - 종류
        - DJango
            - 프레임워크 기반, 대부분 프로제특 구조가 자동생성됨
            - 상대적으로 느리다.
            개발을 빠르게 구축할 수 있다 -> 국내에서 선호, 추세는 변경 중
            - 스타일이 자바진영의 spring과 유사
        - flask
            - 자유도가 높다. 처음부터 모든것을 직접 다 만든다.
            - 가볍고, 빠르게 구축 가능함
            - 미국쪽에서 선호함
            - ex) 주피터 노트북, ....
            - 스타일이 JS진영의 nodejs과 유사
        - fastAPI
            - 모델 서빙쪽 등 추세를 넓혀가는 중
            - 가장 빠름

# 설치
    - 가상환경구축
        - 한대의 머신에서 여러개의 프로젝트 혹은 서비스 가동시 특정 패키지들의 버전이 충돌됨을 방지 => 격리시킨다, 샌드박스
        - python -m venv was
    - 활성화
        - 윈도우 기준 활성화 파일 위치 (CMD에서 진행)
            - ~/was/Scripts/activate.bat
            - (가상환경 이름) 프럼프트(경로) > 
                - (was) > pip list
        - 필요한 패키지 설치
            - 명령어로 생성하기 (코랩에서 진행)
                - pip freeze > requirements.txt
                - 이미 깔려 있는 것(내가 추가한것 이외의 것들) 다 기록됨
                - 필요한것만 카피해서 로컬 requirements.txt 수정
            - (was) > pip install -r ./flask/requirements.txt
                - txt 경로는 상황에 맞춰서 조정
            - (was) > pip list
    - 요약 (cmd 기준)
        - python -m vens was
        - cd was/Scripts
        - activate
        - ../..
        - pip install -r ./flask/requirements.txt
        - pip list

# 최초코드
    - f1.py 참고
    - template.py 파일을 기본형으로 사용한다.

# 웹서비스 (3-tier, cs)
    - 프런트(or 클라이언트 사이드)
        - html5 : 콘테츠담당, 뼈대 담당 => 데이터가 존재함
            - 데이터 
            - 요소(엘리먼트) 이해
            - 구조, 속성(id, class), 입력태그
        - css3 : 레이아웃 담당, 디자인, 애니메이션
        - bootstrap 이미 완성된 디자인 모듈 활용
            - https://adminlte.io/
        (키프레임), 반응형
            - css selector, xpath -> 요소를 특정하는 방법
        - javascript : 인터렉션담당, 이벤트, 통신, 동적구성
            - javascript > es next(2015~) > typescript
                - vue < react < angular => SPA(Single Page Application)
            - 클라이언트 -> 서버로 데이터를 보내는 방법
                - form 전송 => 로그인등등, 화면 껌벅
                - ajax 통신 => 백그라운드 통신
                - 웹소켓 => 백그라운드 통신, 쌍방향통신, 푸시 => 챗봇베이스
            - 개발 생사성을 높이기 위해 라이브러리 사용 => jQeury, ...

    - 백엔드(or 서버 사이드)
        - flask로 구현
            - 같은 포지션, django, fastapi, springboot, nodejs, .net, php, ...
    - 데이터베이스
        - RDBMS
            - Mysql, MSSQL, Maria, 오로라, oracle, ....
        - No SQL
            - 몽고DB, redis, ....

# 프로젝트 구조
    /
    L basic     : flask를 익히기 위한 예제
        L f1.py
        L f2.py
        L template.py
    L app.py    : 서비스 엔트리 포인트
    L static    : 정적 데이터가 위치하는 곳, 라우팅 필요 없음
                : *.js, *.css, *.이미지파일(png,...)
    L templates : html 위치
        L index.html
    L requirements.txt : 해당 프로젝트에서 사용하는 라이브러리 
    L readme.MD : 설명파일