import random

def random_matching(n):
    nodes = list(range(n))
    random.shuffle(nodes)
    pairs = []
    for k in range(0, n, 2):
        i, j = nodes[k], nodes[k+1]
        pairs.append((i, j)) 
    return pairs