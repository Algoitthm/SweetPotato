def solution(money):
    answer = 0
    
    # n번째 집까지 털었을 때의 최대값이라면
    # n-1번째 집을 털었다면? n번째 못털음. n-1까지의 최대값
    # n-1번째 집을 못털었다면? n-2번째 털음 + n번째 털음
    
    # 첫째 집을 털었다면?(마지막집은 첫째집과 연결되어있어서 못텀)
    house = [0]*len(money)
    house[0] = money[0]
    house[1] = house[0]
    for i in range(2, len(money)-1):
        house[i] = max(house[i-1], house[i-2]+money[i])

    
    # 첫째집을 털지 않으면?(마지막집 털 수 있음)
    house2 = [0]*len(money)
    house2[1] = money[1]
    for i in range(2, len(money)):
        house2[i] = max(house2[i-1], house2[i-2]+money[i])
    
    return max(max(house), max(house2))
