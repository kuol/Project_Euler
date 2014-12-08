from collections import deque

fibonacci = deque([1,1])
x = 2
count = 3
while x < 10**999:
    fibonacci.append(x)
    fibonacci.popleft()
    x = sum(fibonacci)
    count += 1
print count
