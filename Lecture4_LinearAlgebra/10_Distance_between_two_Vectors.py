from typing import List
Vector = List[float]


def dot(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return sum(v_i * w_i  for v_i, w_i in zip(v, w))


def subtract(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i  for v_i, w_i in zip(v, w)]



def sum_of_squares(v: Vector) -> float:
    import math
    return math.sqrt(dot(v, v))



# squared distance
def squared_distance(v: Vector, w: Vector) -> float:
    return sum_of_squares(subtract(v, w))


# distance function
def distance(v: Vector, w: Vector) -> float:
    import math
    return math.sqrt(squared_distance(v, w))


matrix1 = [1, 2, 3]
matrix2 = [4, 5, 6]

print(distance(matrix2, matrix1))