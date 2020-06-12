### TCT ���߾�� B�� : April 18th. ���� ���� ####
### BY. NARU KANG
## 02. ���ӵ� ������ ����Ƚ���� ������ȯ �� k�� �ݺ�
ex_2_1 = '11100110100'
ex_2_2 = '110000'
ex_2_3 = '11111001110'

###  Step 1. ������ȯ�ϴ� �Լ� ����� ���� ###
def bin_convert(num_input):
    ### step 1-1. �����ϴ� Ƚ�� counting�ϰ� ����Ʈ�� �־�α�
    result_num = [] # result_num : ������ ���ڵ��� Ƚ���� ��Ƴ��� ����Ʈ
    cnt_within_same = 1 # cnt_within_same : ������ ���� ������ �ݺ� Ƚ��. ù��° �ڸ��� ����Ƚ���� 1�� ����
    for i in range(1,len(num_input)):
        if num_input[i] == num_input[i-1]: ## �ٷ� ���� �ڸ��� ���� �ڸ��� ���ӵ� �� : ����Ƚ�� 1 �߰�
            cnt_within_same += 1
            if i == len(num_input)-1: # ����Ʈ�� �������� ���� ���� Ƚ���� �־���� ��(1)
                result_num.append(cnt_within_same)
        if num_input[i] != num_input[i-1]:## �ٷ� ���� �ڸ��� ���� �ڸ��� �ٸ� �� : 
            result_num.append(cnt_within_same) ## 1) �տ��� ����� ����Ƚ�� ����Ʈ�� �ְ�,
            cnt_within_same = 1 ## 2) ����Ƚ�� �ʱ�ȭ
            if i == len(num_input)-1:# ����Ʈ�� �������� ���� �տ��� ���� Ƚ���� �־���� ��.(2)
                result_num.append(cnt_within_same)

    ### step 1-2. ������ȯ�ϴ� �κ�
    bin_result_num_list =[]
    for j in result_num:
        bin_num = bin(j)[2:] # "0b" ������ȯ�� ���ڿ� ����
        bin_result_num_list.append(bin_num)

    final_result_num = "".join(bin_result_num_list)
    return final_result_num

### Step 2. �Ʊ� ����� ���� �Լ� k�� �ݺ��ϴ� �����Լ� �����
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
