#!/usr/bin/env python
# coding: utf-8

# # Assignment 7, Q- 5
# # Sneha, UIN:733000826

# In[36]:


import numpy as np
from scipy.optimize import linprog


# In[42]:


R = int(input("Enter the number of rows for Matrix A:"))
C = int(input("Enter the number of columns for Matrix A:"))
print("Enter the entries for Matrix A of size {} in a single line (separated by space): ".format(R*C))
  
# User input of entries in a single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrixA = np.array(entries).reshape(R, C)
print(matrixA)

Cb = int(input("Enter the number of columns for Matrix B:"))
print("Enter the entries for Matrix b of size {} in a single line (separated by space): ".format(R*Cb))

# User input of entries in a single line separated by space
entries = list(map(int, input().split()))
  
# For printing the matrix
matrixB = np.array(entries).reshape(R, Cb)
print(matrixB)


# In[43]:


c = np.zeros(C) 
c[0] = 1 # Maximum first and rest are zero, if not, function returns infinity


# Rest of the x entries other than first coordinate must be zero inorder to have an finite infimum  
# Else the maximum value of first coordinate in polytope is infinity  
# So, we need to make rest of the coordinates zero to have an finite infimum  

# In[44]:


res = linprog(-c, A_ub = matrixA, b_ub = matrixB)


# In[45]:


print("Maximum value of given first coordinate in polytope for given matrices A, b is:",res['x'][0])


# In[46]:


import polytope as pc

p = pc.Polytope(matrixA, matrixB)
  
print(p)


# In[47]:


# check for the region within or on polytope[Ax<=b]
# verification with Polytope function
res['x'] in p

