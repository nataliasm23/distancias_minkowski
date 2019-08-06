
# coding: utf-8

# In[1]:


from scipy.spatial.distance import pdist


# In[2]:


P1 = [-3, 0, 6]
P2 = [-1,-1,-1]
P3 = [ 3, 4, 3]
P4 = [10, 0, 0]
P5 = [ 0, 9,10]


# In[3]:


X = [P1,P2,P3,P4,P5]


# In[4]:


Y = pdist(X, 'minkowski', p=1)
print(Y)


# In[5]:


Y = pdist(X, 'minkowski', p=3)
print(Y)


# In[6]:


Y = pdist(X, 'minkowski', p=3)
print(Y)

