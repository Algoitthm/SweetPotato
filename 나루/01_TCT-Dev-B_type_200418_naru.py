### TCT 개발언어 B형 : April 18th. 문제 복기 ####
### BY. NARU KANG
## 01번. 길이가 n인 리스트에서 k개를 선택한 다음, 조합 내 요소를 +, - , x  했을 때 최소가 되는 경우, 그 값을 리턴!
## k가 2 아니면, 3이었던걸로 기억하는데 그거랑 상관없이 k값 정해주면 계산할 수 있도록 만들어 놓음

ex_1_1 = [1,3,5,10,12] 
ex_1_2 = [3,6,10,12]
ex_1_3 = [5,10,11,13]

# Step 1 : 조합/순열 쓸예정임. 그리고 뺄셈함수와 곱셈함수 정의할 것
from itertools import combinations
from itertools import permutations

#곱셈 함수
def multiply(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans * arr[i]
    return ans

# 뺄셈 함수
def subtract(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans - arr[i]
    return ans

# Step 2 : 본체함수 제작
def my_function_1(input_list, k):
    list_com = list(combinations(input_list, k))  # list_com : 입력 리스트 중 k개를 뽑는 모든 조합. 
    list_per = list(permutations(input_list, k))  # list_per : 입력 리스트 중 k개를 뽑는 모든 순열. 

    list_plus = [sum(list_com[i]) for i in range(0, len(list_com))] # 각 조합요소들의 합 모임.
    list_minus = [subtract(list_per[i]) for i in range(0, len(list_per))] # 각 "순열"요소들의 뺼셈 모임.
    list_times = [multiply(list_com[i]) for i in range(0, len(list_com))] # 각 조합 요소들의 곱셈 모임.

    answer_list = [min(list_plus), min(list_minus), min(list_times)] # 각 연산 모임들의 최소값 리스트
    answer = min(answer_list) # 이 들 중 최소값을 결과값으로 도출
    return answer

print(my_function_1(ex_1_1, 2))
print(my_function_1(ex_1_2, 2))
print(my_function_1(ex_1_3, 2))
