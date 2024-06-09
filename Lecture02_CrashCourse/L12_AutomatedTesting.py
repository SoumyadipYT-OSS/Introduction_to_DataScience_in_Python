# Automated Testing and assert

def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40])==5


def smallestItem(xs):
    assert xs, "empty list has no smallest item"
    return min(xs)
