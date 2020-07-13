###타일 장식물##
N = 5
##직사각형 길이를 구하는 함수
def making_length(N):
    first = 1
    sec = 1
    output = []
    output.append(first)
    output.append(sec)
    for i in range(N-1):

        next = output[i]+output[i+1]
        output.append(next)
    return output

## 해당 길이를 통해 최종 값을 리턴
output = making_length(5)
answer = (output[-1]+output[-2])*2
print(answer)