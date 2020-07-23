def solution(N, number):
    answer = -1
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        num_set = {int(str(N)*i)}
        for j in range(1, i+1):
            for x in dp[j]:
                for y in dp[i-j]:
                    num_set.add(x + y)
                    num_set.add(x - y)
                    num_set.add(x * y)
                    if y != 0:
                        num_set.add(x / y)
        if number in num_set:
            return i
        dp[i].update(num_set)

    return answer


if __name__ == '__main__':
    solution(5, 12)
    solution(2, 11)
