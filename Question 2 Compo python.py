#!/usr/bin/env python
# coding: utf-8
Gerer les exceptions
# In[16]:


class math():
    def __init__(self, x):
        self.x=x
        
    def verif_complex(self):
        x=self.x
        while(type(x)==complex):
            x = x.real
        if(type(x)==int):
            self.x=x
            
    def verif_type(self):
        x=self.x
        while (type(x)!=int):
            x=int(input("Entrez un nombre:"))
        if(type(x)==int):
            self.x=x
    
    def verif_negatif(self):
        x=self.x
        while (x<0):
            x=abs(x)
        if(x>0):
            self.x=x
    
    def verif_nbGrand(self):
        x=self.x
        while (len(str(x)) > 4):
            x=int(input("Entrez le bon nombre:"))
        if(len(str(x)) > 3):
            self.x=x
    
    #on considère comme nombre très petit 1
    def verif_nbPetit(self):
        x=self.x
        while (x<=1):
            x=int(input("Entrez le bon nombre:"))
        if(x>1):
            self.x=x
        
    def suite_fibo(self):
        fib=[]
        fib.append(0)
        fib.append(1)
        for i in range(2,self.x+1):
            result=fib[i-1]+fib[i-2]
            fib.append(result)
        return ("La suite de fibonnaci est :", fib)


# In[17]:


a=math(-123)
a.verif_complex()
a.verif_type()
a.verif_negatif()
a.verif_nbGrand()
a.verif_nbPetit()
a.suite_fibo()

