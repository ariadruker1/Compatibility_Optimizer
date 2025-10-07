"""
Aria Druker 
Fall 2025
"""

# Multi-start random hill-climb approach
import os, random
from cleaning_input_compatibility import input_compatibility
from random_matching import random_matching

def main():
    seed = random.seed()

    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, "compatibilityInput.xlsx")

    # get compatibility matrix and student ID's
    C, ids = input_compatibility(path)
    n = len(ids) # amount of students
    m = n // 2 # amount of pairings

    R = 5000 # restarts
    N = 1000 # swap attempts per restart

    best_score = -1
    best_pairs = None

    for trial in range(R):
        pairs = random_matching(n)
        current = sum(C[i][j] for (i, j) in pairs)

        for _ in range(N):
            # pick two distinct pairs at random
            a = random.randrange(m)
            b = random.randrange(m)
            # if same pair is randomly picked there cannot be swaps
            if a == b:
                continue

            (i, j) = pairs[a]
            (k, l) = pairs[b]

            base = C[i][j] + C[k][l]
            gain1 = C[i][k] + C[j][l] - base   # option 1: (i,k) & (j,l)
            gain2 = C[i][l] + C[j][k] - base   # option 2: (i,l) & (j,k)

            # keep only if improves and use greatest gain from combination
            if gain1 >= gain2 and gain1 > 0:
                pairs[a] = (i, k)
                pairs[b] = (j, l)
                current += gain1
            elif gain2 > 0:
                pairs[a] = (i, l)
                pairs[b] = (j, k)
                current += gain2
            # else: no change because doesn't improve score

        if current > best_score:
            best_score = current
            best_pairs = pairs[:]

        if trial % 100 == 0:
            print(f'Best Score After {trial} Restarts: {best_score}')
    
    # print pairings
    best_pairs_ids = [(ids[i], ids[j]) for (i, j) in best_pairs]
    print(f"Best total compatibility: {best_score} is {round((best_score/4949)*100, 1)}% accurate towards the optimal solution")
    print(f"Ideal Pairings:{best_pairs_ids}")

    
if __name__ == '__main__':
    main()