import bisect
def solution(score):
    breakpoints = [60, 70, 80, 90]
    grades = 'FDCBA'
    idx = bisect.bisect_left(breakpoints, score)
    return grades[idx]

a = solution(64)
print(a)
