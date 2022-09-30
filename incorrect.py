#!/usr/bin/env python
# coding: utf-8

# In[18]:


import json

json_open = open('piezo.json', 'r')
json_list = json.load(json_open)

print('json_list:{}'.format(type(json_list)))

material_formula = []
material_id = []
for i in range(len(json_list)):
    material_formula.append(json_list[i]['meta']['formula'])
    material_id.append(json_list[i]['meta']['material_id'])


# In[26]:


import pandas as pd

df = pd.DataFrame({'material_id' : material_id, 'material_formula' : material_formula})


# In[24]:


df


# In[27]:


df2 = df.query('material_id in ["mp-24948", "mp-764673", "mp-615152", "mp-764425", "mp-767274", "mp-24942", "mp-561689", "mp-762221", "mp-771637", "mp-765904", "mp-776939", "mp-765254", "mp-775531", "mp-626075", "mp-765867", "mp-765359", "mp-766864", "mp-561926", "mp-625052", "mp-770149", "mp-764697", "mp-765553", "mp-765859", "mp-767069", "mp-770603", "mp-767263", "mp-765877", "mp-777130", "mp-770252", "mp-765334", "mp-766149", "mp-766842", "mp-771797", "mp-626878", "mp-763348", "mp-763498", "mp-625717", "mp-763052", "mp-781958", "mp-561804", "mp-25503", "mp-772012", "mp-778780", "mp-773569", "mp-24864", "mp-25483", "mp-765198", "mp-626902", "mp-764943", "mp-774101", "mp-766949", "mp-765272", "mp-559001", "mp-763136", "mp-675163", "mp-774147", "mp-557733", "mp-626102", "mp-779211", "mp-625081", "mp-767108", "mp-765875", "mp-32479", "mp-765437", "mp-780753", "mp-764716", "mp-765135", "mp-763696", "mp-766941", "mp-559146", "mp-626881", "mp-764144", "mp-766964", "mp-761325", "mp-764895", "mp-549166", "mp-774149", "mp-25119", "mp-557515", "mp-767123", "mp-765444", "mp-561475", "mp-774003", "mp-765436", "mp-690635", "mp-765525", "mp-625056", "mp-542980", "mp-765182", "mp-764320", "mp-31649", "mp-767044", "mp-764312", "mp-767367", "mp-614005", "mp-782714", "mp-853167", "mp-31935", "mp-766115", "mp-613442", "mp-12992", "mp-699343", "mp-764829", "mp-853130", "mp-625953", "mp-765849", "mp-557291", "mp-565669", "mp-772246", "mp-763323", "mp-776563", "mp-779948", "mp-849318", "mp-31928", "mp-565192", "mp-764338", "mp-557739", "mp-764285", "mp-767186", "mp-31785", "mp-773224", "mp-766909", "mp-775985", "mp-32057", "mp-763095", "mp-765532", "mp-505200", "mp-24927", "mp-853165", "mp-766801", "mp-24932", "mp-639402", "mp-770986", "mp-766917", "mp-764698", "mp-762631"]')


# In[28]:


df2


# In[29]:


df2.to_csv('incorrect_id.csv')


# In[ ]:




