#!/usr/bin/env python
# coding: utf-8

# In[146]:


import pandas as pd
import numpy as np

df = pd.read_csv("material_piezo_list.csv",sep="," )


# In[147]:


df = df.drop(df.columns[0], axis=1)


# In[149]:


df


# In[175]:


import json

json_open = open('piezo.json', 'r')
json_list = json.load(json_open)

print('json_list:{}'.format(type(json_list)))

material_id = []
for i in range(len(json_list)):
    material_id.append(json_list[i]['meta']['material_id'])


# In[176]:


type(material_id)
type(df)


# In[177]:


mi = df['material_id'].to_list()


# In[183]:


mi[1]


# In[179]:


len(material_id)


# In[180]:


len(mi)


# In[181]:


print(set(material_id) ^ set(mi))


# In[182]:


len(set(material_id) ^ set(mi))


# In[17]:


df.tail()


# In[20]:


df_ele = df['elements']


# In[24]:


df_ele[0]


# In[30]:


df_ele[0][1]


# In[25]:


df_uniCelFor = df['unit_cell_formula']


# In[29]:


df_uniCelFor[0]


# In[ ]:





# In[ ]:


# import re
# find_ele = re.findall(r"\'.*\'",df_ele[0])


# In[38]:


# print(find_ele)


# In[47]:


df_ele0 = df_ele[0]


# In[51]:


df_ele00 = df_ele0.replace("'","")
df_ele00 = df_ele00.replace(",","")


# In[52]:


print(df_ele00)


# In[56]:


df_ele000 = df_ele00[1:len(df_ele00)-1].split()


# In[58]:


print(df_ele000[0])


# In[63]:


ele_list = []
for ele in df_ele:
    ele2 = ele.replace("'","")
    ele2 = ele2.replace(",","")
    ele3 = ele2[1:len(ele2)-1].split()
    ele_list.append(ele3)


# In[65]:


print(ele_list)


# In[66]:


ele_list[0][1]


# In[68]:


len(ele_list)


# In[73]:


ele_list_not_double = []

for i in range(len(ele_list)):
    for s in ele_list[i]:
        if s not in ele_list_not_double:
            ele_list_not_double.append(s)

print(ele_list_not_double)


# In[74]:


count_list = [0] * len(ele_list_not_double)

for i in range(len(ele_list)):
    for s in ele_list[i]:
        for j in range(len(ele_list_not_double)):
            if s == ele_list_not_double[j]:
                count_list[j] = count_list[j] + 1
                break

print(count_list)

    


# In[78]:


import matplotlib.pyplot as plt


# In[83]:


plt.figure(figsize=(18,12))
lst = list(range(1,len(ele_list_not_double)+1))
plt.bar(lst, count_list, tick_label=ele_list_not_double, align="center")


# In[90]:


df_extract = df[['energy','energy_per_atom','volume','formation_energy_per_atom','nsites','nelements','e_above_hull','band_gap','density','total_magnetization','oxide_type','elasticity','piezo','diel']]


# In[92]:


df['oxide_type']


# In[95]:


oxide_num = []

for ox in df['oxide_type']:
    if ox == 'None':
        oxide_num.append(0)
    elif ox == 'oxide':
        oxide_num.append(1)
    elif ox == 'hydroxide':
        oxide_num.append(2)
    elif ox == 'ozonide':
        oxide_num.append(3)
    elif ox == 'peroxide':
        oxide_num.append(4)
    elif ox == 'superoxide':
        oxide_num.append(5)
    else:
        print('error')

print(oxide_num)


# In[96]:


len(oxide_num)


# In[108]:


oxide_num2 = []

for ox in df['oxide_type']:
    if ox == 'None':
        oxide_num2.append(0)
    else:
        oxide_num2.append(1)

print(oxide_num2)


# In[115]:


df_extract2 = df_extract.drop('oxide_type',axis=1)


# In[116]:


df_extract2['oxide_num2'] = oxide_num2


# In[119]:


df_extract2


# In[144]:


len(df_extract2)


# In[186]:


df_ex3 = df_extract2


# In[193]:


df_ex4 = pd.DataFrame(df_ex3.dropna(how='any'))
df_ex4


# In[194]:


len(df_ex4)


# In[200]:


df_ex4['elasticity'][0]


# In[201]:


type(df_ex4['elasticity'][0])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[187]:


df_extract2['piezo'][0]


# In[141]:


ex20 = df_extract2['piezo'][0]
ex20 = ex20.replace("{'eij_max': ","*")
ex20 = ex20.replace(", 'piezoelectric_tensor': ","* *")
ex20 = ex20.replace(", 'v_max': ","* *")
ex20 = ex20.replace("}","*")
print(ex20)


# In[136]:


ex20 = ex20[1:len(ex20)-1].split("* *")
print(ex20)


# In[137]:


ex20[0]


# In[145]:


df['piezo']


# In[143]:


G_Reuss = []
G_VRH = []
G_Voigt = []

for i in range(len(df_extract2)):
    ex20 = df['piezo'][i]
    ex20 = ex20.replace("{'eij_max': ","*")
    ex20 = ex20.replace(", 'piezoelectric_tensor': ","* *")
    ex20 = ex20.replace(", 'v_max': ","* *")
    ex20 = ex20.replace("}","*")
    ex20 = ex20[1:len(ex20)-1].split("* *")
    G_Reuss.append(ex20[0])
    G_VRH.append(ex20[1])
    G_Voigt.append(ex20[2])
    
print(G_Reuss)
print(G_VRH)
print(G_Voigt)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




