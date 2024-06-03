def conditional_probability(prob_E_and_F, prob_F):
    return prob_E_and_F / prob_F

# Example usage:
prob_e_and_f = 0.15  # Probability of both events E and F happening together
prob_f = 0.5  # Probability of event F

conditional_prob_e_given_f = conditional_probability(prob_e_and_f, prob_f)
print(f"Conditional probability P(E | F): {conditional_prob_e_given_f:.4f}")
