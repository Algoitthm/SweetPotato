def solution(n):
    answer = run(n)
    answer %= 1000000007
    return answer


def run(n):
    result = [1,2,3]
    for i in range(3, n):
        result.append(result[i-1] + result[i-2])
    return result[n-1]