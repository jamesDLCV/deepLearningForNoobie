#!/usr/bin/env python
# coding: utf-8

# # f(x0, x1) = x0**2 + x1**2

# In[42]:


import numpy as np


# In[43]:


def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)


# In[51]:


def function_tmp1(x0):
    return x0*x0 + 4.0**2.0


# In[52]:


# x0 = 3, x1 = 4, x0 partial differenciation


# In[53]:


numerical_diff(function_tmp1, 3.0)


# In[54]:


# x0 = 3, x1 = 4, x1 partial differenciation


# In[55]:


def function_tmp2(x1):
    return 3.0**2.0 + x1*x1


# In[56]:


numerical_diff(function_tmp2, 4.0)


# In[44]:





# In[ ]:





# In[ ]:




