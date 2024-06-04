# if x1, ... , xn are random variables with mean  µ  and standard deviation  σ, and if n is large, then:
import numpy as np
def formula1(n, µ, σ):
    random_vars = np.random.normal(µ, σ, n)
    S = np.sum(random_vars) / n
    
    print(f"Approximate mean of S: {S:.4f}")
    print(f"Approximate standard deviation of S: {σ / np.sqrt(n):.4f}")
    


def Bernoulli_trial(p: float) -> int:
    import random
    return 1 if random.random() < p  else 0


def Binomial(n: int, p: float) -> int:
    return sum(Bernoulli_trial(p)  for _ in range(n))

