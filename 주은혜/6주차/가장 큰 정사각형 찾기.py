
##가장 큰 정사각형 찾기##
# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/12905
# 세부 설명 https://codedrive.tistory.com/53

# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[1,0],[0,0]]
# print(sum(board[0][:]))
# print(sum(board[:][0]))

if board[0][0] == 1 and sum(board[0][:]) == 1 and sum(board[:][0]):
    answer = 1

else:

    max_point = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):

            if board[i][j] == 0:
                continue
            else:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1

                if max_point < board[i][j]:
                    max_point = board[i][j]

            if max_point == 0:
                answer = 0

            else:
                answer = max_point*max_point

print(answer)
