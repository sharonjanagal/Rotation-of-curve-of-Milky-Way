#!/usr/bin/env python
# coding: utf-8

# In[28]:


from galpy.potential import PowerSphericalPotentialwCutoff, MiyamotoNagaiPotential,  NFWPotential


# In[29]:


bp= PowerSphericalPotentialwCutoff(alpha=1.8,rc=1.9/8.,normalize=0.05)
mp= MiyamotoNagaiPotential(a=3./8.,b=0.28/8.,normalize=.6)
np= NFWPotential(a=16/8.,normalize=.35)
MWPotential2014= bp+mp+np


# In[30]:


MWPotential2014[2]*= 1.5


# In[31]:


from galpy.potential import KeplerPotential
from galpy.util import bovy_conversion
MWPotential2014wBH= MWPotential2014+KeplerPotential(amp=4*10**6./bovy_conversion.mass_in_msol(220.,8.))


# In[ ]:





# In[49]:



from galpy.potential import plotRotcurve
plotRotcurve(MWPotential2014wBH,Rrange=[0,4],grid=1001,yrange=[0.,1.2])


# In[ ]:




