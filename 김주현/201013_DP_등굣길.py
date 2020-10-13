def solution(m, n, puddles):
    maplist = [[0] * m for _ in range(n)]
    # print(maplist)
    # m이 column수, n이 row수
    
    # 못가는 길에 -1 표시
    for puddle in puddles:
        maplist[puddle[1]-1][puddle[0]-1] = -1
        
    # 0,0에 도달하는방법 1개
    maplist[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            # 현위치가, 
            # 시작점이면 그대로
            if i == 0 and j == 0:
                maplist[i][j] = 1
                continue
            # 물웅덩이면 갈 방법없음
            elif maplist[i][j] == -1:
                maplist[i][j] = 0
                continue
            # 아직 가로첫줄이면, 현재칸에 오는 방법은 위칸이 없으므로 이전의 왼쪽칸에서 오는 것 뿐이다.
            elif i == 0 and j >= 1:
                maplist[i][j] = maplist[i][j-1]
                continue
            # 아직 세로첫줄이면, 현재칸에 오는 방법은 왼칸이 없으므로 이전의 위쪽칸에서 오는 것 뿐이다.
            elif j == 0 and i >= 1:
                maplist[i][j] = maplist[i-1][j]
                continue 
            
            # 현재칸은 왼쪽칸과 윗칸에 가는 가짓수가 더해진 것.
            maplist[i][j] = (maplist[i-1][j] + maplist[i][j-1]) % 1000000007
            
    return maplist[n-1][m-1]
