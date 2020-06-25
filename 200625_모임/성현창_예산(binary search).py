def solution(budgets, M):
    answer = 0
    max_budgets = max(budgets)
    data = [i for i in range(max_budgets+1)]
    answer = binary_search(budgets, data, M)

    return answer


def binary_search(budgets, data, M):
    start = 0
    end = len(data) - 1
    ans = 0

    while start <= end:
        mid = (start + end) // 2

        sumed = cal_sum(budgets, data[mid])
        if sumed <= M:
            if mid > ans:
                ans = mid
            start = mid + 1
        else:
            end = mid -1
            
    return ans


def cal_sum(data, mid):
    result = 0
    for i in data:
        if i < mid:
            result += i
        else:
            result += mid
    return result


if __name__ == "__main__":
    solution([120, 110, 140, 150], 485)  # 127