# n은 자릿수
# 십진수로 이루어진 두 배열을 각각 2진수화 후 각 자리에 두 이진수에서 어느 하나라도 1이면 "#", 둘다 0이면 " "
# arr1 [01001, 10100, 11100, 10010, 01011]
# arr2 [11110, 00001, 10101, 10001, 11100]
# 답 ["#####","# # #", "### #", "# ##", "#####"]


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

# def solution(n, arr1, arr2):
#     answer = []
#     binList = []
#     for i in range(len(arr1)):
#         bin1 = int(bin(arr1[i])[2:])
#         bin2 = int(bin(arr2[i])[2:])
#         binnum = str(bin1 + bin2)
#         while(len(binnum) != n):
#             binnum = '0' + binnum
#         binList.append(binnum)
#
#     for com in binList:
#         temp = ''
#         for i in com:
#             if i == '0':
#                 temp += ' '
#             else:
#                 temp += '#'
#         answer.append(temp)
#     return answer

#### 간단한 코드 #################
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:]) # 비트 연산자 사용 | : or
        print(a12)
        a12=a12.rjust(n,'0') # n을 기준으로 오른쪽 정렬후 공백 '0'으로 채움
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
##############################

a = solution(n, arr1, arr2)
print(a)