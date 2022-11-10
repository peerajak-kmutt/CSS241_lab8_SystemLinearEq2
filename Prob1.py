import numpy as np
def LUdecomposition(A):
    m,n = A.shape
    U = A.copy()
    L = np.zeros_like(U)
    np.fill_diagonal(L, 1)

    #Your code here
    #end Your code
    
    return L,U

# Calculae Lz=b
def Lsubstitution(L,b):
    m,n = L.shape

    z = np.zeros(n,dtype=np.float64)
    #Your Code Here
    #End Your code
    return z

# Calculate Ux = z
def GaussianBacksubstitution(A,b):
    m,n = A.shape
    bn, = b.shape
    assert n==m==bn
    x = np.zeros(n,dtype=np.float64)
    
    #Your Code Here
    #End Your code
    
    return x

def Problem1(A,b): 
    #Your code here.
    #1. Calculate A=LU. Given A is known, find L,U
    #2. Calculate Lz=b  Given L from 1., and b from the problem, find z
    #3. Calculate Ux=z  Given U from 1., and z from 2., find x
    return x
