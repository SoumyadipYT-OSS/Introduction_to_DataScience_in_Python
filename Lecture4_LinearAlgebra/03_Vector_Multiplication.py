from typing import List
Vector = List[float]

def mulTwoVector(v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i * w_i  for v_i, w_i in zip(v, w)]

firstVector = [3, 5]
secondVector = [4, 6]

print(mulTwoVector(firstVector, secondVector))
