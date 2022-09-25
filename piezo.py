#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[9]:


json_open = open('piezo.json', 'r')
json_list = json.load(json_open)


# In[11]:


print('json_list:{}'.format(type(json_list)))


# In[27]:


get_data = json_list[0]['eij_max']


# In[28]:


print(get_data)


# In[36]:


eij = []
for i in range(len(json_list)):
    get_eij = json_list[i]['eij_max']
    eij.append(get_eij)


# In[37]:


print(eij)


# In[38]:


len(eij)


# In[39]:


get_point_group = json_list[0]['meta']['point_group']


# In[40]:


print(get_point_group)


# In[44]:


point = []
for i in range(len(json_list)):
    get_point_group = json_list[i]['meta']['point_group']
    point.append(get_point_group)


# In[45]:


print(point)


# In[59]:


point_index = []


# In[58]:


print(point[23])


# In[60]:


for i in range(len(json_list)):
    if point[i] == "23":
            point_index.append(1)
    elif point[i] == "-43m":
            point_index.append(2)
    elif point[i] == "-42m":
            point_index.append(3)
    elif point[i] == "-4":
            point_index.append(4)
    elif point[i] == "4mm":
            point_index.append(5)
    elif point[i] == "4":
            point_index.append(6)
    elif point[i] == "-6m2":
            point_index.append(7)
    elif point[i] == "-6":
            point_index.append(8)
    elif point[i] == "6mm":
            point_index.append(9)
    elif point[i] == "6":
            point_index.append(10)
    elif point[i] == "3m":
            point_index.append(11)
    elif point[i] == "32":
            point_index.append(12)
    elif point[i] == "3":
            point_index.append(13)
    elif point[i] == "mm2":
            point_index.append(14)
    elif point[i] == "222":
            point_index.append(15)
    elif point[i] == "m":
            point_index.append(16)
    elif point[i] == "2":
            point_index.append(17)
    elif point[i] == "1":
            point_index.append(18)
    else:
            print("err")


# In[61]:


print(point_index)


# In[68]:


import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
plt.scatter(point_index,eij)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], ["23", "-43m", "-42m", "-4", "4mm", "4", "-6m2", "-6", "6mm", "6" ,"3m" ,"32" ,"3" ,"mm2", "222", "m", "2", "1"])


# In[69]:


import numpy as np

point_pole = []
for i in range(len(json_list)):
    if point[i] == "23":
            point_pole.append(np.pi / 18)
    elif point[i] == "-43m":
            point_pole.append(np.pi * 3 / 18)
    elif point[i] == "-42m":
            point_pole.append(np.pi * 5 / 18)
    elif point[i] == "-4":
            point_pole.append(np.pi * 7 / 18)
    elif point[i] == "4mm":
            point_pole.append(np.pi * 9 / 18)
    elif point[i] == "4":
            point_pole.append(np.pi * 11 / 18)
    elif point[i] == "-6m2":
            point_pole.append(np.pi * 13 / 18)
    elif point[i] == "-6":
            point_pole.append(np.pi * 15 / 18)
    elif point[i] == "6mm":
            point_pole.append(np.pi * 17 / 18)
    elif point[i] == "6":
            point_pole.append(np.pi * 19 / 18)
    elif point[i] == "3m":
            point_pole.append(np.pi * 21 / 18)
    elif point[i] == "32":
            point_pole.append(np.pi * 23 / 18)
    elif point[i] == "3":
            point_pole.append(np.pi * 25 / 18)
    elif point[i] == "mm2":
            point_pole.append(np.pi * 27 / 18)
    elif point[i] == "222":
            point_pole.append(np.pi * 29 / 18)
    elif point[i] == "m":
            point_pole.append(np.pi * 31 / 18)
    elif point[i] == "2":
            point_pole.append(np.pi * 33 / 18)
    elif point[i] == "1":
            point_pole.append(np.pi * 35 / 18)
    else:
            print("err")


# In[80]:


fig = plt.figure(figsize=(8,8))
point_scatter = fig.add_subplot(111, projection='polar')
point_scatter.scatter(point_pole, eij)
point_scatter.set_rmin(0)
point_scatter.set_rmax(50)
point_scatter.set_xticks(np.linspace(np.pi/18, np.pi*35/18, 18)[0:])
point_scatter.set_xticklabels(["23", "-43m", "-42m", "-4", "4mm", "4", "-6m2", "-6", "6mm", "6" ,"3m" ,"32" ,"3" ,"mm2", "222", "m", "2", "1"])


# In[81]:


fig = plt.figure(figsize=(8,8))
point_scatter = fig.add_subplot(111, projection='polar')
point_scatter.scatter(point_pole, np.log2(eij))
point_scatter.set_rmin(-10)
point_scatter.set_rmax(10)
point_scatter.set_xticks(np.linspace(np.pi/18, np.pi*35/18, 18)[0:])
point_scatter.set_xticklabels(["23", "-43m", "-42m", "-4", "4mm", "4", "-6m2", "-6", "6mm", "6" ,"3m" ,"32" ,"3" ,"mm2", "222", "m", "2", "1"])


# In[ ]:




