from typing import Callable


def twice(repeater: Callable[[str, int], str], s:str) -> str:
    return repeater(s, 2)

def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ', '.join(n_copies)

assert twice(comma_repeater, "type hints")=="type hints, type hints"

print(comma_repeater("Data Science", 3))  # It will print 3 times
print(comma_repeater("Python", 4))  # It will print 4 times