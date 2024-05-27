from typing import List, Tuple

Matrix = List[List[float]]
Vector = List[float]


def shape(A: Matrix) -> Tuple[int, int]:
    num_of_rows = len(A)
    num_of_cols = len(A[0]) if A else 0
    return num_of_rows, num_of_cols


def get_row(A: Matrix, i: int) -> Vector:
    return A[i]

def get_column(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]

ex1_matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0]
]

# Specify valid row and column indices
row_index = 1  # Choose a valid row index (0, 1, or 2)
column_index = 2  # Choose a valid column index (0, 1, or 2)

print(f"Row {row_index}: {get_row(ex1_matrix, row_index)}")
print(f"Column {column_index}: {get_column(ex1_matrix, column_index)}")

