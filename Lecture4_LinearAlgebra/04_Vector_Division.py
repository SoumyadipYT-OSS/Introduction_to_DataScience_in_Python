from typing import List
Vector = List[float]


def divTwoVector(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i / w_i  for v_i, w_i in zip(v, w)]


firstVector = [10, 8]
secondVector = [6, 4]
print(divTwoVector(firstVector, secondVector))