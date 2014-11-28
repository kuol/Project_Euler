import numpy as np

def main():
    a = np.genfromtxt('number.txt', delimiter=' ', dtype='int')
    print up_down(a)
    print left_right(a)
    print diagonal1(a)
    print diagonal2(a)


def up_down(a):
    m,n = a.shape
    s = np.zeros((m-3,n), dtype='int')
    for i in xrange(m-3):
        for j in xrange(n):
            s[i,j] = a[i,j]*a[i+1,j]*a[i+2,j]*a[i+3,j]
    return s.max()

def left_right(a):
    m,n = a.shape
    s = np.zeros((m,n-3), dtype='int')
    for i in xrange(m):
        for j in xrange(n-3):
            s[i,j] = a[i,j]*a[i,j+1]*a[i,j+2]*a[i,j+3]
    return s.max()

def diagonal1(a): #top_left -> bottom_right
    m,n = a.shape
    s = np.zeros((m-3, n-3), dtype='int')
    for i in xrange(m-3):
        for j in xrange(n-3):
            s[i,j] = a[i,j] * a[i+1,j+1] * a[i+2,j+2] * a[i+3,j+3]
    return s.max()

def diagonal2(a): #top_right -> bottom_left
    m,n = a.shape
    s = np.zeros((m-3, n-3), dtype='int')
    for i in xrange(m-3):
        for j in xrange(n-3):
            s[i,j] = a[i,j+3] * a[i+1,j+2] * a[i+2,j+1] * a[i+3,j]
    return s.max()


if __name__ == '__main__':
    main()
