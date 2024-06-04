# p-Values
from scratch.probability import normal_cdf

def NormalProbabilityBelow(x: float, µ: float=0, σ: float=1) -> float:
    return normal_cdf
def NormalProbabilityAbove(lo: float, µ: float=0, σ: float=1) -> float:
    return normal_cdf(lo, µ, σ)

def two_sided_p_value(x: float, µ: float=0, σ: float=1) -> float:
    if x >= µ:
        return 2 * NormalProbabilityAbove(x, µ, σ)
    else:
        
        return 2 * NormalProbabilityBelow(x, µ, σ)