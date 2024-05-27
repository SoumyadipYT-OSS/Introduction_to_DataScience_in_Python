from typing import List
Vector = List[float]


def dot(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return sum(v_i * w_i  for v_i, w_i in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)



import math
def magnitude(v: Vector) -> float:
    return math.sqrt(sum_of_squares(v))