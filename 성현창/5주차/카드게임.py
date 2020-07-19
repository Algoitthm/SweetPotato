"""
    20200712
    https://programmers.co.kr/learn/courses/30/lessons/42896
"""
def solution(left, right):
    number = len(left)+1
    dp = [[0]*number for _ in range(number)]
    for left_idx in range(len(left)):
        for right_idx in range(len(right)):
            if right[right_idx] < left[left_idx]:
                dp[left_idx][right_idx] = dp[left_idx][right_idx-1] + right[right_idx]
            else:
                dp[left_idx][right_idx] = max(dp[left_idx-1][right_idx],
                                              dp[left_idx-1][right_idx-1])
    answer = max(max(i) for i in dp)
    return answer



if __name__ == "__main__":
    print(solution([3, 3, 1], [7, 7, 1]))  # 1
    print(solution([1, 3, 3], [1, 7, 7]))  # 1
    print(solution([1, 1, 1, 1, 3], [2, 3, 1, 1, 1]))  # 3
    print(solution([3, 2, 5], [2, 4, 6]))  # 6

