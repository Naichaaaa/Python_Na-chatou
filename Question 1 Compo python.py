#!/usr/bin/env python
# coding: utf-8
1.a) Implémenter une fonction polynomiale
# In[1]:


def polynome(x):
    f=(x**3)-1.5*(x**2)-6*x+5
    return f


# In[5]:


polynome(5)

1.b) Implémenter une fonction factorielle
# In[40]:


def factorielle(x):
    result=1
    for i in range(1, (x+1)):
        if x==1:
            result=1
        else:
            result=result*i
    return result


# In[43]:


factorielle(5)

1.c) Implémenter la suite de Fibonnaci
# In[56]:


nombre=int(input("Entrez un nombre : "))
suite_fib=[]
suite_fib.append(0)
suite_fib.append(1)
for i in range(2,nombre+1):
    result=suite_fib[i-1]+suite_fib[i-2]
    suite_fib.append(result)
print("La suite de fibonnaci est :", suite_fib)

