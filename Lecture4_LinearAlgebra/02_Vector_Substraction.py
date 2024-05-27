from typing import List
Vector = List[float]

def subTwoVector(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i - w_i  for v_i, w_i in zip(v, w)]


firstVector = [2, 3]
secondVector = [1, 2]

print(subTwoVector(firstVector, secondVector))