from typing import List
Vector = List[float]


def Vector_SUM(vectors: List[Vector]) -> Vector:
    assert vectors
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements  for v in vectors)
    return [sum(vector[i]  for vector in vectors) for i in range(num_elements)]



vectorLists = [ [1,2], [3,4], [5,6] ]

print(Vector_SUM(vectorLists))
