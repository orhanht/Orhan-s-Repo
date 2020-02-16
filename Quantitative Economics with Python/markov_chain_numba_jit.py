import numpy as np
import quantecon as qe
from numba import jit


"""
I want to compare the speeds of pure Python and numba.jit in the case of a simple finite state markov chain model.
"""
# 0 and 1 represents low and high states, respectively.
p, q = 0.9, 0.8     # Probability of staying in the same state for low and high states, respectively.


def fin_state_markov_chain(n):
    x = np.empty(n, dtype=np.int_)
    x[0] = 1
    probs = np.random.uniform(0, 1, size=n)
    for t in range(1, n):
        if x[t - 1] == 1:
            x[t] = probs[t] < q
        else:
            x[t] = probs[t] > p
    return x


length = 1_000_000
# x_array1 = fin_state_markov_chain(length)
# print(np.mean(x_array1 == 0))                    # fraction of time x_array is in state of 0

qe.tic()
fin_state_markov_chain(length)
qe.toc()

fin_state_markov_chain_numba = jit(fin_state_markov_chain)
# x_array2 = fin_state_markov_chain_numba(length)
# print(np.mean(x_array2 == 0))

qe.tic()
fin_state_markov_chain_numba(length)
qe.toc()
