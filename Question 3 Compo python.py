#!/usr/bin/env python
# coding: utf-8
Implémentation de la formule Pricer d’option
# In[19]:


import math
import scipy.stats


# In[32]:


#Déclaration des variables
S=int(input("Entrez le prix actuel de l'action: ")) #Prix actuel de l’action
X=int(input("Entrez le prix d'exercice: "))  #Prix d’exercice de l’option
r=float(input("Entrez le Taux d'intérêt: "))  #Taux d’intérêt sans risque
vol=float(input("Entrez la volatilité: "))  #volatilité implicite du prix de l’action, mesurée par un décimal
T=float(input("Entrez le temps: "))  #Temps restant avant l’expiration de l’option, en pourcentage d’une année

#calcul des variables d1 et d2
d1=(math.log(S/X)+(r+(vol**2)*T))/(vol*math.sqrt(T))
d2=d1-(vol*math.sqrt(T))

#le prix d’une option d’achat
c=S*scipy.stats.norm.cdf(d1) - X*math.exp(-r*T)*scipy.stats.norm.cdf(d2)

#le prix d’une option de vente
p=X*math.exp(-r*T)*scipy.stats.norm.cdf(-d2)-S*scipy.stats.norm.cdf(-d1)
    
print("Le prix de l'option d'achat est C=", round(c,2), "euros")
print("Le prix de l'option de vente est P=", round(p,2), "euros")


# In[27]:


scipy.stats.norm.cdf(-1.0011)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




