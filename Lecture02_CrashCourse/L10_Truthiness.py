all([True, 1, 3])  # all are truthy
all([True, 1, {}])  # False, {} is falsy
any([True, 1, {}])  # True, True is truthy
all([])  # True, no falsy elements in the list
any([])  # False, no truthy elements in the list
