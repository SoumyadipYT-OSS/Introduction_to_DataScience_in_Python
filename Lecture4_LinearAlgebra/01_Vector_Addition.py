from typing import List
Vector = List[float]

def addTwoVector(v: Vector,  w: Vector) -> Vector:
    assert len(v) == len(w)
    return [v_i + w_i for v_i, w_i in zip(v, w)]




firstVector = [1, 2]
secondVector = [2, 1]

print(addTwoVector(firstVector, secondVector))