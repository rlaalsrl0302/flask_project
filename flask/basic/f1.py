# step1 모듈 가져오기
from flask import Flask

# step2 플라스크 객체 생성
app = Flask(__name__)

# step3 특정주소를 요청 -> 해석 -> 누가 처리할지 지정 -> 서버가 응답 => 라우팅

@app.route('/')
def home():
    return "Hello flask 2"

# step4 서버가동
if __name__ == "__main__": # 직접 실행한다면
    # debug = True : 수정 -> 저장 -> 자동 서버 리로드 -> 새로고침 수행
    app.run(debug = True)
