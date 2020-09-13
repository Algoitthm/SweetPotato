##가장 큰 정사각형 찾기##

# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[1,0],[0,0]]
print(board)

tmp = 0
for i in range(len(board)):
    tmp += sum(board[i][:])
print(tmp)
if board[0][0] == 1 and tmp == 1:
    answer = 1

else:

    max_point = 0
    for i in range(1,len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 0:
                continue
            else:
                min_point = min(board[i][j - 1], board[i - 1][j], board[i - 1][j - 1]) + 1
                board[i][j] = min_point

            if max_point < board[i][j]:
                max_point = board[i][j]

    if max_point == 0:
        answer = 0
    else:
        answer = max_point*max_point

print(answer)
