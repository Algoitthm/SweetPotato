##멀리뛰기##
##효진이는 한번에 1칸 혹은 2칸만 뛸 수 있음!
##멀리뛰기에 사용될 칸 수 n 이 주어질때, 끝에 도달아는 방법의 수를 1234567로 나눈 값 리턴하기


# 1과 2만 사용해서,, 더해서 n이 나오는 경우의 수
'''
6은?
111111 -> 1개 6C0
11112 -> 5개  5C1
1122 -> 6개 4C2
222 -> 1개  3C3

5는?
11111 -> 5C0
1112 -> 4C1
122 -> 3C2


n이 짝수일 경우
nC0 + n-1C1 + n-2C2 ..n//2Cn//2

즉 n이 홀수일 경우
nC0 + n-1C1 + ..n-1//2 +1 C n-1//2

 
'''
import operator as op
from functools import reduce

def nCr(n,r):
    if n < 1 or r <0 or n<r :
        raise ValueError
    r = min(r ,n-r)
    numerator = reduce(op.mul,range(n,n-r,-1),1)
    denominator = reduce(op.mul,range(1,r+1),1)
    return numerator//denominator

n = 5
if n%2 == 0:  ##n이 짝수면
    first_num = n
    last_num = n//2

    N = [i for i in range(first_num,last_num-1,-1)]
    r = [j for j in range(0,last_num+1,1)]

    hap = 0
    for n,r in zip(N,r):
        tmp = nCr(n,r)
        hap += tmp

else: ## n이홀수면
    first_num = n
    last_num = n//2

    N = [i for i in range(first_num, last_num , -1)]
    r = [j for j in range(0, last_num + 1, 1)]

    hap = 0
    for n,r in zip(N,r):
        tmp = nCr(n,r)
        hap += tmp

answer = hap % 1234567