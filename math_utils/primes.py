import numpy as np


def isprime(n):
    if n <= 1:
        return False
    for r in range(2, int(np.sqrt(n))+1):
        if n % r == 0:
            return False
    return True
