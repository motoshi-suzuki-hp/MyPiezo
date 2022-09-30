#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np

df = pd.read_csv("incorrect_id.csv",sep="," )


# In[26]:


material_id = df['material_id']
replace_id = df['replace_id']


# In[29]:


df_rep = pd.DataFrame({'material_id' : material_id, 'replace_id' : replace_id})


# In[30]:


df_rep


# In[33]:


# jsonファイルから抽出
import json

json_open = open('piezo.json', 'r')
json_list = json.load(json_open)

print('json_list:{}'.format(type(json_list)))

material_index = []
for i in range(len(json_list)):
    material_index.append(json_list[i]['meta']['material_id'])
df_mi = pd.DataFrame(material_index)


# In[34]:


df_mi


# In[37]:


li_mi = df_rep['material_id'].values.tolist()
li_ri = df_rep['replace_id'].values.tolist()


# In[39]:


material_index_rep = df_mi.replace(li_mi, li_ri)


# In[65]:


material_index_rep


# In[107]:


material_index_rep_dropna = material_index_rep.dropna()


# In[108]:


material_index_rep_dropna = material_index_rep_dropna.T


# In[110]:


material_index_rep_dropna


# In[111]:


len(material_index_rep_dropna.columns)


# In[112]:


li_mi_rep_na = []
for i in range(len(material_index_rep_dropna.columns)):
    li_mi_rep_na.append(material_index_rep_dropna.iloc[0,i])


# In[113]:


li_mi_rep_na


# In[117]:


# 重複確認関数
def has_duplicates(seq):
    return len(seq) != len(set(seq))

print(has_duplicates(li_mi_rep_na))


# In[124]:


li_MI = set(li_mi_rep_na)
li_MI = list(li_MI)


# In[210]:


li_MI


# In[209]:


# ライブラリのインポート
import pymatgen
from pymatgen.ext.matproj import MPRester
import itertools
import pandas as pd

# Materials Projectに登録して取得したAPIキーを入力
API_KEY = 'qgGhptxR7Owa1uL6' 


# In[211]:


with MPRester(API_KEY) as m:
    df_MP = pd.DataFrame()
    #compoundはlist型
    for elements in li_MI:
        compound = m.get_data(elements, data_type='vasp')
        df_mp = pd.DataFrame(compound)           
        df_MP = pd.concat([df_MP,df_mp])
        

#結果を保存
df_MP.to_csv('material_piezo_list_924.csv')


# In[58]:


import pandas as pd
df_MP = pd.read_csv('material_piezo_list_924.csv')


# In[59]:


df_MP_2 = df_MP[['energy','energy_per_atom','volume','formation_energy_per_atom','nsites','nelements','e_above_hull','band_gap','density','total_magnetization','oxide_type','elasticity','piezo','diel']]


# In[60]:


print(df_MP_2['elasticity'].iat[0])


# In[61]:


df_MP_2_na = df_MP_2.dropna(how='any')


# In[111]:


df_MP_2_na = df_MP_2_na.reset_index()


# In[112]:


df_MP_2_na.drop('index', axis=1)


# In[113]:


import json
li_idx = []

# print(json.dumps(df_MP_2['elasticity'].iat[0]))

for i in range(len(df_MP_2_na)):
    if json.dumps(df_MP_2_na['elasticity'].iat[i]) == 'null' or json.dumps(df_MP_2_na['piezo'].iat[i]) == 'null' or json.dumps(df_MP_2_na['diel'].iat[i]) == 'null':
        li_idx.append(i)
print(li_idx)
df_MP_3 = df_MP_2_na.drop(df_MP_2_na.index[li_idx],axis=0)


# In[114]:


oxide_num = []

for ox in df_MP_3['oxide_type']:
    if ox == 'None':
        oxide_num.append(0)
    else:
        oxide_num.append(1)

print(oxide_num)


# In[115]:


df_MP_3 = df_MP_3.drop('oxide_type',axis=1)


# In[116]:


df_MP_3['oxide_num'] = oxide_num


# In[120]:


df_MP_3 = df_MP_3.drop('index',axis=1)


# In[121]:


df_MP_3


# In[122]:


df_MP_3.columns


# In[123]:


data_energy = df_MP_3['energy']
data_energy_per_atom = df_MP_3['energy_per_atom']
data_volume = df_MP_3['volume']
data_formation_energy_per_atom = df_MP_3['formation_energy_per_atom']
data_nsites = df_MP_3['nsites']
data_nelements = df_MP_3['nelements']
data_e_above_hull = df_MP_3['e_above_hull']
data_band_gap = df_MP_3['band_gap']                
data_density = df_MP_3['density']               
data_total_magnetization = df_MP_3['total_magnetization']
data_elasticity = df_MP_3['elasticity']
data_piezo = df_MP_3['piezo']
data_diel = df_MP_3['diel']
data_oxide_num = df_MP_3['oxide_num']


# In[ ]:


data_energy = df_MP['energy']
data_energy_per_atom = df_MP['energy_per_atom']
data_volume = df_MP['volume']
data_formation_energy_per_atom = df_MP['formation_energy_per_atom']
data_nsites = df_MP['nsites']

data_nelements = df_MP['nelements']
data_e_above_hull = df_MP['e_above_hull']

data_band_gap = df_MP['band_gap']                
data_density = df_MP['density']

data_total_magnetization = df_MP['total_magnetization']

data_elasticity = df_MP['elasticity']
data_piezo = df_MP['piezo']
data_diel = df_MP['diel']


# In[124]:


import ast


# In[125]:


ast.literal_eval(data_elasticity.iat[0])


# In[126]:


elas0 = ast.literal_eval(data_elasticity.iat[0])
elas0['elastic_tensor'][0][1]


# In[127]:


G_Reuss = []
G_VRH = []
G_Voigt = []
G_Voigt_Reuss_Hill = []
K_Reuss = []
K_VRH = []
K_Voigt = []
K_Voigt_Reuss_Hill = []
elastic_anisotropy = []
elastic_tensor00 = []
elastic_tensor01 = []
elastic_tensor02 = []
elastic_tensor03 = []
elastic_tensor04 = []
elastic_tensor05 = []
elastic_tensor10 = []
elastic_tensor11 = []
elastic_tensor12 = []
elastic_tensor13 = []
elastic_tensor14 = []
elastic_tensor15 = []
elastic_tensor20 = []
elastic_tensor21 = []
elastic_tensor22 = []
elastic_tensor23 = []
elastic_tensor24 = []
elastic_tensor25 = []
elastic_tensor30 = []
elastic_tensor31 = []
elastic_tensor32 = []
elastic_tensor33 = []
elastic_tensor34 = []
elastic_tensor35 = []
elastic_tensor40 = []
elastic_tensor41 = []
elastic_tensor42 = []
elastic_tensor43 = []
elastic_tensor44 = []
elastic_tensor45 = []
elastic_tensor50 = []
elastic_tensor51 = []
elastic_tensor52 = []
elastic_tensor53 = []
elastic_tensor54 = []
elastic_tensor55 = []
homogeneous_poisson = []
poisson_ratio = []
universal_anisotropy = []
elastic_tensor_original = []
compliance_tensor00 = []
compliance_tensor01 = []
compliance_tensor02 = []
compliance_tensor03 = []
compliance_tensor04 = []
compliance_tensor05 = []
compliance_tensor10 = []
compliance_tensor11 = []
compliance_tensor12 = []
compliance_tensor13 = []
compliance_tensor14 = []
compliance_tensor15 = []
compliance_tensor20 = []
compliance_tensor21 = []
compliance_tensor22 = []
compliance_tensor23 = []
compliance_tensor24 = []
compliance_tensor25 = []
compliance_tensor30 = []
compliance_tensor31 = []
compliance_tensor32 = []
compliance_tensor33 = []
compliance_tensor34 = []
compliance_tensor35 = []
compliance_tensor40 = []
compliance_tensor41 = []
compliance_tensor42 = []
compliance_tensor43 = []
compliance_tensor44 = []
compliance_tensor45 = []
compliance_tensor50 = []
compliance_tensor51 = []
compliance_tensor52 = []
compliance_tensor53 = []
compliance_tensor54 = []
compliance_tensor55 = []
nsites = []

print(type(data_elasticity.iat[0]))
for i in range(len(df_MP_3)):
    s = ast.literal_eval(data_elasticity.iat[i])
    G_Reuss.append(s['G_Reuss'])
    G_VRH.append(s['G_VRH'])
    G_Voigt.append(s['G_Voigt'])
    G_Voigt_Reuss_Hill.append(s['G_Voigt_Reuss_Hill'])
    K_Reuss.append(s['K_Reuss'])
    K_VRH.append(s['K_VRH'])
    K_Voigt.append(s['K_Voigt'])
    K_Voigt_Reuss_Hill.append(s['K_Voigt_Reuss_Hill'])
    elastic_anisotropy.append(s['elastic_anisotropy'])
    elastic_tensor00.append(s['elastic_tensor'][0][0])
    elastic_tensor01.append(s['elastic_tensor'][0][1])
    elastic_tensor02.append(s['elastic_tensor'][0][2])
    elastic_tensor03.append(s['elastic_tensor'][0][3])
    elastic_tensor04.append(s['elastic_tensor'][0][4])
    elastic_tensor05.append(s['elastic_tensor'][0][5])
    elastic_tensor10.append(s['elastic_tensor'][1][0])
    elastic_tensor11.append(s['elastic_tensor'][1][1])
    elastic_tensor12.append(s['elastic_tensor'][1][2])
    elastic_tensor13.append(s['elastic_tensor'][1][3])
    elastic_tensor14.append(s['elastic_tensor'][1][4])
    elastic_tensor15.append(s['elastic_tensor'][1][5])
    elastic_tensor20.append(s['elastic_tensor'][2][0])
    elastic_tensor21.append(s['elastic_tensor'][2][1])
    elastic_tensor22.append(s['elastic_tensor'][2][2])
    elastic_tensor23.append(s['elastic_tensor'][2][3])
    elastic_tensor24.append(s['elastic_tensor'][2][4])
    elastic_tensor25.append(s['elastic_tensor'][2][5])
    elastic_tensor30.append(s['elastic_tensor'][3][0])
    elastic_tensor31.append(s['elastic_tensor'][3][1])
    elastic_tensor32.append(s['elastic_tensor'][3][2])
    elastic_tensor33.append(s['elastic_tensor'][3][3])
    elastic_tensor34.append(s['elastic_tensor'][3][4])
    elastic_tensor35.append(s['elastic_tensor'][3][5])
    elastic_tensor40.append(s['elastic_tensor'][4][0])
    elastic_tensor41.append(s['elastic_tensor'][4][1])
    elastic_tensor42.append(s['elastic_tensor'][4][2])
    elastic_tensor43.append(s['elastic_tensor'][4][3])
    elastic_tensor44.append(s['elastic_tensor'][4][4])
    elastic_tensor45.append(s['elastic_tensor'][4][5])
    elastic_tensor50.append(s['elastic_tensor'][5][0])
    elastic_tensor51.append(s['elastic_tensor'][5][1])
    elastic_tensor52.append(s['elastic_tensor'][5][2])
    elastic_tensor53.append(s['elastic_tensor'][5][3])
    elastic_tensor54.append(s['elastic_tensor'][5][4])
    elastic_tensor55.append(s['elastic_tensor'][5][5])
    homogeneous_poisson.append(s['homogeneous_poisson'])
    poisson_ratio.append(s['poisson_ratio'])
    universal_anisotropy.append(s['universal_anisotropy'])
    # elastic_tensor_original.append(data_elasticity.iat[i]['elastic_tensor_original'])
    compliance_tensor00.append(s['compliance_tensor'][0][0])
    compliance_tensor01.append(s['compliance_tensor'][0][1])
    compliance_tensor02.append(s['compliance_tensor'][0][2])
    compliance_tensor03.append(s['compliance_tensor'][0][3])
    compliance_tensor04.append(s['compliance_tensor'][0][4])
    compliance_tensor05.append(s['compliance_tensor'][0][5])
    compliance_tensor10.append(s['compliance_tensor'][1][0])
    compliance_tensor11.append(s['compliance_tensor'][1][1])
    compliance_tensor12.append(s['compliance_tensor'][1][2])
    compliance_tensor13.append(s['compliance_tensor'][1][3])
    compliance_tensor14.append(s['compliance_tensor'][1][4])
    compliance_tensor15.append(s['compliance_tensor'][1][5])
    compliance_tensor20.append(s['compliance_tensor'][2][0])
    compliance_tensor21.append(s['compliance_tensor'][2][1])
    compliance_tensor22.append(s['compliance_tensor'][2][2])
    compliance_tensor23.append(s['compliance_tensor'][2][3])
    compliance_tensor24.append(s['compliance_tensor'][2][4])
    compliance_tensor25.append(s['compliance_tensor'][2][5])
    compliance_tensor30.append(s['compliance_tensor'][3][0])
    compliance_tensor31.append(s['compliance_tensor'][3][1])
    compliance_tensor32.append(s['compliance_tensor'][3][2])
    compliance_tensor33.append(s['compliance_tensor'][3][3])
    compliance_tensor34.append(s['compliance_tensor'][3][4])
    compliance_tensor35.append(s['compliance_tensor'][3][5])
    compliance_tensor40.append(s['compliance_tensor'][4][0])
    compliance_tensor41.append(s['compliance_tensor'][4][1])
    compliance_tensor42.append(s['compliance_tensor'][4][2])
    compliance_tensor43.append(s['compliance_tensor'][4][3])
    compliance_tensor44.append(s['compliance_tensor'][4][4])
    compliance_tensor45.append(s['compliance_tensor'][4][5])
    compliance_tensor50.append(s['compliance_tensor'][5][0])
    compliance_tensor51.append(s['compliance_tensor'][5][1])
    compliance_tensor52.append(s['compliance_tensor'][5][2])
    compliance_tensor53.append(s['compliance_tensor'][5][3])
    compliance_tensor54.append(s['compliance_tensor'][5][4])
    compliance_tensor55.append(s['compliance_tensor'][5][5])
    nsites.append(s['nsites'])
    


# In[33]:


print(G_Reuss)
print(poisson_ratio)


# In[ ]:





# In[128]:


ast.literal_eval(data_piezo.iat[0])


# In[129]:


s = ast.literal_eval(data_piezo.iat[0])
s['v_max'][2]


# In[130]:


eij_max = []
piezoelectric_tensor00 = []
piezoelectric_tensor01 = []
piezoelectric_tensor02 = []
piezoelectric_tensor03 = []
piezoelectric_tensor04 = []
piezoelectric_tensor05 = []
piezoelectric_tensor10 = []
piezoelectric_tensor11 = []
piezoelectric_tensor12 = []
piezoelectric_tensor13 = []
piezoelectric_tensor14 = []
piezoelectric_tensor15 = []
piezoelectric_tensor20 = []
piezoelectric_tensor21 = []
piezoelectric_tensor22 = []
piezoelectric_tensor23 = []
piezoelectric_tensor24 = []
piezoelectric_tensor25 = []
v_max00 = []
v_max01 = []
v_max02 = []

for i in range(len(df_MP_3)):
    s = ast.literal_eval(data_piezo.iat[i])
    eij_max.append(s['eij_max'])
    piezoelectric_tensor00.append(s['piezoelectric_tensor'][0][0])
    piezoelectric_tensor01.append(s['piezoelectric_tensor'][0][1])
    piezoelectric_tensor02.append(s['piezoelectric_tensor'][0][2])
    piezoelectric_tensor03.append(s['piezoelectric_tensor'][0][3])
    piezoelectric_tensor04.append(s['piezoelectric_tensor'][0][4])
    piezoelectric_tensor05.append(s['piezoelectric_tensor'][0][5])
    piezoelectric_tensor10.append(s['piezoelectric_tensor'][1][0])
    piezoelectric_tensor11.append(s['piezoelectric_tensor'][1][1])
    piezoelectric_tensor12.append(s['piezoelectric_tensor'][1][2])
    piezoelectric_tensor13.append(s['piezoelectric_tensor'][1][3])
    piezoelectric_tensor14.append(s['piezoelectric_tensor'][1][4])
    piezoelectric_tensor15.append(s['piezoelectric_tensor'][1][5])
    piezoelectric_tensor20.append(s['piezoelectric_tensor'][2][0])
    piezoelectric_tensor21.append(s['piezoelectric_tensor'][2][1])
    piezoelectric_tensor22.append(s['piezoelectric_tensor'][2][2])
    piezoelectric_tensor23.append(s['piezoelectric_tensor'][2][3])
    piezoelectric_tensor24.append(s['piezoelectric_tensor'][2][4])
    piezoelectric_tensor25.append(s['piezoelectric_tensor'][2][5])
    v_max00.append(s['v_max'][0])
    v_max01.append(s['v_max'][1])
    v_max02.append(s['v_max'][2])


# In[ ]:





# In[131]:


ast.literal_eval(data_diel.iat[0])


# In[132]:


e_electronic00 = []
e_electronic01 = []
e_electronic02 = []
e_electronic10 = []
e_electronic11 = []
e_electronic12 = []
e_electronic20 = []
e_electronic21 = []
e_electronic22 = []
e_total00 = []
e_total01 = []
e_total02 = []
e_total10 = []
e_total11 = []
e_total12 = []
e_total20 = []
e_total21 = []
e_total22 = []
n = []
poly_electronic = []
poly_total = []

for i in range(len(df_MP_3)):
    s = ast.literal_eval(data_diel.iat[i])
    e_electronic00.append(s['e_electronic'][0][0])
    e_electronic01.append(s['e_electronic'][0][1])
    e_electronic02.append(s['e_electronic'][0][2])
    e_electronic10.append(s['e_electronic'][1][0])
    e_electronic11.append(s['e_electronic'][1][1])
    e_electronic12.append(s['e_electronic'][1][2])
    e_electronic20.append(s['e_electronic'][2][0])
    e_electronic21.append(s['e_electronic'][2][1])
    e_electronic22.append(s['e_electronic'][2][2])
    e_total00.append(s['e_total'][0][0])
    e_total01.append(s['e_total'][0][1])
    e_total02.append(s['e_total'][0][2])
    e_total10.append(s['e_total'][1][0])
    e_total11.append(s['e_total'][1][1])
    e_total12.append(s['e_total'][1][2])
    e_total20.append(s['e_total'][2][2])
    e_total21.append(s['e_total'][2][2])
    e_total22.append(s['e_total'][2][2])
    n.append(s['n'])
    poly_electronic.append(s['poly_electronic'])
    poly_total.append(s['poly_total'])


# In[ ]:





# In[133]:


data_energy


# In[134]:


pd.Series(poly_total)


# In[136]:


this_is_data = pd.concat([data_energy, data_energy_per_atom, data_volume, data_formation_energy_per_atom, data_nsites, data_nelements, data_e_above_hull, data_band_gap, data_density, data_total_magnetization, data_oxide_num, 
                          pd.Series(G_Reuss), pd.Series(G_VRH), pd.Series(G_Voigt), pd.Series(G_Voigt_Reuss_Hill), pd.Series(K_Reuss), pd.Series(K_VRH), pd.Series(K_Voigt), pd.Series(K_Voigt_Reuss_Hill), pd.Series(elastic_anisotropy), 
                          pd.Series(elastic_tensor00), pd.Series(elastic_tensor01), pd.Series(elastic_tensor02), pd.Series(elastic_tensor03), pd.Series(elastic_tensor04), pd.Series(elastic_tensor05), 
                          pd.Series(elastic_tensor10), pd.Series(elastic_tensor11), pd.Series(elastic_tensor12), pd.Series(elastic_tensor13), pd.Series(elastic_tensor14), pd.Series(elastic_tensor15), 
                          pd.Series(elastic_tensor20), pd.Series(elastic_tensor21), pd.Series(elastic_tensor22), pd.Series(elastic_tensor23), pd.Series(elastic_tensor24), pd.Series(elastic_tensor25), 
                          pd.Series(elastic_tensor30), pd.Series(elastic_tensor31), pd.Series(elastic_tensor32), pd.Series(elastic_tensor33), pd.Series(elastic_tensor34), pd.Series(elastic_tensor35), 
                          pd.Series(elastic_tensor40), pd.Series(elastic_tensor41), pd.Series(elastic_tensor42), pd.Series(elastic_tensor43), pd.Series(elastic_tensor44), pd.Series(elastic_tensor45), 
                          pd.Series(elastic_tensor50), pd.Series(elastic_tensor51), pd.Series(elastic_tensor52), pd.Series(elastic_tensor53), pd.Series(elastic_tensor54), pd.Series(elastic_tensor55), 
                          pd.Series(homogeneous_poisson), pd.Series(poisson_ratio), pd.Series(universal_anisotropy), 
                          pd.Series(compliance_tensor00), pd.Series(compliance_tensor01), pd.Series(compliance_tensor02), pd.Series(compliance_tensor03), pd.Series(compliance_tensor04), pd.Series(compliance_tensor05), 
                          pd.Series(compliance_tensor10), pd.Series(compliance_tensor11), pd.Series(compliance_tensor12), pd.Series(compliance_tensor13), pd.Series(compliance_tensor14), pd.Series(compliance_tensor15), 
                          pd.Series(compliance_tensor20), pd.Series(compliance_tensor21), pd.Series(compliance_tensor22), pd.Series(compliance_tensor23), pd.Series(compliance_tensor24), pd.Series(compliance_tensor25), 
                          pd.Series(compliance_tensor30), pd.Series(compliance_tensor31), pd.Series(compliance_tensor32), pd.Series(compliance_tensor33), pd.Series(compliance_tensor34), pd.Series(compliance_tensor35), 
                          pd.Series(compliance_tensor40), pd.Series(compliance_tensor41), pd.Series(compliance_tensor42), pd.Series(compliance_tensor43), pd.Series(compliance_tensor44), pd.Series(compliance_tensor45), 
                          pd.Series(compliance_tensor50), pd.Series(compliance_tensor51), pd.Series(compliance_tensor52), pd.Series(compliance_tensor53), pd.Series(compliance_tensor54), pd.Series(compliance_tensor55), 
                          pd.Series(nsites), pd.Series(eij_max), 
                          pd.Series(piezoelectric_tensor00), pd.Series(piezoelectric_tensor01), pd.Series(piezoelectric_tensor02), pd.Series(piezoelectric_tensor03), pd.Series(piezoelectric_tensor04), pd.Series(piezoelectric_tensor05), 
                          pd.Series(piezoelectric_tensor10), pd.Series(piezoelectric_tensor11), pd.Series(piezoelectric_tensor12), pd.Series(piezoelectric_tensor13), pd.Series(piezoelectric_tensor14), pd.Series(piezoelectric_tensor15), 
                          pd.Series(piezoelectric_tensor20), pd.Series(piezoelectric_tensor21), pd.Series(piezoelectric_tensor22), pd.Series(piezoelectric_tensor23), pd.Series(piezoelectric_tensor24), pd.Series(piezoelectric_tensor25), 
                          pd.Series(v_max00), pd.Series(v_max01), pd.Series(v_max02), 
                          pd.Series(e_electronic00), pd.Series(e_electronic01), pd.Series(e_electronic02), 
                          pd.Series(e_electronic10), pd.Series(e_electronic11), pd.Series(e_electronic12), 
                          pd.Series(e_electronic20), pd.Series(e_electronic21), pd.Series(e_electronic22), 
                          pd.Series(e_total00), pd.Series(e_total01), pd.Series(e_total02), 
                          pd.Series(e_total10), pd.Series(e_total11), pd.Series(e_total12), 
                          pd.Series(e_total20), pd.Series(e_total21), pd.Series(e_total22), 
                          pd.Series(n), pd.Series(poly_electronic), pd.Series(poly_total)], axis=1)

this_is_data.columns = ["ata_energy", "data_energy_per_atom", "data_volume", "data_formation_energy_per_atom", "data_nsites", "data_nelements", "data_e_above_hull", "data_band_gap", "data_density", "data_total_magnetization", "data_oxide_num", 
                        "G_Reuss", "G_VRH", "G_Voigt", "G_Voigt_Reuss_Hill", "K_Reuss", "K_VRH", "K_Voigt", "K_Voigt_Reuss_Hill", "elastic_anisotropy", 
                        "elastic_tensor00", "elastic_tensor01", "elastic_tensor02", "elastic_tensor03", "elastic_tensor04", "elastic_tensor05", 
                        "elastic_tensor10", "elastic_tensor11", "elastic_tensor12", "elastic_tensor13", "elastic_tensor14", "elastic_tensor15", 
                        "elastic_tensor20", "elastic_tensor21", "elastic_tensor22", "elastic_tensor23", "elastic_tensor24", "elastic_tensor25", 
                        "elastic_tensor30", "elastic_tensor31", "elastic_tensor32", "elastic_tensor33", "elastic_tensor34", "elastic_tensor35", 
                        "elastic_tensor40", "elastic_tensor41", "elastic_tensor42", "elastic_tensor43", "elastic_tensor44", "elastic_tensor45", 
                        "elastic_tensor50", "elastic_tensor51", "elastic_tensor52", "elastic_tensor53", "elastic_tensor54", "elastic_tensor55", 
                        "homogeneous_poisson", "poisson_ratio", "universal_anisotropy", 
                        "compliance_tensor00", "compliance_tensor01", "compliance_tensor02", "compliance_tensor03", "compliance_tensor04", "compliance_tensor05", 
                        "compliance_tensor10", "compliance_tensor11", "compliance_tensor12", "compliance_tensor13", "compliance_tensor14", "compliance_tensor15", 
                        "compliance_tensor20", "compliance_tensor21", "compliance_tensor22", "compliance_tensor23", "compliance_tensor24", "compliance_tensor25", 
                        "compliance_tensor30", "compliance_tensor31", "compliance_tensor32", "compliance_tensor33", "compliance_tensor34", "compliance_tensor35", 
                        "compliance_tensor40", "compliance_tensor41", "compliance_tensor42", "compliance_tensor43", "compliance_tensor44", "compliance_tensor45", 
                        "compliance_tensor50", "compliance_tensor51", "compliance_tensor52", "compliance_tensor53", "compliance_tensor54", "compliance_tensor55", 
                        "nsites", "eij_max", 
                        "piezoelectric_tensor00", "piezoelectric_tensor01", "piezoelectric_tensor02", "piezoelectric_tensor03", "piezoelectric_tensor04", "piezoelectric_tensor05", 
                        "piezoelectric_tensor10", "piezoelectric_tensor11", "piezoelectric_tensor12", "piezoelectric_tensor13", "piezoelectric_tensor14", "piezoelectric_tensor15", 
                        "piezoelectric_tensor20", "piezoelectric_tensor21", "piezoelectric_tensor22", "piezoelectric_tensor23", "piezoelectric_tensor24", "piezoelectric_tensor25", 
                        "v_max00", "v_max01", "v_max02", 
                        "e_electronic00", "e_electronic01", "e_electronic02", 
                        "e_electronic10", "e_electronic11", "e_electronic12", 
                        "e_electronic20", "e_electronic21", "e_electronic22", 
                        "e_total00", "e_total01", "e_total02", 
                        "e_total10", "e_total11", "e_total12", 
                        "e_total20", "e_total21", "e_total22", 
                        "n", "poly_electronic", "poly_total"]


# In[137]:


print(this_is_data)


# In[141]:


this_is_data.to_csv('this_is_data.csv')


# In[ ]:




