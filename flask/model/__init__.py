# 모델 서빙, 예측 처리 기능 제공
import joblib

# 모델, 레이블 로드 처리(전역처리)
import os
# a-z 소문자
from string import ascii_lowercase
#정규식
import re

# print(os.path.abspath(__file__))
# print(os.path.realpath(__file__))
# 경로 만들기 (개발 : 윈도우, 서비스 : 리눅스)
# print(os.path.join(os.path.dirname(__file__), "lang_predict.ml"))

# 1. 모델로드
clf = joblib.load(os.path.join(os.path.dirname(__file__), "lang_predict.ml"))

# 2. 레이블로드
label = joblib.load(os.path.join(os.path.dirname(__file__), "lang_predict.lb"))


# 3. 번역요청 원본 데이터 -> 학습용 전처리 함수
# 텍스트 => 일련의 과정(전처리) => (1, 26), 2차원 리스트

def encode_freqs_data(src : str) -> list:
    """
        - 텍스트 원문 -> 빈도계산 및 정답추출하려 특정구조로 리턴
        - parameters
            - src : 번역 요청 원문 텍스트
        - returns
            - list : [[0.0001, ......]]
    """
    
    ALPHA_LEN   = len(ascii_lowercase) # 1회만 작동하면 됨
    STD_ASCII_A = ord('a')


    
    text        = src.lower()
    p           = re.compile("[^a-z]*")
    text        = p.sub("", text)
    counts      = [0] * ALPHA_LEN

    for ch in text:
        counts[ord(ch) - STD_ASCII_A] += 1
    total_count = len(text)
    counts_norms = list(map(lambda x : x / total_count, counts))

    return [counts_norms]


# 4. 예측 수행 함수
def predict(data : list) -> dict:
    # 4-1. 모델 예측 수행
    pred_y = clf.predict(data)
    print(pred_y)
    # 4-2. 응답 데이터 구성, 실패는 배제
    return {
            "success" : 1,
            "code" : pred_y[0],
            "ko"   : label[pred_y[0]]
        }
    
if __name__ == "__main__":
    # 단위 테스트 용도
    sample_data = """Joseph Crespo dit Monsieur Jo, né le 1er janvier 1925 à Elne (Pyrénées-Orientales) et mort le 7 mai 2004 à Mably (Loire), est un joueur de rugby à XV et international français de rugby à XIII, évoluant au poste de demi de mêlée, de demi d'ouverture ou de centre.

Enfant de Perpignan, il découvre le rugby à XV au sein du club de quartier de l'A.S. Perpignan aux côtés d'un dénommé Puig-Aubert puis tous deux rejoignent l'U.S.A. Perpignan. J. Crespo devient champion de France juniors en 1943 puis champion de France seniors en 1944 dans une équipe perpignanaise comprenant Joseph Desclaux, Puig-Aubert et Frédéric Trescazes contre l'Aviron bayonnais de Jean Dauger sur le score de 20-5.

Le rugby à XIII réapparaît en France en 1944 après son interdiction durant la Seconde Guerre mondiale ; J. Crespo, à l'instar de nombreux Perpignanais tels qu'Henri Riu, rejoint ce code de rugby et s'engage au sein du R.C. Roanne de Claudius Devernois en 1945. Au sein du club roannais, au côté de René Duffort avec qui il perfectionne la passe croisée, il remporte à deux reprises le Championnat de France en 1947 et 1948, puis il rejoint l'U.S. Lyon-Villeurbanne pour deux autres titres en 1951 et 1955, complétés de deux titres de Coupe de France en 1953 et 1954.

Demi de mêlée référence du Championnat de France, capable de jouer en demi d'ouverture ou centre avec autant de succès, il compte également 28 sélections avec l'équipe de France, prenant part aux titres de la Coupe d'Europe des nations en 1949, 1951 et 1952, à la Tournée de l'équipe de France de rugby à XIII en 1951 en Australie et Nouvelle-Zélande, et à la finale de la Coupe du monde en 1954.

Lire la suite"""
    # 데이터 전처리
    preprocessing_data = encode_freqs_data(sample_data)
    # 예측
    result = predict(preprocessing_data)
    print(result)