# Generators

def generate_range(n):
    i=0
    while i<n:
        yield i
        i += 1
        
for i in generate_range(10):
    print(f"i: {i}")
        
    
# for comprehensions
evens_below_20 = (i for i in generate_range(20)  if i%2==0)
print(evens_below_20)


# an enumerate function turn values into pairs