"""
    [direction, 행, 열, 행, 열]
    행렬 밀기
"""

import numpy as np


def solution(len_x, len_y, input_list):
    # make matrix
    matrix = make_matrix(len_x, len_y)
    result = 0
    for i in input_list:
        direction, y1, x1, y2, x2 = i
        # extract matrix
        sub_matrix = extract_matrix(matrix, y1, x1, y2, x2)
        # swipe matrix
        sub_matrix, answer = swipe_matrix(sub_matrix, direction)
        # insert matrix
        matrix = insert_matrix(matrix, sub_matrix, y1, x1, y2, x2)
        result += answer
    return result


def make_matrix(x, y):
    result = np.arange(x*y).reshape(y, x)
    return result


def extract_matrix(matrix, y1, x1, y2, x2):
    result = matrix[x1:x2+1, y1:y2+1].copy()
    return result


def insert_matrix(matrix, sub_matrix, y1, x1, y2, x2):
    matrix[x1:x2+1, y1:y2+1] = sub_matrix
    return matrix


def swipe_matrix(matrix, direction):
    result = matrix
    len_x = len(result[0])
    len_y = len(result)
    if direction == 0: #  down
        save_sub_matrix = result[len_y-1,:].copy()
        result[1:len_y,:] = result[:len_y-1,:]
        result[0,:] = save_sub_matrix
    elif direction == 1:  # up
        save_sub_matrix = result[0, :].copy()
        result[:len_y-1,:] = result[1:len_y,:]
        result[len_y-1, :] = save_sub_matrix
    elif direction == 2:  # right
        save_sub_matrix = result[:, len_x-1].copy()
        result[:, 1:len_x] = result[:, :len_x-1]
        result[:,0] = save_sub_matrix
    elif direction == 3:  # left
        save_sub_matrix = result[:,0].copy()
        result[:,:len_x-1] = result[:,1:len_x]
        result[:, len_x-1] = save_sub_matrix
    answer = sum(save_sub_matrix)
    return result, answer


if __name__ == "__main__":
    # solution(4, 5, [[0, 1, 2, 3, 3]])
    # solution(4, 5, [[1, 1, 2, 3, 3]])
    # solution(4, 5, [[2, 1, 2, 3, 3]])
    solution(4, 5, [[3, 1, 2, 3, 3]])