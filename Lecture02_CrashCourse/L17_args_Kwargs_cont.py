# args and kwargs cont...

def f2(x, y):
    return x + y

def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
assert g(1, 2) == 6