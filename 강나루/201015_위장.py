### 문제 주소 : https://programmers.co.kr/learn/courses/30/lessons/42578

from collections import Counter ### Counter 불러오기

def solution(items):
    typeOfClothes = Counter([item[1] for item in items])  ## 옷 종류별로 개수 구하기

    answer = 1 ## 기본 값 = 1
    for i in typeOfClothes:
           answer = answer * (typeOfClothes[i] + 1)       ## 각 옷 종류별로 가진 옷수에서 1을 더 함(안 걸치는 것도 가능하므로)

    answer = answer - 1                                   ## 모든 종류에서 아무것도 안 걸친 경우 빼기

    return answer
