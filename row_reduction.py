import numpy as np

def matrix_form_check(matrix):
    """掃き出し法が実行できる行列になっているか"""
    try: 
        (matrix.shape[0] + 1) == matrix.shape[1]
        print("This is row_reductionable!")
    except:
        print("This is row_reductionable!")

def matrix_line_transform(matrix, n):
    if matrix[n, n] != 1: # 対角要素が１になっているか
        matrix[n] = matrix[n] / matrix[n, n]
    for line_num in range(matrix.shape[0]):
        if line_num == n: # 対角要素を含む行は飛ばす
            continue
        else:
            print(matrix[line_num, 0])
            coef = matrix[line_num, n]
            print(coef)
            print(matrix[n])
            tmp = matrix[n] * coef
            matrix[line_num] = matrix[line_num] - tmp
    
    return matrix

if __name__ == "__main__":
    # matrix = np.array([[1, -1, 2, 2],
    #                    [2, -1, 2, 3],
    #                    [1, 2, -3, -3]])
    matrix_form_check(matrix)
    for col_num in range(matrix.shape[1]-1):
        formed_matrix = matrix_line_transform(matrix, col_num)
    print(formed_matrix)
