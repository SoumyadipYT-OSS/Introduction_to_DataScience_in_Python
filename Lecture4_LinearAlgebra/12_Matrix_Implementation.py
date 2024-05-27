from typing import List, Tuple
Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
    num_of_rows = len(A)
    num_of_cols = len(A[0]) if A else 0
    return num_of_rows, num_of_cols


# example
matrix1 = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
]

rows, cols = shape(matrix1)
print(f"Matrix shape:  {rows} rows x {cols} columns")

print(f"Element at A[1][2]: {matrix1[1][2]}")