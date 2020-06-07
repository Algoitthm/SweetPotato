"""
    split list to 2 lists
    find min(sum diff)
"""
from itertools import product


def solution(num_list):
    result = float('inf')
    all_combination_result = two_partitions(num_list)
    for i in all_combination_result:
        a, b = i
        calculation = abs(sum(a) - sum(b))
        if calculation < result:
            result = calculation
    return result


def two_partitions(S):
    facs = S
    res = []
    for pattern in product([True, False], repeat=len(facs)):
        l1 = ([x[1] for x in zip(pattern, facs) if x[0]])
        l2 = ([x[1] for x in zip(pattern, facs) if not x[0]])
        if l1 and l2:
            res.append([l1, l2])
    return res


if __name__ == "__main__":
    solution([1, 2, 3, 4])  # 0
    solution([1, -1, 1, 1])  # 0
    solution([1, -1, 1, 1, 1])  # 1