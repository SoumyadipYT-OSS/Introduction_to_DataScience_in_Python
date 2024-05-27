from typing import List, Tuple, Callable
Matrix = List[List[float]]


Vector = List[float]


def shape(A: Matrix) -> Tuple[int, int]:
    num_of_rows = len(A)
    num_of_cols = len(A[0]) if A else 0
    return num_of_rows, num_of_cols


def make_matrix(num_rows: int, num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    return [[entry_fn(i, j)
             for j in range(num_cols)]
             for i in range(num_rows)]


# Here entry_fn is a function for generating its elements