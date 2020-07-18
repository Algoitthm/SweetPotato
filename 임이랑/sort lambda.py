numbers = [70, 0, 0, 0]
def solution(numbers):
    answer = ''
    num_list = []
    for i in range(len(numbers)):
        strnum = str(numbers[i])
        num_list.append(strnum)
    num_list.sort(key=lambda x: x*3, reverse=True)
    for i in range(len(num_list)):
        answer += num_list[i]
    for value in answer:
        if value!='0':
            return answer
    return '0'

a = solution(numbers)
print(a)

#####################
# sort함수에서 key=lambda x: ??? 를 설정하면 ?? 기준으로 정렬함
# ??에는 수식이 들어가도 됨