from typing import List
Vector = List[float]


def scalar_Multiply(c: float, v: Vector) -> Vector:
    return [c * v_i  for v_i in v]


def vectorSUM(vectors: List[Vector]) -> Vector:
    assert vectors
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements  for v in vectors)
    return [sum(vector[i]  for vector in vectors) for i in range(num_elements)]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return scalar_Multiply(1/n, vectorSUM(vectors))



givenVector_List = [ [1, 3], [4, 2], [6, 3], [5, 8] ]
ans = vector_mean(givenVector_List)
print(ans)