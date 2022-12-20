#!/usr/bin/env python
# coding: utf-8

# #Matplotlib
# Matplotlib is a library for the Python programming language that enables users to create visualisations that may be either static, animated, or
# interactive. Matplotlib enables users to do tasks that range from simple to complex. Develop stories in a format that is appropriate for publishing.
# Develop zoomable, pagable, and updatable graphs that may be interactively created.
# #Pandas
# """Pandas is an open source library that was primarily developed for the purpose of dealing with relational or 
# labelled data in a straightforward and user-friendly manner."""
# 
# #bar
# The height of the bars in a bar plot is proportional to the value that they represent, while the plot itself displays categorical data as rectangular bars. It is often used to make comparisons between the values of the many categories included in the data.

# In[15]:


import pandas as pd
"""Pandas is an open source library that was primarily developed for the purpose of dealing with relational or 
labelled data in a straightforward and user-friendly manner."""
from matplotlib import pyplot as plot  
"""Matplotlib is a library for the Python programming language that enables users to create visualisations that may be either static, animated, or
interactive. Matplotlib enables users to do tasks that range from simple to complex. Develop stories in a format that is appropriate for publishing.
Develop zoomable, pagable, and updatable graphs that may be interactively created."""


# In[ ]:


df=pd.read_csv("/content/drive/MyDrive/fuel price.csv") # loading dataset 


# In[20]:


df.head(10) # showing dataset 


# In[5]:


df=df.drop(['Unnamed: 0'],axis=1) # drop unname colums


# In[6]:


df.info()  # showing data informatiom 


# In[7]:


df.isnull().sum() # check null valuse


# In[8]:


df.nunique()


# # plotting line graph using matplotlib

# #Pump price in pence/litre (ULSP)
# # ULSP = Ultra low sulpur unleaded petrol

# In[9]:


df1=df.pivot_table(index=['Date'], values=['Pump price in pence/litre (ULSP)','Duty rate in pence/litre (ULSP)'])   
plot.figure(figsize = (20,8)) # define figure size 
plot.plot(df1.head(15)) 
plot.legend(['Duty rate in pence/litre (ULSP)','Pump price in pence/litre (ULSP)']) 
plot.xlabel('Year')
#  x axis define year 
plot.ylabel('Price ')
# y axis define price 
plot.title('Pump price in pence/litre (ULSP)') 
# define title name 
plot.show() # showing graph 


# # plotting line graph using matplotlib

# #Pump price in pence/litre (ULSD)
# #ULSD = Ultra low sulphur diesel
# 

# In[10]:


df2=df.pivot_table(index=['Date'], values=['Pump price in pence/litre (ULSD)','Duty rate in pence/litre (ULSD)'])  
# define figuresize 
plot.figure(figsize = (20,8)) 
plot.plot(df2.head(16)) 
plot.legend(['Duty rate in pence/litre (ULSD)','Pump price in pence/litre (ULSD)']) 
plot.xlabel('Year')
#  x axis define year 
plot.ylabel('Price ')
# y axis define price 
plot.title('Pump price in pence/litre (ULSD)') 
# define title name 
plot.show() 


# #comparison of Pump price in pence/litre (ULSD) and (ULSP)
# A bar plot is a kind of data visualisation that displays categorical information as a series of rectangular bars, with the height of each bar being proportional to the value it represents. This is often used in the process of contrasting the values of the many categories included in the data.

# In[11]:


df3=df.pivot_table(index=['Date'], values=['Pump price in pence/litre (ULSD)','Pump price in pence/litre (ULSP)'])   
# define figure size
plot.rcParams['figure.figsize']=(20,7) 
df3= df3.head(10)
df3.plot.bar()
plot.xlabel('Year')
# x axis define year 
plot.ylabel('Price ')
# y axis define price 
plot.title('comparison of Pump price in pence/litre (ULSD) and Pump price in pence/litre (ULSP)') 
# define title name 
plot.show() ;


# #Comparison of VAT percentage rate (ULSP) and (ULSD)

# In[12]:


df4=df.pivot_table(index=['Date'], values=['VAT percentage rate (ULSD)','VAT percentage rate (ULSP)'])   
# define figure size 
plot.rcParams['figure.figsize']=(20,7) 
df3= df4.head(10)
df3.plot.bar()
plot.xlabel('Year')
#  x axis define year 
plot.ylabel('VAT ')
# y axis define vat 
plot.title('Comparison of VAT percentage rate (ULSP) and  VAT percentage rate (ULSD)') 
# define title name 
plot.show() ;


# #Comparison of Pump price in pence/litre (ULSP) with Date

# In[13]:


# define figure size.
plot.rcParams['figure.figsize']=(20,7) 
# define font_size.
plot.rcParams.update({'font.size': 10}) 
df5= df.head(15)
df5.plot(kind="scatter", x='Date', y='Pump price in pence/litre (ULSP)', alpha=0.9) 
# x_label set here.
plot.xlabel("Date") 
# y_label set here.
plot.ylabel("Price") 
# title set here.
plot.title("Comparison of Pump price in pence/litre (ULSP) with date") 
plot.show() 


# #Comparison of Pump price in pence/litre (ULSD) with Date 

# In[14]:


# define figure size.
plot.rcParams['figure.figsize']=(20,7) 
# define font_size.
plot.rcParams.update({'font.size': 10}) 
df5= df.head(15)
df5.plot(kind="scatter", x='Date', y='Pump price in pence/litre (ULSD)', alpha=0.9) 
# x_label set here.
plot.xlabel("Date") 
# y_label set here.
plot.ylabel("Price") 
# title set here.
plot.title("Comparison of Pump price in pence/litre (ULSD) with Date  ") 
plot.show() 


# In[14]:




