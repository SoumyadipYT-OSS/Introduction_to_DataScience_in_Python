from typing import List
Vector = List[float]


def dotProduct (v: Vector, w: Vector) -> Vector:
    assert len(v) == len(w)
    return sum(v_i * w_i  for v_i, w_i in zip(v, w))


firstMatrix = [1, 2, 3]

secondMatrix = [4, 10, 5]


ans = dotProduct(firstMatrix, secondMatrix)
print(ans)