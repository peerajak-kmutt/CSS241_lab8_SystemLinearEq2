import numpy as np

def Jacobi(A,b,kmax):
    n, = b.shape
    x = np.zeros_like(b)

    #Your code here
    #end your code
    return x
            

def Problem2(A,b):
    return Jacobi(A,b,21)

