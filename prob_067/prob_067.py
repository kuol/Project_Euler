N = 100
a = [[0 for x in xrange(N)] for x in xrange(N)]

counter = 0
with open('triangle.txt') as f:
    for line in f:
        data = line.split()
        a[counter][:] = [int(x) for x in data]
        counter = counter + 1

for i in xrange(N-1,0,-1):
    for j in xrange(i):
        a[i-1][j] = a[i-1][j] + a[i][j] if a[i][j] > a[i][j+1] else a[i-1][j] + a[i][j+1]

print "The Maximum sum is: %d" %a[0][0]
