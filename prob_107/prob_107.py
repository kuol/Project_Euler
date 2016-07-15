# Prim's algorithm?
import numpy as np

data = np.genfromtxt('p107_network.txt', delimiter = ',')
original_cost = np.nansum(data) / 2
where_nan = np.isnan(data)
data[where_nan] = np.inf
n = data.shape[1]

V = [0]
E = []

while len(V) < n:
    # Get matrix index of the minimum edge that connects to elements in V.
    ind = data[V].argmin()
    i, j = ind / n, ind % n
    # Append the new vertex and edge
    V.append(j)
    E.append(data[V[i],j])
    # Discard edge between vertices in the tree. 
    data[V,j] = np.inf
    data[j,V] = np.inf

#print(sorted(V))
print(E)
print("="*100)
print(V)
print("="*100)
#print("Original cost is: %f" % original_cost)
#print("Current cost is: %f" % sum(E))
print("Total saved cost is: %f" % (original_cost - sum(E)))

