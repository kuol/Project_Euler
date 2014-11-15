def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)

i = 2
count = 0 
while i < 33:
    count += fib(i)
    i += 3
print count
