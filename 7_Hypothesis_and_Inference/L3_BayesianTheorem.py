# Bayesian Inference
import math
def B(α: float, ß: float) -> float:
    return math.gamma(α) * math.gamma(ß) / math.gamma(α + ß)

def ß_pdf(x: float, α: float, ß: float) -> float:
    if x<=0  or  x>=1:
        return 0
    return x ** (α-1) * (1-x) ** (ß-1) / B(α, ß)