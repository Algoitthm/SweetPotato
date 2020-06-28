"""
    피보나치 
"""


def solution(N):
    made_list = make_list(N)
    answer = cal_sum(made_list[len(made_list)-1], made_list[len(made_list)-2])
    return answer

def make_list(N):
    result = [1]
    num = 1
    for i in range(N-1):
        result.append(num)
        num = num + result[len(result)-2]
    return result

def cal_sum(a, b):
    return 2 * (a + (a + b))

