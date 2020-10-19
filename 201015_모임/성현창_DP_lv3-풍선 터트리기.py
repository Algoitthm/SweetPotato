###############################################################
# 서로다른 숫자가 적힌 일렬로 나열된 풍선 n개
# 서로 인접한 2개의 풍선을 선택하여 숫자가 큰 풍선을 터트림
# 단 한 번 작은 숫자 풍선을 터트릴 수 있음
# 이 때 최후까지 남을 수 있는 풍선의 개수를 return
# 
# 1 <= 풍선개수 <= 1000000
# -1000000000 <= 적힌 숫자 <= 1000000000
#
# Point 1:   선택한 풍선을 기점으로 왼쪽 그룹과 오른쪽 그룹의 최솟값보다 값이 작다면
#            선택한 풍선은 최후까지 남을 수 있다.
# Point 2:   첫번재 풍선과 마지막 풍선은 항상 끝까지 남을 수 있다.
###############################################################

def solution(a):
    # 특이 케이스(사실 필요 없음)
    if len(a) == 1:
        return 1
    elif len(a) == 2:
        return 2

    answer = 0
    maps = [[0 for _ in range(len(a))] for _ in range(2)]
    tmp = 9999999999
    # 선택 풍선을 기점으로 왼쪽의 최솟값
    for i in range(0, len(a)):
        if a[i] < tmp:
            tmp = a[i]
        maps[0][i] = tmp
    tmp = 9999999999
    # 선택 풍선을 기점으로 오른쪽의 최솟값
    for i in reversed(range(0, len(a))):
        if a[i] < tmp:
            tmp = a[i]
        maps[1][i] = tmp
    maps
    for i in range(len(a)):
        if a[i] <= maps[0][i] or a[i] <= maps[1][i]:
            # 왼쪽 그룹 또는 오른쪽 그룹보다 작다면 최후까지 남기 가능(같다면 자기가 젤 작다는 뜻)
            answer += 1
    return answer

def search(a, i):
    # TIME OVER --> 했던 계산을 계속 함
    front_lst = a[0:i]
    back_lst = a[i+1:]

    min_front = min(front_lst)
    min_back = min(back_lst)

    if a[i] > min_front and a[i] > min_back:
        return 0
    return 1

def search2(a, i, front, back):
    # TIME OUT --> list 조작이 너무 느림
    if a[i] > front[i-1] and a[i] > back[i+1]:
        return 0
    return 1


if __name__ == "__main__":
    # solution([9,-1,-5])  # 3
    solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])  # 6