# Typing module

from typing import List

def total(xs: List[float]) -> float:
    return sum(xs)

a = [2, 6]
print(total(a))
