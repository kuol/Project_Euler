# Reference: http://www.ams.org/samplings/feature-column/fcarc-kissing
import numpy as np
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
    tol = 10e-12
    xx = [c1.x, c2.x, c3.x]
    yy = [c1.y, c2.y, c3.y]
    #rr = [c1.r if c1.r!=1 else -c1.r, c2.r if c2.r!=1 else -c2.r, c3.r if c3.r!=1 else -c3.r]
    rr = [c1.r if np.abs(c1.r - 1) < tol else -c1.r, c2.r if np.abs(c2.r-1)<tol else -c2.r, c3.r if np.abs(c3.r-1)<tol else -c3.r]
    ## compute radius
    k = 1.0/np.array(rr)
    r = 1.0/(sum(k) + 2*np.sqrt(k[0]*k[1] + k[1]*k[2] + k[2]*k[0]))
    ## compute center
    rhs = (xx[1]**2 - xx[0]**2) + (yy[1]**2 - yy[0]**2) + (r + rr[0])**2 - (r + rr[1])**2
    s = -(float(xx[1]) - xx[0])/(yy[1] - yy[0])
    t = float(rhs)/(2*(yy[1] - yy[0]))
    
    a = (1 + s**2)
    b = 2*s*(t-yy[0]) - 2*xx[0]
    c = xx[0]**2 + (t - yy[0])**2 - (r + rr[0])**2
    
    if b**2 - 4*a*c > 0:
        x1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a) 
        x2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
        y1 = s*x1 + t
        y2 = s*x2 + t
    else:
        print "OOps"
        c1.show()
        c2.show()
        c3.show()
        print "b^2 - 4ac = %0.8f" %(b**2 - 4*a*c)
        return 1
    
    # Be careful here! You can't test if "==", since they are float numbers!
    if (x1 - xx[2])**2 + (y1 - yy[2])**2 - (r + rr[2])**2 < 10e-12:
        x,y = x1,y1
    else:
        x,y = x2,y2
    
    return Circle((x,y,r))


def reproduce(c1, c2, c3, all_generations, level=0):
    if level == 0:
        return 0
    else:
        child = get_circle(c1,c2,c3)
        all_generations.append((child,level))
        reproduce(c1,c2,child,all_generations,level-1)
        reproduce(c1,c3,child,all_generations,level-1)
        reproduce(c2,c3,child,all_generations,level-1)

c1 = Circle((0,0,1))
c2 = Circle((0,4-2*np.sqrt(3), 2*np.sqrt(3)-3))
c3 = Circle((3-2*np.sqrt(3), np.sqrt(3)-2, 2*np.sqrt(3)-3))
c4 = Circle((-c3.x, c3.y, c3.r))
c5 = get_circle(c2,c3,c4)
#branch_side = [(c1,-1), (c2,0), (c3,0), (c4,0)]
#branch_center = [(c1,-1), (c2,0), (c3,0), (c4,0)]
branch_side = []
branch_center = []
area = 1 - (c2.r**2 + c3.r**2 + c4.r**2 + c5.r**2) # fracation of blank area

#level = 10
# This gives warning for taking np.sqrt()
reproduce(c1,c2,c3,branch_side,10)
#reproduce(c2,c3,c5,branch_center,9)


r2s = 0 
for i in xrange(len(branch_side)):
    r2s = r2s + branch_side[i][0].r ** 2

r2c = 0
for i in xrange(len(branch_center)):
    r2c = r2c + branch_center[i][0].r ** 2


blank_area = area - (r2s + r2c)*3
print "The fraction of blank area is %0.8f" %blank_area


