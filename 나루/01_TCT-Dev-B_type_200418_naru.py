### TCT ���߾�� B�� : April 18th. ���� ���� ####
### BY. NARU KANG
## 01��. ���̰� n�� ����Ʈ���� k���� ������ ����, ���� �� ��Ҹ� +, - , x  ���� �� �ּҰ� �Ǵ� ���, �� ���� ����!
## k�� 2 �ƴϸ�, 3�̾����ɷ� ����ϴµ� �װŶ� ������� k�� �����ָ� ����� �� �ֵ��� ����� ����

ex_1_1 = [1,3,5,10,12] 
ex_1_2 = [3,6,10,12]
ex_1_3 = [5,10,11,13]

# Step 1 : ����/���� ��������. �׸��� �����Լ��� �����Լ� ������ ��
from itertools import combinations
from itertools import permutations

#���� �Լ�
def multiply(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans * arr[i]
    return ans

# ���� �Լ�
def subtract(arr):
    ans = arr[0]
    for i in range(1, len(arr)):
        ans = ans - arr[i]
    return ans

# Step 2 : ��ü�Լ� ����
def my_function_1(input_list, k):
    list_com = list(combinations(input_list, k))  # list_com : �Է� ����Ʈ �� k���� �̴� ��� ����. 
    list_per = list(permutations(input_list, k))  # list_per : �Է� ����Ʈ �� k���� �̴� ��� ����. 

    list_plus = [sum(list_com[i]) for i in range(0, len(list_com))] # �� ���տ�ҵ��� �� ����.
    list_minus = [subtract(list_per[i]) for i in range(0, len(list_per))] # �� "����"��ҵ��� �E�� ����.
    list_times = [multiply(list_com[i]) for i in range(0, len(list_com))] # �� ���� ��ҵ��� ���� ����.

    answer_list = [min(list_plus), min(list_minus), min(list_times)] # �� ���� ���ӵ��� �ּҰ� ����Ʈ
    answer = min(answer_list) # �� �� �� �ּҰ��� ��������� ����
    return answer

print(my_function_1(ex_1_1, 2))
print(my_function_1(ex_1_2, 2))
print(my_function_1(ex_1_3, 2))
