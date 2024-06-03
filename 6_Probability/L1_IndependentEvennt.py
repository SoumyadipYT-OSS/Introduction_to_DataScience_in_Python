def independent_Event(prob_E, prob_F, prob_E_and_F):
    product_of_probs = prob_E * prob_F
    return abs(product_of_probs - prob_E_and_F)


E = 0.3
F = 0.5
E_and_F = 0.15

res = independent_Event(E, F, E_and_F)
print(f"Are events E and F independent? {res}")
