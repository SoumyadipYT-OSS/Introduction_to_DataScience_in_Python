# Flipping a coin
from typing import Tuple
import math

def Normal_Approximation_to_Binomial(n: int, p: float) -> Tuple[float, float]:
    µ = p*n
    σ = math.sqrt(p * (1 - p) * n)
    return µ, σ



from scratch.probability import normal_cdf


def NormalProbabilityAbove(lo: float, µ: float=0, σ:float=1) -> float:
    return normal_cdf(lo, µ, σ)

def NormalProbabilityBetween(lo: float, hi: float, µ: float=0, σ: float=1) -> float:
    return normal_cdf(hi, µ, σ)

def NormalProbabilityOutside(lo: float, hi: float, µ: float=0, σ: float=1) -> float:
    return 1 - NormalProbabilityBetween(lo, hi, µ, σ)


def normal_cdf(x: float, µ: float=0, σ: float=1) -> float:
    return (1 + math.erf((x-µ) / math.sqrt(2) / σ)) / 2
def inverse_normal_cdf(x: float, µ: float=0, σ: float=1) -> float:
    return (1 / normal_cdf(x, µ, σ))
def NormalUpperBound(prob: float, µ: float=0, σ: float=1) -> float:
    return inverse_normal_cdf(prob, µ, σ) 
def NormalLowerBound(prob: float, µ: float=0, σ: float=1) -> float:
    return inverse_normal_cdf(1 - prob, µ, σ)
def Normal_Two_Sided_Bounds(prob: float, µ: float=0, σ: float=1) -> float:
    tail_prob = (1 - prob) / 2
    upper_bound  = NormalUpperBound(tail_prob, µ, σ)
    lower_bound = NormalLowerBound(tail_prob, µ, σ)
    return lower_bound, upper_bound
