a = []
with open('numbers.txt') as f:
    for line in f:
        a.append(line)
a = [x.strip().split(' ') for x in a]

N = len(a)
for i in xrange(N):
    a[i] = [int(x) for x in a[i]]

for i in xrange(1,N):
    for j in xrange(i+1):
        if j==0:
            a[i][j] += a[i-1][j]
        elif j==i:
            a[i][j] += a[i-1][j-1]
        else:
            a[i][j] = max(a[i-1][j-1], a[i-1][j]) + a[i][j]

print max(a[N-1])



