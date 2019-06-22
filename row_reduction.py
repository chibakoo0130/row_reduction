import numpy as np
def matrix_form_check(matrix):
    try: 
        matrix.shape[0] + 1 == matrix.shape[1]
    except:
        print("This in row_reductionable!")

def matrix_line_transform(matrix, n):
    if matrix[n, n] != 1:
        matrix[n] = matrix[n] / matrix[n, n]
    
    for line_num in range(matrix.shape[0]):
        if line_num == n: 
            continue
        else:
            matrix[line_num] = matrix[line_num] / matrix[n]
    
    return matrix

if __name__ == "__main__":
    matrix = np.array([[1, -2, -3],
                       [-1, 3, 4],
                       [2, -3, -4]])
    matrix_form_check(matrix)
    for i in range(matrix.shape[0]):
        formed_matrix = matrix_line_transform(matrix, i)
    print(formed_matrix)
