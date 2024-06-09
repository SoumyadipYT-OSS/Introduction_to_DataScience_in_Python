# Zip and Argument Unpacking (* performs argument unpacking)

pairs = [ ('a', 1), ('b', 2), ('c', 3) ]
letters, numbers = zip(*pairs)   # * is a 'asterick' sign
print(letters)
print(numbers)