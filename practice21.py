###큰 수 만들기
# 어떤 수에서 k 개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자 구하기
number = "1924"
K = 2 #제거할 갯수

import itertools
N = len(number) - K

nums = list(itertools.combinations(list(number),N))
print(nums)
output = []
for number in nums:
    tmp = ''.join(number)
    output.append(int(tmp))
# print(output)
answer = max(output)
print(answer)