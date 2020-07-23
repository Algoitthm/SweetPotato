###문자열 압축
s ='a'

import itertools
#N개로 자름
def making_split(s,N):  ##문자열을 N개 단위로 나누는 함수
    s_list = []
    for i in range(0,len(s),N):
        s_list.append(s[i:i+N])
    # print(s_list)
    return s_list

def making_groups(s_list):
    groups = []  ## 나눈 문자열대로 그룹화 하는 함수 (abab->2ab)
    for key, g in itertools.groupby(s_list,lambda x:x[0:len(s_list[0])]):
        tmp = list(g)
        if len(tmp) != 1:
            groups.append(len(tmp)) ###공통 문자열 갯수

        groups.append(key)
    return groups

def finding_minimum_lenth(groups):
    answer=0
    for i in range(len(groups)):
        answer += len(str(groups[i]))

    return answer

##main 시행 부분 ######
output = []
if len(s) ==1:  #a 같은 경우
    answer = 1
else:
    for N in range(1,len(s)):

        s_list = making_split(s,N)
        groups = making_groups(s_list)
        output.append(finding_minimum_lenth(groups))
        answer = min(output)

print(answer)
