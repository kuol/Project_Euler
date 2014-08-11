import numpy as np
import matplotlib.pyplot as plt

def main():
    c1 = Circle((0,0,1))
    c2 = Circle((0,4-2*np.sqrt(3), 2*np.sqrt(3)-3))
    c3 = Circle((3-2*np.sqrt(3), np.sqrt(3)-2, 2*np.sqrt(3)-3))
    son = get_circle(c1,c2,c3)


class Circle(object):
    def __init__(self,l= [0]*3):
        self.x = l[0]
        self.y = l[1]
        self.r = l[2]
    def get_radius(self):
        return self.r
    def get_center(self):
        return self.x, self.y
    def show(self):
        print "(x,y) = (%f, %f)\nr = %f" %(self.x, self.y, self.r)
    def plot(self):
        plt.axes()
        circle = plt.Circle((self.x, self.y), radius=self.r, fc='y')
        plt.gca().add_patch(circle)
        plt.axis('scaled')
        plt.show()

def get_circle(c1,c2,c3):
    x = [c1.x, c2.x, c3.x]
    y = [c1.y, c2.y, c3.y]
    r = [c1.r if c1.r!=1 else -c1.r, 
         c2.r if c2.r!=1 else -c2.r, 
         c3.r if c3.r!=1 else -c3.r,]
    
    A = np.empty((3,3))
    b = np.empty(3)
    soln = np.empty(3)
    for i in xrange(3):
        A[i,0] = 2*(x[(i+1)%3] - x[i])
        A[i,1] = 2*(y[(i+1)%3] - y[i])
        A[i,2] = 2*(r[(i+1)%3] - r[i])
        b[i] = (x[(i+1)%3]**2 - x[i]**2) + (y[(i+1)%3]**2 - y[i]**2) - (r[(i+1)%3]**2 - r[i]**2)
    
    cramer_solver(A,b,soln)
    return Circle(soln)
    
def cramer_solver(A,b,x):
    denom = det(A)
    numer = np.empty(3)
    if denom == 0:
        print "Equation doens't have unique solution, abort"
        return 1
    elif A.shape[0] != np.size(b) or A.shape[0] != np.size(x):
        print "Flawed input size, abort"
        return 1
    else:
        for i in np.size(b):
            temp = A.copy()
            temp[:,i] = b
            numer[i] = det(temp)
        x = numer/float(denom)

def det(A):
    if np.size(A) == 1:
        return A
    elif A.shape[0] != A.shape[1]:
        return 0
    else:
        result = 0
        for i in xrange(A.shape[0]):
            temp = np.delete(A,0,0) # delete Row 0
            temp = np.delete(A,i,1) # delete Column i
            result = result + (-1)**(i&1)*A[0,i]*det(temp)
        return result
       

if __name__ == '__main__ ':
    main()
