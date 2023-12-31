# html읽어서 랜더링 후(필요시 데이터를 넣어서 동적구성) 응답 -> SSR(Server Side Rendering)
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 기본 라우팅은 get 방식만 처리된다

@app.route('/')
def home():
    # render_template => templates 폴더 밑에서 index.html을 찾아서 읽어서, 데이터를 버무려서, 동적으로 구성해서 리턴
    return render_template("index.html")

# 별도로 post를 처리하고 싶다면 추가(명시적 표현)
@app.route('/detect_lang', methods = ["POST"])
def detect_lang():
    # 1. 클라이언트가 보낸 내용을 받는다(POST로 보냄) => 요청을 타고 들어온다!!
    # request.form[] 보다는 request.form.get() 방식이 더 안정적이다.
    ori_text = request.form.get("ori_text")
    # 2. 데이터를 전처리 <- 머신러닝 초입에서 구현

    # 3. 모델 로드(서빙을 받음) <- 머신러닝
    # 4. 예측 수행 <- 머신러닝
    # 5. 응답 데이터 구성
    return f"언어 감지 페이지 : {ori_text}"

# http://127.0.0.1:5000/ssgo
# 1개의 url에서 method에 따라 처리를 달리하겠다.
@app.route('/ssgo', methods = ["POST", "GET"])
def ssgo():
    if request.method == "GET":
        return render_template("index2.html")
    else:
        # post 처리
        # 전송한 데이터 추출
        # request.args.get("키") => GET 방식
        ori_text = request.form.get("ori_text")
        print(ori_text)
        
        # 현재 모델이 없으므로 무조건 성공에 영어로 응답하겠다(더미 데이터)
        # python의 딕셔너리 == json == js의 클레스(혹은 객체)
        res = {
            "success" : 1,
            "code" : "en",
            "ko" : "영어"
        }
        # idct => json 문자열로 변환 : jsonify
        return jsonify(res)



if __name__ == "__main__":
    app.run(debug = True)
    


