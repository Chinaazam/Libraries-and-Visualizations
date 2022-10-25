#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib.pyplot as plt


# In[9]:


import numpy as np
x = np.linspace (0,5,11)
y = x ** 2


# In[3]:


x


# In[7]:


y


# In[21]:


plt.plot(x, y)


# In[54]:


plt.plot(x,y, "g")
plt.title("Yearly Sales Performance (For Illustration)")
plt.xlabel("Years")
plt.ylabel("Sales (thousands)")
plt.show()


# In[36]:


plt.plot(x,y, "rp")


# In[42]:


#creating multiplots on the same canvas
plt.subplot(1,2,1)
plt.plot(x,y, "r")
plt.subplot(1,2,2)
plt.plot(y,x, "b")


# In[20]:


#scatter plot
plt.scatter(x,y, marker = "+")


# In[ ]:





# In[87]:


#box plot
data = [np.random.normal(0, std, 100) for std in range(1,4)]
plt.boxplot(data, vert = True, notch = True, patch_artist = True);
#I found that patch_artist is used to tell the code that the boxes are oatches and not just paths. 
#Notch is used to the modify the boxes from its default rectangular format


# In[61]:


from random import sample
data = sample(range(1,1000), 100)
plt.hist(data, color = "red",ec = "black")
plt.xlabel("Salary (thousands)")
plt.ylabel("No of Employees")
plt.title("Histogram Practice Graph")

#ec = edge color

