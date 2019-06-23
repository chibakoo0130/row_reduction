import row_reduction
import numpy as np


form = [int(x) for x in input("行列の行数、列数を入力:" ).split()]

matrix = [int(y) for y in input("行列の要素を入力:").split()]
matrix = np.reshape(matrix, (form[0], form[1]))

row_reduction.matrix_form_check(matrix)
row_reduction.matrix_line_transform(matrix)