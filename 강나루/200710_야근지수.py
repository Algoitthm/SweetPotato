##### 야근지수 #####
#### 야근피로도 : 야근 시작시점에서 남은 일의 작업량 제곱하여 더한 겂. ####
#### 야근피로도 최소화 하기 ####


## 1차시도 :: 정확도 통과했으나 효율성 테스트를 통과못함
def solution(n, works):
    if sum(works) <= n: #### 만약 주어진 시간내에 남아있는 일을 끝낼수 있다면?
    return 0              ### 0을 반환

    for i in range(1, n+1):   ### 주어진 시간만큼 일을 수행할 것
        works.sort(reverse=True) # 해야할 작업량 중 가장 큰 숫자부터 내림차순 정렬
        if works[0] > 0:
            works[0] = works[0]-1 ## 가장 큰 작업량을 1시간 일했으니 1 뺴줌

    result = [num**2 for num in works] ### 리스트내 숫자들의 제곱값 리스트
    answer = sum(result)
    return answer ## 리스트내 숫자들의 제곱값 합

### Test case
works = [4, 3, 3]; n = 4
works = [2, 1, 2]; n = 1
works = [1,1] ; n = 3

solution(n, works)

### 2차시도!
### 효율성도 통과하려면?
### 첫번째로 큰 값과 두번쨰로 큰 값을 같게 만들며 줄여나가기!


def solution(n, works):
    works_to_do = sum(works)
    time_left = n

    if works_to_do <= time_left: #### 만약 주어진 시간내에 남아있는 일을 끝낼수 있다면?
        return 0                   ### 0을 반환

    while (time_left > 0):   ### 남은 시간이 0이 될 때까지 반복
        works.sort(reverse=True) # 해야할 작업량 중 가장 큰 숫자부터 내림차순 정렬
        works_to_do = sum(works)

        first_max = works[0]
        sec_max = works[1]
        diff_max = first_max-sec_max

        if first_max > sec_max:## 가장 큰 작업량을 두번째로 큰 작업량이랑 똑같게 만들어줌
            works[0] = first_max-diff_max
            time_left = time_left - diff_max
        if first_max == sec_max: ## 차이가 없으면 두번째로 큰 작업량에서 1을 빼줌.
            works[1] = works[1]-1
            time_left = time_left-1

    result = [num**2 for num in works] ### 리스트내 숫자들의 제곱값 리스트
    answer = sum(result)
    return answer ## 리스트내 숫자들의 제곱값 합

### Test case
works = [4, 3, 3]; n = 4
works = [2, 1, 2]; n = 1
works = [1,1] ; n = 3

solution(n, works)

# BUT STILL IMPERFECT...
