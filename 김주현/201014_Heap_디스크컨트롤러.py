# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq

def solution(jobs):
    answer = 0
    count = 0
    last = -1
    h_list = []
    
    # jobs 요청시간순 오름차순 정렬
    jobs.sort()
    
    # 총 소요시간을 작업 최초 시작시간으로 초기화
    time = jobs[0][0]
    
    # 작업이 남아있는 동안,
    while count < len(jobs):
        # 현재 시간
        for req_time, job_spend in jobs:
            if last < req_time <= time:
                # 작업 소요시간으로 min 힙을 만들기 위해 (job_spend, req_time) 푸시
                # 현재 시간 기준으로 요청이 들어온 작업만 힙에 넣는다.
                # 작업 소요시간이 가장 짧은 놈을 구할 수 있다.
                heapq.heappush(h_list, (job_spend, req_time))
        
        # print(time, h_list[0])
        # 바로 수행할 수 있는 작업이 있는 경우 해당 작업 수행하기
        if len(h_list) > 0:
            count += 1
            last = time
            term, start = heapq.heappop(h_list)
            time += term
            answer += (time - start)
        # 바로 수행할 수 있는 작업이 없는 경우 그냥 1초 증가
        else:
            time += 1
            
    return answer//len(jobs)
