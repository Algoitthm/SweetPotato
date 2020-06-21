def solution(stock, dates, supplies, k):
    import heapq
    
    answer = 0
    idx = 0
    pq = []
    
    # 재고가 실제 납품일 까지 감당이 안될 동안
    while stock < k:
        
        # 우선 
        for i in range(idx, len(dates)):
            # 재고가 추가공급일 까지 못가면 heap 넣기를 그만 두고 재고를 충당하러 간다.
            if stock < dates[i]:
                break
            # 해당일의 추가공급을 heap 에다 집어넣기
            # (가장 적은게 왼쪽이니까 -를 붙여서 제일 큰 것이 왼쪽으로 가도록함)
            heapq.heappush(pq, -supplies[i])     
            idx = i + 1
        
        # 추가공급으로 재고 충당하기
        # 현재 까지 확인한 추가공급일 중 큰 것을 넣어준다.
        stock += (heapq.heappop(pq) * -1)
        answer += 1

    return answer