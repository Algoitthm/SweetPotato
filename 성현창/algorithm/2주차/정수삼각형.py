def solution(triangle):
    # result = triangle.pop(0)
    for i in range(len(triangle)):
        if i == 0:
            continue
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])
    answer = max(triangle[len(triangle)-1])
    print(answer)
    return answer

if __name__ == "__main__":
    solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])