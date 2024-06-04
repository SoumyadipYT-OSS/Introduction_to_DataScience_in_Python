values = list(range(10))
probabilities = [1/10] * 10

expected_value_range10 = sum(x * p for x, p in zip(values, probabilities))
print(f"The expected value of the range(10) variable is: {expected_value_range10}")