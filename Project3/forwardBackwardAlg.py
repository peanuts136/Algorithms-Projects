def forwardBackward(observations, states,startProb, transProb,emitProb,):
    T= len(observations)
    N = len(states)
    #computes the marginal probabilities of being in each hidden state at each step 

    ##Forward pass: calculates the total probabilitity of reaching a specific state at time t
    #given observations from beginning up to T
    #formula(init) = forward[s][0] = startProb[s] * emit_prob[s][observations[0]]
    #formula = probability of being in state s at time t and observating at that time t
    #Initialization
    forward = [[0 for _ in range(T)] for _ in range(N)]

    for s in range(N):
        forward[s][0] = startProb[s] + emitProb[s][observations[0]]
    #Recurrence
    for t in range(1,T):
        for s in range(N):
            total = 0
            for r in range(N):
                total += forward[r][t-1] * transProb[r][s] * emitProb[s][observations[t]]
            forward[s][t] = total
    
    #Backwards Pass:calculates the probability of observing the sequence from t+1 to t-1, given state at time t is s
    #Initialzation:
    backward = [[0 for _ in range(T)] for _ in range(N)]
    for s in range(N):
        backward[s][T-1] =1 #always 1 because no observations follow T-1
    #recurrence
    for t in range(T-2,-1,-1): #alr accounts for t-1
        for r in range(N):
            total = 0 
            for s in range(N):
                total += backward[s][t+1] * transProb[r][s] * emitProb[s][observations[t+1]]
            backward[r][t] = total
    #The forward and backward probabilities are combined and normalized to compute the marginal prob
    marginals = [[0 for _ in range(T)] for _ in range(N)]
    for t in range(T):
        norm_factor = 0
        for s in range(N):
            norm_factor += forward[s][t] * backward[s][t] 
        for s in range(N):
            marginals[s][t] = (forward[s][t] * backward[s][t]) / norm_factor
    return marginals


# Example usage
states = ["Fair", "Loaded"]
observations = [int(c) - 1 for c in "23443224462431261412355552456612616666663546661636616563556412441436124342246236511262136656662263243"]  # Adjust to zero-based indexing

# Transition, emission, and initial probabilities
start_prob = [0.5, 0.5]
trans_prob = [[0.95, 0.05], [0.1, 0.9]]
emit_prob = [
    [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],  # Fair die
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.5]   # Loaded die
]

# Run Forward-Backward Algorithm
marginals = forwardBackward(observations, states, start_prob, trans_prob, emit_prob)
print("Marginal Probabilities:")
for t in range(len(observations)):
    print(f"Time {t}: Fair = {marginals[0][t]:.4f}, Loaded = {marginals[1][t]:.4f}")



