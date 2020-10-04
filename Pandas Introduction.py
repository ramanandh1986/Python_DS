#!/usr/bin/env python
# coding: utf-8

# #PANDA INTRODUCTION

# In[1]:


get_ipython().system('pip install pandas')


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")


# In[7]:


df.head()


# In[11]:


df.head(10)


# In[12]:


df.head(20)


# In[13]:


df.head(50)


# In[14]:


df.dtypes


# In[15]:


df.columns


# In[16]:


df.axes


# In[17]:


df.ndim


# In[18]:


df.size


# In[19]:


df.shape


# In[20]:


df.values


# In[21]:


df.size


# In[22]:


df.columns


# In[25]:


len(df.columns)


# In[24]:





# In[26]:


df.columns


# In[28]:


df.dtypes


# In[30]:


len(df.row)


# In[31]:


df.count


# In[36]:


total_rows = df['rank'].count


# In[38]:


total_rows


# In[42]:


dir(df)


# In[43]:


df.describe()


# In[44]:


df.max()


# In[45]:


df.min()


# In[50]:


df.sample(10, random_state=5)


# In[51]:


df.describe()


# In[52]:


df.std()


# In[55]:


df1 = df.head(50).mean()


# In[56]:


df1


# In[57]:


df.rank


# In[58]:


df['rank']


# In[59]:


df.salary


# In[60]:


df['salary']


# In[61]:


df[['salary']]


# In[62]:


df2 = df["phd"]


# In[68]:


df2.describe()


# In[71]:


df.phd.count()


# In[66]:


rows


# In[72]:


df.phd.mean()


# In[78]:


df[(df['salary']>120000) & (df['sex']== "Female")]


# In[79]:


df.iloc[1:4,0:2]


# In[80]:


df.iloc[0:10,0:4]


# In[94]:


df.groupby('rank')[['salary']].mean()


# In[86]:


df.groupby('rank')[['salary','phd']].mean()


# In[88]:


df[df['salary']>100000


# In[89]:


import matplotlib.pyplot as plt


# In[90]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[91]:


x = [-3,5,7 ]


# In[92]:


y = [10, 2, 5]


# In[93]:


import seaborn as sns


# In[ ]:




