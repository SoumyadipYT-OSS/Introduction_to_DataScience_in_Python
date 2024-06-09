# Regular Expressions

import re

re_example1 = [not re.match("a", "cat")]  # word 'cat' doesn't start with 'a'
print(re_example1)

re_example2 = [not re.search("c", "dog")]  # word 'dog' doesn't have a 'c' letter in it.
print(re_example2)

re_example3 = 3==len(re.split("[ab]", "carbs"))  # split on 'a' or 'b' to
print(re_example3)

re_example4 = "R-D-"==re.sub("[0-9]", "-", "R2D2")  # replace digits with dashes
print(re_example4)


re_examples = [re_example1, re_example2, re_example3, re_example4]
assert all(re_examples)  # all regex examples should be true
