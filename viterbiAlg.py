import math
def viterbi_algorithm(observations, states, start_prob, trans_prob, emit_prob):
    T = len(observations)
    N = len(states)

    # Initialize DP table and back-pointer table
    prob = [[0 for _ in range(T)] for _ in range(N)] #T x S
    prev = [[None for _ in range(T)] for _ in range(N)]

    # Initialization step
    for s in range(N):
        prob[s][0] = start_prob[s] * emit_prob[s][observations[0]]

    # Recursion step
    for t in range(1, T): #T0 dealt with already
        for s in range(N):
            for r in range(N):
                new_prob = prob[r][t-1] * trans_prob[r][s] * emit_prob[s][observations[t]]
                if new_prob > prob[s][t]:
                    prob[s][t] = new_prob
                    prev[s][t] = r
             
    # Termination step and path traceback
    path = [0] * T
    path[T - 1] = max(range(N), key=lambda s: prob[s][T - 1])
    for t in range(T - 2, -1, -1):
        path[t] = prev[path[t + 1]][t+1]


    return path
    

states = ["Fair", "Loaded"]
observations = [int(c) - 1 for c in "23443224462431261412355552456612616666663546661636616563556412441436124342246236511262136656662263243"]  # Adjust to zero-based indexing
# Transition, emission, and initial probabilities
start_prob = [0.5, 0.5]
trans_prob = [[0.95, 0.05], [0.1,0.90]] #to fair, to loaded
emit_prob = [
    [1/6, 1/6, 1/6, 1/6, 1/6, 1/6],  # Fair die
    [0.1, 0.1, 0.1, 0.1, 0.1, 0.5],   # Loaded die
]

viterbiPath = viterbi_algorithm(observations, states, start_prob, trans_prob, emit_prob)
viterbiPathAsCharacters=""
for i in viterbiPath:
    if i == 0:
        viterbiPathAsCharacters += "F"
    else:
        viterbiPathAsCharacters+= "L"
print(viterbiPathAsCharacters)