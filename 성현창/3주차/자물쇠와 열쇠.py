import numpy as np
import copy


def solution(key, lock):
    key = np.array(key)
    lock = np.array(lock)
    answer = False
    #  or 사용
    #  1. 4가지 key를 만든다.
    key_list = [key, np.rot90(key), np.rot90(key, 2), np.rot90(key, 3)]
    #  2. lock에 key len - 1 만큼 padding을 만든다.
    padding_lock = make_padding(lock, len(key)-1)
    #  3. kwy 별로 lock의 모든 좌표에 or 시전하여 모두 1인 lock이 나오면 true else false
    for i in key_list:
        if compare(i, padding_lock):
            return True
    return answer

def make_padding(lock, i):
    asdf = 2 * i + len(lock)
    result = np.ones((asdf, asdf))
    result[i:lock.shape[0]+i, i:lock.shape[1]+i] = lock
    return result


def compare(key, lock):
    tmp = len(lock)-len(key)+1
    for i in range(tmp):
        for j in range(tmp):
            result = copy.deepcopy(lock)
            result[i:key.shape[0] + i, j:key.shape[1] + j] += key
            if not check_zeros(result):
                return True
    return False

def check_zeros(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return True
    return False


if __name__ == "__main__":
    solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])