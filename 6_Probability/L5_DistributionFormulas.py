# Probability Density Function

def uniform_pdf(x: float) -> float:
    return 1 if 0 <= x < 1 else 0


# Cumulative Distribution Function
def uniform_cdf(x: float) -> float:
    if x < 0:
        return 0
    elif x < 1:
        return x
    else:
        return 1
    


# Normal Distribution 
import math
SQRT_TWO_PI = math.sqrt(2*math.pi)
def normal_pdf(x: float, meu: float=0, sigma: float=1) -> float:
    return (1/SQRT_TWO_PI*sigma) * (math.exp(-(x-meu)**2 / (2*sigma) ** 2))
