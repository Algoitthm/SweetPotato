###타겟넘버##
##깊이 우선 탐색##
##타겟 넘버를 만들 수 있는 경우의 수를 리턴##
##숫자를 적절히 더하고 빼서..타겟 넘버를 생성하고자 함!
numbers = [1,1,1,1,1]
target = 3
##DFS 하기
output = [0]
for data1 in numbers:
    tmp = []
    for data2 in output:
        tmp.append(data2+data1) ##더하기
        tmp.append(data2-data1) ##빼기..

    output = tmp  #요소들 더한거나 뺀걸 다시 output으로 받음
# print(output)
answer = output.count(target)
print(answer)