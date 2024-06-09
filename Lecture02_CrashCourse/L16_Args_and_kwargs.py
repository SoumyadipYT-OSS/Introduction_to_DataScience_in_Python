# args and kwargs

def magic(*args, **kwargs):
    print("unamed args: ", args)
    print("keyword args: ", kwargs)

ex1 = magic(1, 2, key="word", key2="word2")
print(ex1)
print("\n")



def magic2(*args, **kwargs):
    print("unnamed arguments: ", args)
    print("named arguments: ", kwargs)

ex2 = magic2(1, 2, "Data Science", 3, "Python", key="ID-SUP", key2=8.5, key3="Grade")
print(ex2)