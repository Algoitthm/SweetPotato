### TCT 개발언어 B형 : April 18th. 문제 복기 ####
### BY. NARU KANG
## 03. 리스트의 숫자들을 두 그룹으로 분할한 다음, 각 그룹의 합 차이 중 최솟값은?
ex_3_1 = [1,3,5,9]
ex_3_2 = [10,5,19,14]
ex_3_3 = [5,9,10,21,19]


from itertools import combinations
from collections import Counter

def my_function_3(input_list):
    list_1 = []
    for k in range(2,len(input_list)):
        list_0 = list(combinations(input_list, k))  # List 0.입력 리스트 중 k개를 뽑는 모든 조합. 
        list_1 = list_1 + list_0  # List 0은 반복문을 통해 K가 2부터 입력리스트의 길이보다 1 작은 수까지 모두 합쳐줌.

    list_2 = [list(set(input_list)-set(list_1[i])) for i in range(0, len(list_1))]  # List 2 : List 1의 각 요소에서 입력 List를 뺀 요소들의 모임 


    list_1_sum = [sum(list_1[i]) for i in range(0, len(list_1))] # List 1의 각 요소들의 합 모임.
    list_2_sum = [sum(list_2[i]) for i in range(0, len(list_2))] # List 2의 각 요소들의 합 모임
    lists_sum_diff = [abs(list_1_sum[i]-list_2_sum[i]) for i in range(0, len(list_1_sum))] # List 1, 2 요소들의 차이

    answer = min(lists_sum_diff) # 이 중에서 최솟값을 함수의 결과 값으로 출력
    return answer

## Test
print(my_function_3(ex_3_1))
print(my_function_3(ex_3_2))
print(my_function_3(ex_3_3))
