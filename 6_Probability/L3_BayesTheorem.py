def Bayes_Theorem(prob_E_subject_F, prob_F_subject_E, prob_E):
    prob_F = prob_F_subject_E * prob_E + (1 - prob_E)
    posterior = (prob_F_subject_E * prob_E) / prob_F
    return posterior


p_e_given_f = 0.8  # Probability of E given F
p_f_given_e = 0.6  # Probability of F given E
p_e = 0.5  # Prior probability of E

posterior_prob = Bayes_Theorem(p_e_given_f, p_f_given_e, p_e)
print(f"Posterior probability of E given F: {posterior_prob:.4f}")