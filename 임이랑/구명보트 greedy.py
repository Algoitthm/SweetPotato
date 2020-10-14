people = [70, 50, 80, 50]
limit = 100

def solution(people, limit):
    # 전부 한 명씩 한 보트를 탄다고 생각
    answer = len(people)
    # 무거운 순서대로 정렬
    people_lst = sorted(people, reverse = True)
    print(people_lst)
    heavy = 0
    light = len(people_lst)-1
    while heavy < light :
        if people_lst[light]+people_lst[heavy] <= limit :
            light-=1
            answer-=1
        heavy+=1
    return answer

a = solution(people, limit)
print(a)