from typing import List, Tuple
Matrix = List[List[float]]

def shape(A: Matrix) -> Tuple[int, int]:
    num_of_rows = len(A)
    num_of_cols = len(A[0]) if A else 0
    return num_of_rows, num_of_cols