### TCT ���߾�� B�� : April 18th. ���� ���� ####
### BY. NARU KANG
## 03. ����Ʈ�� ���ڵ��� �� �׷����� ������ ����, �� �׷��� �� ���� �� �ּڰ���?
ex_3_1 = [1,3,5,9]
ex_3_2 = [10,5,19,14]
ex_3_3 = [5,9,10,21,19]


from itertools import combinations
from collections import Counter

def my_function_3(input_list):
    list_1 = []
    for k in range(2,len(input_list)):
        list_0 = list(combinations(input_list, k))  # List 0.�Է� ����Ʈ �� k���� �̴� ��� ����. 
        list_1 = list_1 + list_0  # List 0�� �ݺ����� ���� K�� 2���� �Է¸���Ʈ�� ���̺��� 1 ���� ������ ��� ������.

    list_2 = [list(set(input_list)-set(list_1[i])) for i in range(0, len(list_1))]  # List 2 : List 1�� �� ��ҿ��� �Է� List�� �� ��ҵ��� ���� 


    list_1_sum = [sum(list_1[i]) for i in range(0, len(list_1))] # List 1�� �� ��ҵ��� �� ����.
    list_2_sum = [sum(list_2[i]) for i in range(0, len(list_2))] # List 2�� �� ��ҵ��� �� ����
    lists_sum_diff = [abs(list_1_sum[i]-list_2_sum[i]) for i in range(0, len(list_1_sum))] # List 1, 2 ��ҵ��� ����

    answer = min(lists_sum_diff) # �� �߿��� �ּڰ��� �Լ��� ��� ������ ���
    return answer

## Test
print(my_function_3(ex_3_1))
print(my_function_3(ex_3_2))
print(my_function_3(ex_3_3))
