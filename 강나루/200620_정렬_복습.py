#### 정렬방식에 크게 5가지가 있음
## 1) 선택정렬  /  2) 삽입정렬  /  3) 병합정렬  /  4) 퀵정렬  / 5) 버블정렬

## 예제 :
a = [50, 20, 30, 60, 83, 21]

## 01. 선택정렬
def find_min_idx(a):
    n = len(a)
    min_idx = 0
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def sel_sort(a):
    result = []  # 새 리스트를 만들어 정렬된 값을 저장
    while a:     # 주어진 리스트에 값이 남아있는 동안 계속
        min_idx = find_min_idx(a)  # 리스트에 남아 있는 값 중 최솟값의 위치
        value = a.pop(min_idx)    # 찾은 최솟값을 빼내어 value에 저장
        result.append(value)     # value를 결과 리스트 끝에 추가
    return result

## 02. 삽입정렬
# 리스트 r에서 v가 들어가야 할 위치를 돌려주는 함수
def find_ins_idx(r, v):
    # 이미 정렬된 리스트 r의 자료를 앞에서부터 차례로 확인하여
    for i in range(0, len(r)):
        # v 값보다 i번 위치에 있는 자료 값이 크면
        # v가 그 값 바로 앞에 놓여야 정렬 순서가 유지됨
        if v < r[i]:
            return i
    # 적절한 위치를 못 찾았을 때는
    # v가 r의 모든 자료보다 크다는 뜻이므로 맨 뒤에 삽입
    return len(r)

def ins_sort(a):
    result = []  # 새 리스트를 만들어 정렬된 값을 저장
    while a:     # 기존 리스트에 값이 남아 있는 동안 반복
        value = a.pop(0) # 기존 리스트에서 한 개를 꺼냄
        ins_idx = find_ins_idx(result, value)  # 꺼낸 값이 들어갈 적당한 위치 찾기
        result.insert(ins_idx, value)  # 찾은 위치에 값 삽입(이후 값은 한 칸씩 밀려남)
    return result

## 03. 병합정렬
def merge_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요 없음
    if n <= 1:
        return a
    # 그룹을 나누어 각각 병합 정렬을 호출하는 과정
    mid = n // 2  # 중간을 기준으로 두 그룹으로 나눔
    g1 = merge_sort(a[:mid]) # 재귀 호출로 첫 번째 그룹을 정렬
    g2 = merge_sort(a[mid:]) # 재귀 호출로 두 번째 그룹을 정렬
    # 두 그룹을 하나로 병합
    result = []       # 두 그룹을 합쳐 만들 최종 결과
    while g1 and g2:  # 두 그룹에 모두 자료가 남아 있는 동안 반복
        if g1[0] < g2[0]: # 두 그룹의 맨 앞 자료 값을 비교
            # g1의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g1.pop(0))
        else:
            # g2의 값이 더 작으면 그 값을 빼내어 결과로 추가
            result.append(g2.pop(0))
    # 아직 남아 있는 자료들을 결과에 추가
    # g1과 g2 중 이미 빈 것은 while을 바로 지나감
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

### 테스트!
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(merge_sort(d))


### 4) 퀵정렬
def quick_sort(a):
    n = len(a)
    # 종료 조건: 정렬할 리스트의 자료 개수가 한 개 이하이면 정렬할 필요가 없음
    if n <= 1:
        return a
    # 기준 값을 정하고 기준에 맞춰 그룹을 나누는 과정
    pivot = a[-1]  # 편의상 리스트의 마지막 값을 기준 값으로 정함
    g1 = []        # 그룹 1: 기준 값보다 작은 값을 담을 리스트
    g2 = []        # 그룹 2: 기준 값보다 큰 값을 담을 리스트
    for i in range(0, n - 1):  # 마지막 값은 기준 값이므로 제외
        if a[i] < pivot:       # 기준 값과 비교
            g1.append(a[i])    # 작으면 g1에 추가
        else:
            g2.append(a[i])    # 크면 g2에 추가
    # 각 그룹에 대해 재귀 호출로 퀵 정렬을 한 후
    # 기준 값과 합쳐 하나의 리스트로 결괏값 반환
    return quick_sort(g1) + [pivot] + quick_sort(g2)
 
d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))

### 5) 버블 정렬
### 주어진 리스트 왼쪽부터 인접한 두 원소를 비교하여 왼쪽이 오른쪽보다 클 경우에 서로 자리바꿈하고,
### 다시 그 오른쪽에 있는 수와 비교하여 가장 큰 값을 먼저 찾아내는 방법

a = [50, 20, 30, 60, 83, 21]
sorted_a = []

while a: # a에 무언가가 들어있는한 True
    large = a[0]
    for i in range(len(a)-1): # 0 ~ n-2까지 반복
        if a[i] > a[i+1]:
            large = a[i]
            a[i] = a[i+1]
            a[i+1] = large
        else:
            large = a[i+1]
sorted_a.append(large)
a.remove(large)
