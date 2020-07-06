# 프로그래머스 실패율 문제
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x: result[x], reverse=True)

a = solution(N, stages)
print(a)


# sorted에 dictionary 입력 시 keys가 sort 되어서 출력됨
# sorted 기준 lambda는 result[x]: 즉 value를 기준으로 정렬
# value 기준으로 정렬되지만 정렬 순서대로 dictionary key가 출력됨