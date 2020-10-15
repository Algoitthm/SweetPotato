
##가장 큰 정사각형 찾기##
# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/12905
# 세부 설명 https://codedrive.tistory.com/53

# board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[1,0],[0,0]] ##특수한 경우
# print(sum(board[0][:]))
# print(sum(board[:][0]))

##첫 행 첫 열 값만 1이고 나머지값이 모두 0으로 채워진 행렬일 경우, 무조건 답으로 1을 반환함
if board[0][0] == 1 and sum(board[0][:]) == 1 and sum(board[:][0]):
    answer = 1

else:

    max_point = 0 # 초기 최대 값을 0으로 설정
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):

            if board[i][j] == 0:
                continue
            else:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1 # 왼쪽/위쪽/ 대각선 방향으로 값을 비교하여, 모두 1로 채워져 있으면 해당 값에 1을 더한 값을 넣어줌

                if max_point < board[i][j]:  #최대값을 board[i][j] 값으로 업데이트
                    max_point = board[i][j]

            if max_point == 0:
                answer = 0

            else:
                answer = max_point*max_point

print(answer)
