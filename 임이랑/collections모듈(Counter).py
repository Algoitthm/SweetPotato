############################################################################
프로그래머스 문제 - 완주하지 못한 선수
code 예시

import collections
p = ['leo', 'kiki', 'eden']
c = ['eden', 'kiki']

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)

    return list(answer.keys())[0]

a = solution(p, c)
print(a)

###########################################################################3

collections.Counter(): 컨테이너에 동일한 값의 자료가 몇개인지를 파악하는데 사용하는 객체이다.
Counter()의 입력값으로 리스트, 딕셔너리, '값 = 개수 형태', 문자열 등이 가능하며, 결과값은 딕셔너리 형채로 출력된다.

아래 블로그에서 상세한 설명을 확인할 수 있다.
출처: https://excelsior-cjh.tistory.com/94 [EXCELSIOR]

