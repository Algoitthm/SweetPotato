#추가, 연속적인 문자열의 갯수 구하기 (groupby 안씀 / 씀 둘다)

a = '11100100011'  #3,2,1,3,2
a = list(a)
output = []
cnt = 1
tmp = []
for i in range(len(a)-1):

    if a[i] == a[i+1]:
        cnt +=1
        if i == len(a)-2: ##리스트 맨 마지막부분.. range가 뒤가 열린구간이라 맨 마지막은 len(a)-1-1임
            output.append(cnt)
    else:
        output.append(cnt)
        cnt = 1

print(output)

import itertools
groups = []

for k, g in itertools.groupby(a,lambda x:x[0]):
    groups.append(list(g))
print(groups)

output=[]
for data in groups:
    output.append(len(data))

print(output)

###요약버전
groups = []
for k, g in itertools.groupby(a,lambda x:x[0]):
    groups.append(len(list(g)))
print(groups)
