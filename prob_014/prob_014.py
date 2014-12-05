"""
Several observations:
    1. There's no established math formula to compute the max_collatz, don't even try
    2. Once Collatz number of an odd number: k is computed, it'll be easy to get Collatz
       number of:
       2k, 2^2k, 2^3k, ... 2^log2(N/k)*k
    3. The biggest improvement of efficiency lies in: reusing Collatz that has already 
       been computed -- here, I use numbers to store it.
    4. The final tricky part: due to the "3k+1", it's hard to predict the range of numbers
       whose Collatz is needed to get Collatz of numbers < N (3*N+1 is still not enough).
       Thus I choose dictionary as numbers's data structure
    5. Results: Run time < 3s
"""
import numpy as np

def main():
    max_collatz(1000000)

def max_collatz(N):
    numbers = {}
    m = 0
    for i in xrange(1,N,2):
        t = collatz(i,numbers)
        temp = t + np.log2(N/i)
        if m < temp:
            m = temp
            candidate = i*2**(np.log2(N/i)) 
    print m, candidate

def collatz(i, numbers):
    N = len(numbers)
    if i in numbers:
        return numbers[i]
    elif i == 1:
        numbers[1] = 1
        return 1
    else:
        if i%2: #odd
            if 3*i+1 not in numbers:
                numbers[i] = 1 + collatz(3*i+1, numbers)
                return 1 + collatz(3*i+1, numbers)
            else:
                numbers[i] = 1 + numbers[3*i+1]
                return numbers[i]
        else: # even
            if i/2 not in numbers:
                numbers[i] = 1 + collatz(i/2, numbers)
                return 1 + collatz(i/2, numbers)
            else:
                numbers[i] = 1+ numbers[i/2]
                return numbers[i]

# ======================================================
#                     Brute Force 
# ======================================================
def max_collatz1(N):
    m = 0
    for i in xrange(1,N):
        temp = collatz1(i)
        if m < temp:
            m = temp
            candidate = i
    print m, candidate



def collatz1(i):
    if i == 1:
        return 1
    else:
        if i%2: #odd
            return 1 + collatz1(3*i+1)
        else: # even
            return 1 + collatz1(i/2)

if __name__ == '__main__':
    main()
