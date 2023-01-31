#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# A contains columns of independent vectors which span the space
A = np.matrix([[1,-1,1,1],[2,1,1,1],[3,1,1,1]]).T

# Some rearrangements for ease of coding
u = A.T
v = np.zeros(u.shape)

for i in range(u.shape[0]):
    if i == 0 :
        v[i] = u[i]
        v[i] = u[i] / np.linalg.norm(u[i])
    else :
        v[i] = u[i]
        for j in range(i):
            v[i] = v[i] - (np.linalg.norm(np.dot(u[i],v[j].T))/np.linalg.norm(np.dot(v[j],v[j].T))) * v[j]
        v[i] = v[i] / np.linalg.norm(v[i])


# In[3]:


print(" A = \n", A)
      
Q = v.T
print("\n Q = \n",Q)

R = np.matmul(Q.T, A)
print("\n R = \n",np.round(R,3))

