#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import warnings
warnings.filterwarnings('ignore')


# In[3]:


df = pd.read_csv('Retail(Dataset).csv')  
df.head()  


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


df.describe()


# In[7]:


df.isnull().sum()


# In[8]:


df.info()


# In[9]:


df.columns


# In[10]:


df.duplicated().sum()


# In[11]:


df.nunique()


# In[12]:


df['Postal Code'] = df['Postal Code'].astype('object')


# In[13]:


df.drop_duplicates(subset=None,keep='first',inplace=True)
df.duplicated().sum()


# In[ ]:


corr = df.corr()
sns.heatmap(corr,annot=True,cmap='Reds')


# In[ ]:


df = df.drop(['Region'],axis = 1)


# In[ ]:


sns.pairplot(df, hue = 'Ship Mode')


# In[15]:


df['Ship Mode'].value_counts()


# In[16]:


sns.countplot(x=df['Ship Mode'])


# In[17]:


df['Segment'].value_counts() 


# In[18]:


sns.pairplot(df,hue = 'Segment')


# In[19]:


sns.countplot(x = 'Segment',data = df, palette = 'rainbow')


# In[20]:


df['Category'].value_counts()


# In[21]:


sns.countplot(x='Category',data=df,palette='tab10')


# In[22]:


sns.pairplot(df,hue='Category')


# In[23]:


df['Sub-Category'].value_counts()


# In[24]:


plt.figure(figsize=(15,12))
df['Sub-Category'].value_counts().plot.pie(autopct='dark')
plt.show()


# In[25]:


df['State'].value_counts()


# In[26]:


plt.figure(figsize=(15,12))
sns.countplot(x='State',data=df,palette='rocket_r',order=df['State'].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# In[27]:


df.hist(figsize=(10,10),bins=50)
plt.show()


# In[28]:


plt.figure(figsize=(10,8))
df['Region'].value_counts().plot.pie(autopct = '%1.1f%%')
plt.show()


# In[29]:


fig,ax=plt.subplots(figsize=(20,8))
ax.scatter(df['Sales'],df['Profit'])
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
plt.show()


# In[30]:


sns.lineplot(x='Discount',y='Profit',label='Profit',data=df)
plt.legend()
plt.show()


# In[31]:


sns.lineplot(x='Quantity',y='Profit',label='Profit',data=df)
plt.legend()
plt.show()


# In[32]:


df.groupby('Segment')[['Profit','Sales']].sum().plot.bar(color=['pink','blue'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[33]:


plt.figure(figsize=(12,8))
plt.title('Segment wise Sales in each Region')
sns.barplot(x='Region',y='Sales',data=df,hue='Segment',order=df['Region'].value_counts().index,palette='rocket')
plt.xlabel('Region',fontsize=15)
plt.show()


# In[34]:


df.groupby('Region')[['Profit','Sales']].sum().plot.bar(color=['blue','red'],figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[35]:


ps = df.groupby('State')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['blue','orange'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('States')
plt.ylabel('Profit/loss & Sales')
plt.show()


# In[36]:


t_states = df['State'].value_counts().nlargest(10)
t_states


# In[37]:


df.groupby('Category')[['Profit','Sales']].sum().plot.bar(color=['yellow','purple'],alpha=0.9,figsize=(8,5))
plt.ylabel('Profit/Loss and sales')
plt.show()


# In[38]:


ps = df.groupby('Sub-Category')[['Sales','Profit']].sum().sort_values(by='Sales',ascending=False)
ps[:].plot.bar(color=['red','lightblue'],figsize=(15,8))
plt.title('Profit/loss & Sales across states')
plt.xlabel('Sub-Category')
plt.ylabel('Profit/loss & Sales')
plt.show()


# In[ ]:


thank you


# In[ ]:




