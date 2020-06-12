### TCT 개발언어 B형 : April 18th. 문제 복기 ####
### BY. NARU KANG
## 02. 연속된 숫자의 연속횟수를 이진변환 후 k번 반복
ex_2_1 = '11100110100'
ex_2_2 = '110000'
ex_2_3 = '11111001110'

###  Step 1. 이진변환하는 함수 만들어 놓기 ###
def bin_convert(num_input):
    ### step 1-1. 연속하는 횟수 counting하고 리스트에 넣어두기
    result_num = [] # result_num : 연속한 숫자들의 횟수를 담아놓을 리스트
    cnt_within_same = 1 # cnt_within_same : 독립된 연속 숫자의 반복 횟수. 첫번째 자리의 연속횟수는 1로 시작
    for i in range(1,len(num_input)):
        if num_input[i] == num_input[i-1]: ## 바로 앞의 자리와 현재 자리가 연속될 때 : 연속횟수 1 추가
            cnt_within_same += 1
            if i == len(num_input)-1: # 리스트의 마지막일 때는 계산된 횟수를 넣어줘야 함(1)
                result_num.append(cnt_within_same)
        if num_input[i] != num_input[i-1]:## 바로 앞의 자리와 현재 자리가 다를 때 : 
            result_num.append(cnt_within_same) ## 1) 앞에서 계산한 연속횟수 리스트에 넣고,
            cnt_within_same = 1 ## 2) 연속횟수 초기화
            if i == len(num_input)-1:# 리스트의 마지막일 때는 앞에서 계산된 횟수를 넣어줘야 함.(2)
                result_num.append(cnt_within_same)

    ### step 1-2. 이진변환하는 부분
    bin_result_num_list =[]
    for j in result_num:
        bin_num = bin(j)[2:] # "0b" 이진변환시 문자열 제거
        bin_result_num_list.append(bin_num)

    final_result_num = "".join(bin_result_num_list)
    return final_result_num

### Step 2. 아까 만들어 놓은 함수 k번 반복하는 최종함수 만들기
def my_function_2(num_input, k):
    for i in range(0,k):
        num_input = bin_convert(num_input)
    return num_input

my_function_2(ex_2_1, 2)
my_function_2(ex_2_2, 3)

## Test
print(my_function_2(ex_2_1, 2))
print(my_function_2(ex_2_2, 3))
print(my_function_2(ex_2_3, 10))
