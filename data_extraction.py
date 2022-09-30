#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json

json_open = open('piezo.json', 'r')
json_list = json.load(json_open)

print('json_list:{}'.format(type(json_list)))

material_formula = []
for i in range(len(json_list)):
    material_formula.append(json_list[i]['meta']['formula'])


# In[7]:


print(material_formula)


# In[23]:


material_eij = []
for i in range(len(json_list)):
    material_eij.append(json_list[i]['eij_max'])


# In[24]:


print(material_eij)


# In[25]:


material_index = []
for i in range(len(json_list)):
    material_index.append(json_list[i]['meta']['material_id'])


# In[26]:


print(material_index)


# In[30]:


len(material_index)


# In[3]:


get_ipython().system('python -m pip install --upgrade pip setuptools')


# In[4]:


get_ipython().system('pip install pymatgen')


# In[3]:


conda install -c conda-forge pymatgen


# In[4]:


# ライブラリのインポート
import pymatgen
from pymatgen.ext.matproj import MPRester
import itertools
import pandas as pd

# Materials Projectに登録して取得したAPIキーを入力
API_KEY = 'qgGhptxR7Owa1uL6' 


# In[27]:


with MPRester(API_KEY) as m:
    df_MP = pd.DataFrame()
    #compoundはlist型
    for elements in material_index:
        compound = m.get_data(elements, data_type='vasp')
        df_mp = pd.DataFrame(compound)           
        df_MP = df_MP.append(df_mp)

#結果を保存
df_MP.to_csv('material_piezo_list.csv')


# In[28]:


df_MP.shape


# In[29]:


df_MP.head(10)


# In[ ]:




