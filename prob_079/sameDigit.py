with open('p079_keylog.txt') as f:
    data = f.readlines()
data = [int(x.strip()) for x in data]

hdo = [(x/100, x/10%10, x%10) for x in data]

# Ajacency matrix of size: 8x8
A = [[0]*10 for i in range(10)]
for x in hdo:
    i,j,k = x
    if A[i][j] == -1 or A[i][j] == 2:
        A[i][j], A[j][i] = 2,2
    else:
        A[i][j], A[j][i] = 1,-1

    if A[i][k] == -1 or A[i][k] == 2:
        A[i][k], A[k][i] = 2,2
    else:
        A[i][k], A[k][i] = 1,-1

    if A[j][k] == -1 or A[j][k] == 2:
        A[j][k], A[k][j] = 2,2
    else:
        A[j][k], A[k][j] = 1,-1

for x in A:
    print x
#for x in hdo:
#    if x[0]==x[1] or x[0]==x[2] or x[1]==x[2]:
#        print ("Same digits for %d!")
#
#a = [0]*10
#for x in hdo:
#    for k in x:
#        a[k] += 1
#print(a)

