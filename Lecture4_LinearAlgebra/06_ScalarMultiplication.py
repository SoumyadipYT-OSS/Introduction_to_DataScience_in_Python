from typing import List
Vector = List[float]


def scalarMultiplication(c: float, v: Vector) -> Vector:
    return [c * v_i  for v_i in v]



scalarValue = 5
givenVector = [1, 2, 3]

print(scalarMultiplication(scalarValue, givenVector))
